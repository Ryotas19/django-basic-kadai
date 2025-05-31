from django.contrib import admin
from .models import Product, Category
from django.utils.safestring import mark_safe

class productAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image')
    search_fields = ('name',)
    list_filter = ('category',)
    
    def image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" style="width:100px; height:auto;">')
        return '(No Image)'
    image.short_description = '画像'

    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Product, productAdmin)
admin.site.register(Category, CategoryAdmin)