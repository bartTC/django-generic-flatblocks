from django.db import models
from django.contrib import admin

from django.utils.translation import ugettext_lazy as _

class Title(models.Model):
    title = models.CharField(_('Title'), max_length=40, blank=True)
    
    def __unicode__(self):
        return "(TitleBlock) %s" % self.title
    
class Image(models.Model):
    image = models.ImageField(_('Image'), upload_to='images/blocks/', blank=True)

    def __unicode__(self):
        return "(ImageBlock) %s" % self.title
        
class TitleAndText(models.Model):
    title = models.CharField(_('Title'), max_length=40, blank=True)
    text = models.TextField(_('Text'), blank=True)

    def __unicode__(self):
        return "(TitleAndTextBlock) %s" % self.title

admin.site.register(Title)
admin.site.register(Image)
admin.site.register(TitleAndText)