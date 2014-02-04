from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_generic_flatblocks.contrib.gblocks import settings as blocks_settings


class Title(models.Model):

    class Meta:
        verbose_name = _('Title')
        verbose_name_plural = _('Titles')

    title = models.CharField(_('title'), max_length=255, blank=True)

    def __unicode__(self):
        return "(TitleBlock) %s" % self.title

class Text(models.Model):

    class Meta:
        verbose_name = _('Text')
        verbose_name_plural = _('Texts')

    text = models.TextField(_('text'), blank=True)

    def __unicode__(self):
        return "(TextBlock) %s..." % self.text[:20]

class Image(models.Model):

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    image = models.ImageField(_('image'),
        upload_to=blocks_settings.UPLOAD_PATH + 'gblocks/', blank=True)

    def __unicode__(self):
        return "(ImageBlock) %s" % self.image

class TitleAndText(models.Model):

    class Meta:
        verbose_name = _('Title and text block')
        verbose_name_plural = _('Title and text blocks')

    title = models.CharField(_('title'), max_length=255, blank=True)
    text = models.TextField(_('text'), blank=True)

    def __unicode__(self):
        return "(TitleAndTextBlock) %s" % self.title

class TitleTextAndImage(models.Model):

    class Meta:
        verbose_name = _('Titled image')
        verbose_name_plural = _('Titled images')

    title = models.CharField(_('title'), max_length=255, blank=True)
    text = models.TextField(_('text'), blank=True)
    image = models.ImageField(_('image'),
        upload_to=blocks_settings.UPLOAD_PATH + 'gblocks/', blank=True)

    def __unicode__(self):
        return "(TitleTextAndImageBlock) %s" % self.title
