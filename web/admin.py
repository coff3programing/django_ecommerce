from django.contrib import admin
from .models import Category, Product

# Register your models here.
admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['category', 'name', 'description' , 'price', 'image']
    list_display = ['name', 'category', 'price', 'image', 'register_date']