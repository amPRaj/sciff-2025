from django.contrib import admin
from .models import Movie

admin.site.site_header = "ShowsStoppers Admin"
admin.site.site_title = "ShowsStoppers Admin Portal"
admin.site.index_title = "Welcome to ShowsStoppers Admin"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'rate', 'dur', 'dir', 'create')
    search_fields = ('title', 'dir', 'year')
    list_filter = ('year', 'rate', 'create')
    ordering = ('-create',)
    readonly_fields = ('uuid', 'create')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'desc1', 'year', 'rate', 'dur')
        }),
        ('Production Details', {
            'fields': ('dir', 'screenplay', 'prod')
        }),
        ('Media Files', {
            'fields': ('image', 'file')
        }),
        ('System Fields', {
            'fields': ('uuid', 'create'),
            'classes': ('collapse',)
        }),
    )
