from django.contrib import admin
from .models import Menu, Items
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"name": ("title",)}

class ItemsAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Menu, MenuAdmin)


admin.site.register(Items, ItemsAdmin, 
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),)

