from django.test import TestCase
from django.conf import settings
from django.core.context_processors import PermWrapper
from django.template import Template, TemplateDoesNotExist, TemplateSyntaxError
from django.template.context import Context
from django.core.exceptions import ObjectDoesNotExist


class HttpRequest(object):
    """
    Stupid simple HttpRequest class to store a user. May need to be expaneded
    in the future to act more like the real deal.
    """
    def __init__(self, user):
        self.user = user


class GenericFlatblocksTestCase(TestCase):
    def setUp(self):
        # Create a dummy user
        from django.contrib.auth.models import User
        dummy_user = User.objects.create_user(u'johndoe', u'john@example.com', u'foobar')
        dummy_user.first_name = u'John'
        dummy_user.last_naem = u'Doe'
        dummy_user.save()
        
        self.assertEqual(dummy_user.pk, 1)
        self.dummy_user = dummy_user
        
        self.admin_user = User.objects.create_superuser(u'admin', u'admin@example.com', u'foobar')
    
    def tearDown(self):
        from django.contrib.auth.models import User
        User.objects.all().delete()

    def parseTemplate(self, template_string, admin_user=False):
        user = admin_user and self.admin_user or self.dummy_user
        t = Template(template_string)
        c = Context({'user': user,
                     'request': HttpRequest(user),
                     'LANGUAGE_CODE': 'en'})
        return t.render(c)

    def testModelBehaviour(self):
        """
        Direct flatblock creation.
        """
        from django_generic_flatblocks.models import GenericFlatblock
        from django_generic_flatblocks.contrib.gblocks.models import Title

        title_obj = Title.objects.create(title=u'Hello World')
        generic_obj = GenericFlatblock()
        generic_obj.slug=u'hello_world'
        generic_obj.content_object=title_obj
        generic_obj.save()

        self.assertEqual(generic_obj.slug, u'hello_world')
        self.assertEqual(generic_obj.content_object, title_obj)
        self.assertEqual(generic_obj.__unicode__(), u'hello_world')

    def testSlugArgument(self):
        from django_generic_flatblocks.models import GenericFlatblock

        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock "title" for "gblocks.Title" %}
        {% gblock "title","foo" for "gblocks.Title" %}
        {% gblock "title","foo",LANGUAGE_CODE for "gblocks.Title" %}
        {% gblock "user",user.pk for "gblocks.Title" %}
        {% gblock "int","slug",1 for "gblocks.Title" %}
        '''
        self.parseTemplate(template_string)
        self.assertTrue(GenericFlatblock.objects.get(slug='title'))
        self.assertTrue(GenericFlatblock.objects.get(slug='title_foo'))
        self.assertTrue(GenericFlatblock.objects.get(slug='title_foo_en'))
        self.assertTrue(GenericFlatblock.objects.get(slug='user_1'))
        self.assertTrue(GenericFlatblock.objects.get(slug='int_slug_1'))

    def testSlugArgumentWithInteger(self):
        # Integer slug
        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock 1 for "auth.user" %}
        '''
        t = self.parseTemplate(template_string)
        self.assertTrue(self.dummy_user.username in t)

        # Integer slug with custom template
        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock 1 for "auth.user" with "auth/user/flatblock_firstname.html" %}
        '''
        t = self.parseTemplate(template_string)
        self.assertTrue(self.dummy_user.first_name in t)

        # Non exisiting integer, empty template
        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock 5 for "auth.user" %}
        '''
        t = self.parseTemplate(template_string)
        self.assertFalse(t.strip())

    def testForArgument(self):
        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock "title" for "foo.Bar" %}
        '''
        self.assertRaises(AttributeError, self.parseTemplate, template_string)

        # Missing for argument
        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock "title" %}
        '''
        self.assertRaises(TypeError, self.parseTemplate, template_string)

    def testWithArgument(self):
        # With template string
        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock "title" for "gblocks.Title" with "test_template.html" %}
        '''
        t = self.parseTemplate(template_string)
        self.assertTrue(u'<hello></hello>' in t)

        # Non existing templates should fallback to the default one
        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock "title" for "gblocks.Title" with "test_template_doesnotexist.html" %}
        '''
        t = self.parseTemplate(template_string)
        self.assertTrue(u'<h2></h2>' in t)

        # Raise exception if the template does not exist if TEMPLATE_DEBUG is True
        settings.TEMPLATE_DEBUG = True
        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock "title" for "auth.Permissions" %}
        '''
        self.assertRaises((TemplateDoesNotExist, TemplateSyntaxError), self.parseTemplate, template_string)
        settings.TEMPLATE_DEBUG = False

        # Fail silently if the template does not exist but TEMPLATE_DEBUG is False
        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock "title" for "auth.Permissions" %}
        '''
        self.assertTrue(self.parseTemplate(template_string).strip() == u'')

    def testAsArgument(self):
        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock "title" for "gblocks.Title" as "title_object" %}
        <div>{{ title_object }}</div>
        '''
        t = self.parseTemplate(template_string)
        t = ''.join(t.splitlines()) # Remove spaces
        self.assertTrue(u'<div><h2></h2></div>' in t)

    def testIntoArgument(self):
        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock "title" for "gblocks.Title" into "title_object" %}
        <foo>{{ title_object.title }}</foo>
        '''
        self.parseTemplate(template_string)

        from django_generic_flatblocks.models import GenericFlatblock
        o = GenericFlatblock.objects.get(slug='title')
        o.content_object.title = u'Into Argument'
        o.content_object.save()

        t = self.parseTemplate(template_string)
        self.assertTrue(u'<foo>Into Argument</foo>' in t)


        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock 1 for "auth.User" into "the_user" %}
        <foo>{{ the_user.username }}</foo>
        '''
        t = self.parseTemplate(template_string)
        self.assertTrue(u'<foo>johndoe</foo>' in t)


        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock 5 for "auth.User" into "the_user" %}
        <foo>{{ the_user.username }}</foo>
        '''
        t = self.parseTemplate(template_string)
        self.assertTrue(u'<foo></foo>' in t)


        from django.contrib.auth.models import User
        settings.TEMPLATE_DEBUG = True
        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock 5 for "auth.User" into "the_user" %}
        <foo>{{ the_user.username }}</foo>
        '''
        self.assertRaises((User.DoesNotExist, TemplateSyntaxError), self.parseTemplate, template_string)
        settings.TEMPLATE_DEBUG = False

    def testRelatedObjectDeletion(self):
        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock "title" for "gblocks.Title" into "title_object" %}
        <foo>{{ title_object.title }}</foo>
        '''
        self.parseTemplate(template_string)

        from django_generic_flatblocks.models import GenericFlatblock
        o = GenericFlatblock.objects.get(slug='title')
        old_content_object = o.content_object
        o.content_object.delete()

        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock "title" for "gblocks.Title" into "title_object" %}
        <foo>{{ title_object.title }}</foo>
        '''
        self.parseTemplate(template_string)
        o = GenericFlatblock.objects.get(slug='title')
        self.assertNotEqual(old_content_object, o.content_object)

    def testContributedModels(self):

        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock "title" for "gblocks.Title" %}
        {% gblock "text" for "gblocks.Text" %}
        {% gblock "image" for "gblocks.Image" %}
        {% gblock "title_and_text" for "gblocks.TitleAndText" %}
        {% gblock "title_text_and_image" for "gblocks.TitleTextAndImage" %}
        '''
        self.parseTemplate(template_string)

        from django_generic_flatblocks.contrib.gblocks import models
        from django_generic_flatblocks.models import GenericFlatblock
        self.assertTrue(isinstance(GenericFlatblock.objects.get(slug=u'title').content_object, models.Title))
        self.assertTrue(isinstance(GenericFlatblock.objects.get(slug=u'text').content_object, models.Text))
        self.assertTrue(isinstance(GenericFlatblock.objects.get(slug=u'image').content_object, models.Image))
        self.assertTrue(isinstance(GenericFlatblock.objects.get(slug=u'title_and_text').content_object, models.TitleAndText))
        self.assertTrue(isinstance(GenericFlatblock.objects.get(slug=u'title_text_and_image').content_object, models.TitleTextAndImage))
        
    def testAdminLink(self):
        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock "title" for "gblocks.Title" with "test_template.html" %}
        '''
        t = self.parseTemplate(template_string, admin_user=True)        
        self.assertTrue("/admin/gblocks/title/1/" in t)
        
        
        # The admin link gets appended to the "into" argument
        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock "title" for "gblocks.Title" into "title_object" %}
        {{ title_object_admin_url }}
        '''
        t = self.parseTemplate(template_string, admin_user=True)        
        self.assertTrue("/admin/gblocks/title/1/" in t)

        # You can define the admin prefix using a setting
        from django.conf import settings
        settings.ADMIN_URL_PREFIX = '/secret-admin-url/'
        
        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock "title" for "gblocks.Title" with "test_template.html" %}
        '''
        t = self.parseTemplate(template_string, admin_user=True)        
        self.assertTrue("/secret-admin-url/gblocks/title/1/" in t)
        

        template_string  = '''
        {% load generic_flatblocks %}
        {% gblock "title" for "gblocks.Title" into "title_object" %}
        {{ title_object_admin_url }}
        '''
        t = self.parseTemplate(template_string, admin_user=True)        
        self.assertTrue("/secret-admin-url/gblocks/title/1/" in t)