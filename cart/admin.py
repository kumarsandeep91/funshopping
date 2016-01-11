from django.contrib import admin
from .models import CartItem
# Register your models here.
class CartAdmin(admin.ModelAdmin):
	search_fields = ['product']
	list_display = ('product', 'quantity')
admin.site.register(CartItem, CartAdmin)