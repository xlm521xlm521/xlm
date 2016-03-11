from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile
admin.site.register(UserProfile)
# Register your models here.
admin.site.register(Category)
admin.site.register(Page)

class CategoryAdmin(admin.ModelAdmin) :
    prepopulated_fields = {'slug':('name',)}
