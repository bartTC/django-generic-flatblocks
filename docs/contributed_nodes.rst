.. _ref-contributed-nodes:

Contributed content nodes
=========================

django-generic-flatblocks comes with some very commonly used content-nodes.
They are not installed by default. To do so, insert ``django_generic_flatblocks.contrib.gblocks``
to your ``INSTALLED_APPS`` in your settings and resync your database:
``./manage.py syncdb``.

The contributed content nodes are:

- **gblocks.Title**: A CharField rendered as a <h2> Tag.

- **gblocks.Text**: A TextField rendered as html paragraphs. (This is what
  django-chunks provides)

- **gblocks.Image**: A ImageField rendered as <img> Tag.

- **gblocks.TitleAndText**: A CharField and a TextField. (This is what
  django-flatblocks provides)

- **gblocks.TitleTextAndImage**: A CharField, TextField and ImageField

So if you want to display a title and textfield, use this templatetag for 
example::

    {% gblock "about_me" for "gblocks.TitleAndText" %}
