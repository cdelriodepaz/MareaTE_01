from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from .models import Parish, Publication


class PublicationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }


admin.site.register(Parish)
admin.site.register(Publication, PublicationAdmin)
