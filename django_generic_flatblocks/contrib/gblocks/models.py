from django.db import models
from django.utils.translation import ugettext_lazy as _

class Title(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)

    def __unicode__(self):
        return "(TitleBlock) %s" % self.title

class Text(models.Model):
    text = models.TextField(_('text'), blank=True)

    def __unicode__(self):
        return "(TextBlock) %s..." % self.text[:20]

class Image(models.Model):
    image = models.ImageField(_('image'), upload_to='gblocks/', blank=True)

    def __unicode__(self):
        return "(ImageBlock) %s" % self.image

class TitleAndText(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    text = models.TextField(_('text'), blank=True)

    def __unicode__(self):
        return "(TitleAndTextBlock) %s" % self.title

class TitleTextAndImage(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    text = models.TextField(_('text'), blank=True)
    image = models.ImageField(_('image'), upload_to='gblocks/', blank=True)

    def __unicode__(self):
        return "(TitleTextAndImageBlock) %s" % self.title
