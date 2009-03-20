from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django_generic_flatblocks.models import GenericFlatblock

class GenericFlatblockAdmin(admin.ModelAdmin):

    list_display = (
        'related_object_changelink',
        'slug'
    )

    list_display_links = ('slug',)

    def related_object_changelink(self, obj):
        return '<a href="%s">%s - %s</a>' % (
            self.generate_related_object_admin_link(obj.content_object),
            obj.slug,
            obj.content_object.__unicode__(),
        )
    related_object_changelink.allow_tags = True
    related_object_changelink.short_description = _('change related object')

    def generate_related_object_admin_link(self, related_object):
        return '../../%s/%s/%s/' % (
            related_object._meta.app_label,
            related_object._meta.module_name,
            related_object.pk
        )

    def change_view(self, request, object_id, extra_context=None):
        """
        Haven't figured out how to edit the related object as an inline.
        This template adds a link to the change view of the related
        object..
        """
        related_object = self.model.objects.get(pk=object_id).content_object
        c = {
            'admin_url': self.generate_related_object_admin_link(related_object),
            'related_object': related_object,
            'related_app_label': related_object._meta.app_label,
            'related_module_name': related_object._meta.module_name,
        }
        c.update(extra_context or {})
        self.change_form_template = 'admin/django_generic_flatblocks/change_form_forward.html'
        return super(GenericFlatblockAdmin, self).change_view(request, object_id, extra_context=c)

admin.site.register(GenericFlatblock, GenericFlatblockAdmin)
