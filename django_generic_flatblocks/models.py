from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import loading
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify


class GenericFlatblock(models.Model):
    slug = models.SlugField(_('slug'), max_length=255, unique=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __init__(self, *args, **kwds):
        ret = super(GenericFlatblock, self).__init__(*args, **kwds)
        if self.slug is None:
            self.slug = self._generate_slug()
        return ret

    def _generate_slug(self):
        return slugify((self.content_type.model, self.content_object.id))

    def __unicode__(self):
        return self.slug
