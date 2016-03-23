.. _installation:

Installation
============

This package is available through the python package index, pypi. You can
install the latest version by::

    pip install django-generic-flatblocks


Add the module to your ``INSTALLED_APPS`` in your settings::

    INSTALLED_APPS = (
        ...
        'django_generic_flatblocks',
        'django_generic_flatblocks.contrib.gblocks',  # Optional sample models
    )

Make sure that ``django.core.context_processors.request`` was added to your
``TEMPLATE`` options::

    TEMPLATES = [{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                ...

*(Optional)* Define the url prefix to your contrib.admin installation in the
setting ``ADMIN_URL_PREFIX``. Most commonly this is ``/admin/``. Beware
the trailing slash.

Migrate the database schemas::

    ./manage.py migrate

See :ref:`quickstart` for a quick demonstration or :ref:`ref-usage` for a
detailed integration.

