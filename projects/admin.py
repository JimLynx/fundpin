from django.contrib import admin
from .models import Project, Category, Country


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'country',
        'pin_id',
        'name',
        'category',
        'location',
        'image',
        'is_featured',
    )
    list_editable = ['is_featured']
    ordering = ('country',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Country, CountryAdmin)
