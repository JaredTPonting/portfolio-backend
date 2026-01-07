from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from django.contrib import admin
from .models import Project, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "image_preview")

    def image_preview(self, obj):
        if obj.image_url:
            return format_html(
                '<img src="{}" style="height: 60px;" />',
                obj.image_url
            )
        return "—"
