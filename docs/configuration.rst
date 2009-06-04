..  _configuration:

Configuration
=============

1. Insert ``django_generic_flatblocks`` to your ``INSTALLED_APPS`` in your
   settings. 
   
2. (optional) Define the url prefix to your contrib.admin installation in the
   setting ``ADMIN_URL_PREFIX``. Most commonly this is ``/admin/``. Beware
   the trailing slash.
  
3. Resync your database: ``./manage.py syncdb``

Next step is: :ref:`ref-usage`