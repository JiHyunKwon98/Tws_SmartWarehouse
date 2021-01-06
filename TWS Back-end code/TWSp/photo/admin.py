from django.contrib import admin
from photo.models import Category, Product, Order, Face, Order_Product

class ProductInline(admin.StackedInline):
    model = Product
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (ProductInline,)
    list_display = ('id', 'name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'pname', 'upload_dt')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'oname', 'ocall', 'no')

@admin.register(Order_Product)
class Order_ProductAdmin(admin.ModelAdmin):
    list_display = ('id','order_id', 'order', 'product_id', 'product', 'no')

@admin.register(Face)
class FaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'fname')