from django.contrib import admin
from . import models

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('title', 'created_at')
     list_filter = ('created_at',)
     list_editable = ('title',)
     list_display_links = ('created_at',)
    
class ProductAdmin(admin.ModelAdmin):
     list_display = ('title', 'price', 'product_qty', 'category', 'created_at')
     prepopulated_fields = {'slug': ('title',)} 
     list_filter = ('created_at', 'category')
     list_editable = ('title', 'price', 'product_qty', 'category')
     list_display_links = ('created_at',)

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
