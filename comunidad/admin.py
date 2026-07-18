from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from .models import Parish, Publication


class PublicationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(parish=request.user.parish)


class ParishAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(id=request.user.parish.id)


admin.site.register(Parish, ParishAdmin)
admin.site.register(Publication, PublicationAdmin)
