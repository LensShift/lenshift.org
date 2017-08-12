from django.contrib import admin

from apps.api.models import Infographic, Section


@admin.register(Infographic)
class InfographicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'url',
        'status'
    )


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = (
        'section_position',
        'text',
        'text_position_x',
        'text_position_y',
    )
