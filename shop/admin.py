from django.contrib import admin
from .models import Category, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description','category', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock','available']
    list_per_page = 30

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)