.. _ref-creating-nodes:

============================
Create your own content node
============================

A content node is a simple django-model. No quirks. If you want to use a title
and a textfield as your content-node, define a new model ``Entry`` in your
application ``myproject``::

    from django.db import models
    from django.contrib import admin
    from django.utils.encoding import python_2_unicode_compatible

    @python_2_unicode_compatible
    class Entry(models.Model):
        title = models.CharField(max_length=255, blank=True)
        content = models.TextField(blank=True)

        def __str__(self):
            return self.title

    admin.site.register(Entry)

.. important::
    django-generic-flatblocks creates an empty content-node upon first
    request, so make sure each field has either it's default value or
    allow ``blank=True``. Don't forget to register your Model in the
    admin backend, if you want to edit it there.

Then create a template ``myproject/entry/flatblock.html`` in your
template directory. This template is the default template to render the
content node, if you do not provide a unique template for it (*with*
argument).

In this template are all context-variables from the *parent* template
available plus some extra variables. See arguments/with above for details.

A common template source for the content node would be::

    <h1>{{ object.title }}</h1>
    {{ object.content|safe }}

    {% if admin_url %}<a href="{{ admin_url }}">edit this</a>{% endif %}

In your templates, create a new content node using the templatetag::

    {% gblock "about_me" for "myproject.Entry" %}

For some pre defined nodes see :ref:`ref-contributed-nodes`
