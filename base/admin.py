# restaurant/admin.py
from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_price', 'adjusted_price')  # Display these fields in the admin list view
    search_fields = ('name',)  # Enable search by name
    list_filter = ('base_price',)  # Filter by base price

# Register the model with the custom admin class
admin.site.register(MenuItem, MenuItemAdmin)

from django.contrib import admin
from .models import DosaWorldMenu

@admin.register(DosaWorldMenu)
class DosaWorldMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_price')
