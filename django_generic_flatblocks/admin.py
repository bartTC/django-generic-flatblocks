from django.contrib import admin
from django.conf import settings
from django_generic_flatblocks.models import GenericFlatblock

class GenericFlatblockAdmin(admin.ModelAdmin):
    def change_view(self, request, object_id, extra_context=None):
        """
        It seems impossible to edit related objects inline. 
        This template forwards the user to the real content object admin site.
        """
        related_object = self.model.objects.get(pk=object_id).content_object
        c = {
            'admin_base_url': getattr(settings, 'ADMIN_BASE_URL', '/admin'),
            'related_app_label': related_object._meta.app_label,
            'related_module_name': related_object._meta.module_name,
            'related_pk': related_object.pk,
            
        }
        c.update(extra_context or {})
        self.change_form_template = 'admin/generic_flatblocks/change_form_forward.html'
        return super(GenericFlatblockAdmin, self).change_view(request, object_id, extra_context=c)
    
admin.site.register(GenericFlatblock, GenericFlatblockAdmin)