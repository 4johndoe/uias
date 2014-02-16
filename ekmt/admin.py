from django.contrib import admin
from ekmt.models import LicenseBook, Firm

class LicBookInline(admin.StackedInline):
    model = LicenseBook

class FirmAdmin(admin.ModelAdmin):
    list_display = ('name', 'edrpo')

    search_fields = ['name', 'edrpo', 'number']

    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['edrpo']}),
    ]

    inlines = [LicBookInline]

admin.site.register(Firm, FirmAdmin)