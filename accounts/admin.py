from django.contrib import admin
from .models import User_Details
# Register your models here.

@admin.register(User_Details)
class UserDetailAdmin(admin.ModelAdmin):
	search_fields = ['user']
	list_display = ('id', 'user', 'sex', 'address', 'contact')

#admin.site.register(User_Details)
