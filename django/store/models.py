from django.db import models
import datetime
import os
from accounts.models import UserTable

# Create your models here.
def get_file_path(request, filename):
    original = filename
    current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = "%s_%s" % (current_time, original)
    return os.path.join('uploads/', file_name)

class Category(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    status=models.BooleanField(default=False,help_text="0-default , 1-Hide")
    trending=models.BooleanField(default=False,help_text="0-default , 1-Hide")
    meta_title=models.CharField(max_length=150,null=False,blank=False)
    meta_keywords=models.CharField(max_length=150,null=False,blank=False)
    meta_description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    small_description=models.TextField(max_length=250,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-default , 1-Hide")
    trending=models.BooleanField(default=False,help_text="0-default , 1-Hide")
    tag=models.CharField(max_length=150,null=False,blank=False)
    meta_title=models.CharField(max_length=150,null=False,blank=False)
    meta_keywords=models.CharField(max_length=150,null=False,blank=False)
    meta_description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Cart(models.Model):
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    

class Order(models.Model):
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=150,null=False,blank=False)
    last_name=models.CharField(max_length=150,null=False,blank=False)
    email = models.EmailField(max_length=150,null=False, blank=False)
    phone=models.CharField(max_length=150,null=False,blank=False)
    address=models.TextField(max_length=500,null=False,blank=False)
    city=models.CharField(max_length=150,null=False,blank=False)
    state=models.CharField(max_length=150,null=False,blank=False)
    country=models.CharField(max_length=150,null=False,blank=False)
    pincode=models.CharField(max_length=150,null=False,blank=False)
    total_price=models.FloatField(null=False,blank=False)
    payment_mode=models.CharField(max_length=150,null=False,blank=False)
    payment_id = models.CharField(max_length=250,null=True,blank=True)
    order_status=(
                  ('pending','Pending'),
                  ('out_for_shipping','Out For Shipping'),
                  ('completed','Completed'),
                  )
    status=models.CharField(max_length=250,choices=order_status,default='pending')
    message=models.TextField(null=True)
    tracking_no=models.CharField(max_length=250,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} - {}'.format(self.id,self.tracking_no)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price=models.FloatField(null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    
    def __str__(self):
        return '{} - {}'.format(self.order.id,self.order.tracking_no)
class BillingAddress(models.Model):
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50,null=False)
    address=models.TextField(max_length=500,null=False,blank=False)
    city=models.CharField(max_length=150,null=False,blank=False)
    state=models.CharField(max_length=150,null=False,blank=False)
    country=models.CharField(max_length=150,null=False,blank=False)
    pincode=models.CharField(max_length=150,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.user.username