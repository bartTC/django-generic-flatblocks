from django.template import Library, Node
from django.template import TemplateSyntaxError, TemplateDoesNotExist, Variable
from django.template.loader import select_template
from django.conf import settings
from django.db.models.loading import get_model
from generic_flatblocks.models import GenericFlatblock

register = Library()

class GenericFlatblockNode(Node):
    def __init__(self, slug, modelname=None, template_path=None, variable_name=None):
        self.slug = slug
        self.modelname = modelname
        self.template_path = template_path
        self.variable_name = variable_name
    
    def get_content_object(self, modelname, slug):
        applabel, modellabel = modelname.split(".")
        related_model = get_model(applabel, modellabel)
        
        print slug
        try:
            # Objekt laden
            obj = GenericFlatblock.objects.get(slug=slug)
        except GenericFlatblock.DoesNotExist:
            # Objekt exisitert noch nicht, neu erstellen
            related_obj = related_model.objects.create()
            obj = GenericFlatblock.objects.create(slug=slug, content_object=related_obj)
        return obj        

    def resolve(self, var, context):
        """Resolves a variable if var is not in " or '"""
        if var[0] in ('"', "'") and var[-1] == var[0]:
            return var[1:-1]
        else:
            return Variable(var).resolve(context)
        
    def render(self, context):    
        
        # Get the content and related content object
        generic_object = self.get_content_object(
            modelname = self.resolve(self.modelname, context),
            slug = self.resolve(self.slug, context)
        )
        
        context['generic_object'] = generic_object
        context['object'] = generic_object.content_object

        # Render the template
        template_paths = []
        if self.template_path:
            template_paths.append(self.resolve(self.template_path, context))
        template_paths.append('%s/%s/flatblock.html' % \
            tuple(self.resolve(self.modelname, context).lower().split(".")))
            
        try: 
            t = select_template(template_paths)
        except:
            if settings.TEMPLATE_DEBUG:
                raise
            return ''
        content = t.render(context)
        
        # Set content as variable inside context, if variable_name is given
        if self.variable_name:
            context[self.resolve(self.variable_name, context)] = content
            return ''
        return content
        
def do_genericflatblock(parser, token):
    """
    {% genericflatblcok "slug" %}
    {% genericflatblcok "slug" for "appname.modelname" %}
    {% genericflatblcok "slug" for "appname.modelname" with "templatename.html" %}
    {% genericflatblcok "slug" for "appname.modelname" with "templatename.html" as "variable" %}
    """

    def next_bit_for(bits, key, if_none=None):
        try:
            # TODO: auf naechste variable pruefen
            return bits[bits.index(key)+1]
        except ValueError:
            return if_none
    
    bits = token.contents.split()
    args = {
        'slug': bits[1],
        'modelname': next_bit_for(bits, 'for'),
        'template_path': next_bit_for(bits, 'with'),
        'variable_name': next_bit_for(bits, 'as'),
    }
    return GenericFlatblockNode(**args)

register.tag('gblock', do_genericflatblock)