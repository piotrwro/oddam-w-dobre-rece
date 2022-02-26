from django.contrib import admin

# Register your models here.
from home.models import Category, Institution

admin.site.register(Category)
admin.site.register(Institution)
