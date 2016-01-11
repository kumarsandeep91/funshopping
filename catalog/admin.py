from django.contrib import admin

# Register your models here.
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	search_fields = ['name']
	list_display = ('name', 'brand', 'price')

# no need of this line
#admin.site.register(Product, ProductAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	search_fields = ['name']
#admin.site.register(Category, CategoryAdmin)