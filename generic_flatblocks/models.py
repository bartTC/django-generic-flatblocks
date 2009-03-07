from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.generic import GenericTabularInline
from django.conf import settings
from test.test_socket import Urllib2FileobjectTest
from urlparse import urljoin
import urllib


class GenericFlatblock(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    
    def __unicode__(self):
        return self.slug

class FlatblockTitleAndText(models.Model):
    title = models.CharField(_('Title'), max_length=255, blank=True)
    content = models.TextField(_('Content'), blank=True)
    
    def __unicode__(self):
        return "%s: %s" % (self.pk, self.title)
    
class FlatblockImageWithCaption(models.Model):
    image=models.ImageField(_('Image'), upload_to='images/')
    caption = models.TextField(_('Caption'), blank=True)
    
    def __unicode__(self):
        return "%s" % (self.image)