.. _quickstart:



==========
Quickstart
==========

You can join unlimited of slug-strings or context-variables to one slug. Most
commonly you will do this if you need to use the users LANGUAGE_CODE in your
slug, to have different content nodes for every language::

    {% load generic_flatblocks %}
    {% gblock "website","title",LANGUAGE_CODE for "gblocks.Title" %}

The slug can also be a context variable::

    {% with "website_teaser" as my_slug %}
        {% gblock my_slug for "gblocks.Text" %}
    {% endwith %}

You can render each generic block with a template of your choice::

    {% gblock "website_urgent_notice" for "gblocks.Text" with "urgent.html" %}

You can pass an integer as slug. In this case, generic-flatblocks
will fetch the model instance with the primary key you named in slug.
Basically this is a {% include %} tag on model level::

    {% gblock 1 for "auth.user" with "current_user.html" %}

You can store the related object directly in the context using
the "into" argument. This is the quickest way to display any
model. The "for" and "as" arguments are ignored::

    {% gblock 1 for "auth.user" into "the_user_object" %}
    <p>The first user is {{ the_user_object.username }}!</p>
    {% if the_user_object_admin_url %}<a href="{{ the_user_object_admin_url }}">edit</a>{% endif %}


Let's create an flatblock with a "as" argument. We publish this
block at the end of this page in a variable called ``FOOTER``::

    {% gblock "footer" for "gblocks.Text" as "FOOTER" %}

    {{ FOOTER }}

