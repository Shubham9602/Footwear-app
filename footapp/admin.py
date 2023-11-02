from django.contrib import admin
from footapp.models import Products
from footapp.models import Contact

# Register your models here.

#admin.site.register(Products)

class ProductsAdmin(admin.ModelAdmin):
    list_display=['id','name','cat','price','pdetail','is_active','pimage']
    list_filter=['cat','is_active']
admin.site.register(Products,ProductsAdmin)