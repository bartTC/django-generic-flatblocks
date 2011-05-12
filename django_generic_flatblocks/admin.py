# -*- conding: utf-8 -*-
from django.db.models import loading
from django.contrib import admin
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django_generic_flatblocks.models import GenericFlatblock
from django_generic_flatblocks import settings as generic_flatblock_settings


class GenericFlatblockAdmin(admin.ModelAdmin):

    list_display = (
        'related_object_changelink',
        'slug'
    )
    fields = ('slug',)

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

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = {'models': []}
        for item in generic_flatblock_settings.FLATBLOCK_MODELS:
            app_label, model_name = item.split('.')
            model_cls = loading.cache.get_model(app_label, model_name)
            extra_context['models'].append({
                'name': model_name,
                'options': model_cls._meta,
                'add_url': reverse('admin:%s_%s_add' % (app_label.lower(), model_name.lower()))
            })

        print 'extra_context:', extra_context
        self.change_form_template = 'admin/django_generic_flatblocks/add_form.html'
        return super(GenericFlatblockAdmin, self).add_view(request, form_url,
            extra_context=extra_context)

admin.site.register(GenericFlatblock, GenericFlatblockAdmin)
