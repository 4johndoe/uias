from django.contrib import admin
from ekmt.models import License, Carriage

class CarriageInline(admin.TabularInline):
    model = Carriage
    extra = 1

class EkmtAdmin(admin.ModelAdmin):
    list_display = ('number', 'firm', 'kod')
    list_filter = ['firm']
    search_fields = ['kod']
    inlines = [CarriageInline]


admin.site.register(License, EkmtAdmin)
