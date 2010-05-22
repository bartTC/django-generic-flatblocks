.. _changelog:

=========
Changelog
=========

**0.9.1** (backwards compatible)
    * Django 1.2 compatibility! Fixed a bug where tests did not pass
      under Django 1.2. Thanks to Brian Rosner for this.

**v0.9** (backwards compatible)
    * Fixed a bug where an integer was not allowed as a part of a slug.

**v0.4** (backwards compatible)
    * Added Danish translation.
    * Added better documentation.
    * Added unittests.
    * If you fetch a not existing "primary key" object the templatetag
      will fail silently if settings.TEMPLATE_DEBUG is False.

**v0.3.0** (2009-03-21)
    * Added the *into* argument. You can now display any instance directly
      without creating and rendering a template.

**v0.2.1** (2009-03-20)
    * You can now pass a context variable with a integer to fetch a specific
      object.
    
**v0.2.0** (2009-03-20)
    * Added the ability to pass an integer as slug. This will cause that the
      templatetag fetches the specific *for* model with the primary key named
      in *slug*.

**v0.1.2** (2009-03-20)
    * Switched from distutils to setuptools. Fixed whitespace.

**v0.1.1** (2009-03-15)
    * Fixed wrong upload path of a contributed, generic block
  
**v0.1** (2009-03-13)
    * Initial release