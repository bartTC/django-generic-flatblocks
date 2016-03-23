.. _ref-usage:

==============
Detailed usage
==============

First of all, in every template you want to use generic-flatblocks, load the
templatetags library::

    {% load generic_flatblocks %}

Then define a content node using the ``gblock`` templatetag::

    {% gblock "unique_slug" for "applabel.modelname" with "render/with/template.html" as "variable" %}

The arguments in detail:
========================

**"unique_slug"** (required):
-----------------------------

The slug argument defines under which
*key* the content is stored in your database. You can define as many slugs
as you want, just use a comma as separator. You can use context-variables as 
well. Examples::
  
    "homepage headline" becomes "homepage_headline"
    "homepage","headline" becomes "homepage_headline"
    "homepage_title",LANGUAGE_CODE becomes "homepage_title_en" (depends on the users locale code)
    "user",user.pk becomes "user_1" (depends on the primary key of the currently logged in user)

You can pass an *integer* as the slug. This will cause the templatetag to fetch
the model named in *for* with the primary key you named in *slug*. Example::
  
    {% gblock 1 for "auth.user" with "path/to/template.html" %}
  
This will fetch the auth.User with the primary key 1 and renders this model
object with the template "path/to/template.html". In this case, the
``generic_object`` in ``None``. Basically this is a ``{% include %}`` tag on
model level. This can also be a context variable.
  
*for* **"applabel.modelname"** (required):
------------------------------------------

The *for* argument defines, what content-node (model) will be used to store
and display the content. The format is *appname.modelname*. For some
contributed content-nodes see :ref:`ref-contributed-nodes` below.
This argument can be a context-variable.

*with* **"template_path"** (optional):
--------------------------------------

You can define a template that is used for rendering the content node. If you
do not provide any template, the default template ``<applabel>/<modelname>/flatblock.html``
is used. This argument can be a context-variable.

In this template are all context-variables from the *parent* template
available plus some extra variables:

- ``object``: This variable is the model-instance for the generic block.

- ``generic_object``: This variable is the model-instance for the generic
  content object itself. Mostly you don't need this.
  
- ``admin_url``: A URL to the change view of the current object. This variable
  is ``None`` if the current user has no change permissions for the object.
  
*as* **"variable name"** (optional):
--------------------------------------

If you provide a variable name, the *rendered content node* is stored in it.
Otherwise it's displayed directly. This argument can be a context-variable.
  
*into* **"variable_name"** (optional):
--------------------------------------

If you provide a variable name, the *related object* is stored in it. No
template rendering is done. The *with* and the *as* arguments are ignored.
This argument can be a context-variable.
  
After calling the gblock templatetag, you have the same variables available
as in the *with* template:
  
- ``variable_name``: This variable is the model-instance for the generic block.

- ``variable_name`` + ``"_genric_object"``: This variable is the model-instance for
  the generic content object itself. Mostly you don't need this.
  
- ``variable_name`` + ``"_admin_url"``: A URL to the change view of the current object.
  This variable is ``None`` if the current user has no change permissions for
  the object.
  
This is the quickest way to display any model instance or content-node
directly without creating a template::
  
    {% gblock 1 for "auth.User" into "theuser" %}
    The first user is {{ theuser.username }}! (<a href="{{ theuser_admin_url }}">edit</a>)

would be rendered as::
  
    The first user is johndoe! (<a href="/admin/auth/user/1/">edit</a>)

.. note::
   If you have `settings.TEMPLATE_DEBUG` set to `True` and your related object
   does not exist, the templatetag will raise a ObjectNotFound exception. It
   will fail silently if you set `settings.TEMPLATE_DEBUG` to `False` and
   return an (empty, not saved) instance of the related model.
