from django.contrib import admin
from django_generic_flatblocks.contrib.gblocks.models import *

admin.site.register(Title)
admin.site.register(Text)
admin.site.register(Image)
admin.site.register(TitleAndText)
admin.site.register(TitleTextAndImage)
