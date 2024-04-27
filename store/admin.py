from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


from .models import *
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'get_image', 'rating', 'price', 'category')
    list_display_links=('title', 'get_image', 'rating')
    list_filter=('title', 'rating')
    prepopulated_fields={'slug': ('title',)}

    @admin.display
    def get_image(self, item=Item):
        if item.image:
            return mark_safe(f'<img src="{item.image.url}" width="50%" />')
        return None

admin.site.register(Item, ItemAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'slug')
    list_display_links=('id', 'name', 'slug')
    prepopulated_fields={'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class TagsAdmin(admin.ModelAdmin):
    list_display=('id', 'tag', 'slug')
    list_display_links=('id', 'tag', 'slug')
    prepopulated_fields={'slug': ('tag',)}

admin.site.register(Tags, TagsAdmin)
