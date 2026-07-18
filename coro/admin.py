from django.contrib import admin
from . import models


class ProjectAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(parish=request.user.parish)


class ProjectAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(project__parish=request.user.parish)


class VoiceTrackAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(song__project__parish=request.user.parish)


admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Song, ProjectAdmin)
admin.site.register(models.VoiceTrack, VoiceTrackAdmin)
