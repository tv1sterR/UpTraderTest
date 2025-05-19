from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_name', 'parent', 'order', 'url', 'named_url')
    list_filter = ('menu_name', )
    search_fields = ('name', 'menu_name', 'url', 'named_url')
    fields = ('name', 'menu_name', 'parent', 'order', 'url', 'named_url')

admin.site.register(Menu, MenuAdmin)
