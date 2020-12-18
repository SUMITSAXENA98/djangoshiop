from django.contrib import admin
from .models import Product,Category

# Register your models here.


class adminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']

class adminCategory(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Product,adminProduct)

admin.site.register(Category,adminCategory)