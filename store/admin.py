from django.contrib import admin
from . import models


@admin.register(models.Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'price', 'last_update']
