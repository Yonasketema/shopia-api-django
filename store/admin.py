from django.contrib import admin
from django.utils.html import format_html, urlencode
from . import models


@admin.register(models.Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" />')
        return ''


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'price', 'last_update']
    inlines = [ProductImageInline]

    class Media:
        css = {
            'all': ['style.css']
        }


@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass
