from django.contrib import admin
from . models import Category,Product,Cart,OrderItem,BillingAddress
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(BillingAddress)