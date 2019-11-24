.. image:: https://img.shields.io/pypi/v/django-generic-flatblocks.svg
    :target: https://pypi.org/project/django-generic-flatblocks/

.. image:: https://travis-ci.org/bartTC/django-generic-flatblocks.svg?branch=master
    :target: https://travis-ci.org/bartTC/django-generic-flatblocks

.. image:: https://api.codacy.com/project/badge/Coverage/606e8ced3f0a48ee8a4b623cd8314b72
    :target: https://www.codacy.com/app/bartTC/django-generic-flatblocks

.. image:: https://api.codacy.com/project/badge/Grade/606e8ced3f0a48ee8a4b623cd8314b72
    :target: https://www.codacy.com/app/bartTC/django-generic-flatblocks

----

📖 **Full documentation: https://django-generic-flatblocks.readthedocs.io/**

=========================
django-generic-flatblocks
=========================

If you want to add tiny snippets of text to your site, manageable by the admin
backend, you would use either `django-chunks`_ or `django-flatblocks`_.
However, both of them have one problem: you are limited to a predefined
content field; a "text" field in chunks and a "title" and "text" field in
flatblocks.

django-generic-flatblocks solves this problem as it knows nothing about the
content itself. You *attach* your hand made content node (a simple model) where
you can define any fields you want.

.. _`django-flatblocks`: http://github.com/zerok/django-flatblocks/tree/master
.. _`django-chunks`: http://code.google.com/p/django-chunks/


