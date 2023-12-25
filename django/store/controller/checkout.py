from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from store.models import Product,Cart,Order,OrderItem,BillingAddress
from accounts.forms import UserForm
from accounts.models import UserTable

import random

@login_required(login_url='accounts:loginview')
def index(request):
    raw_cart = Cart.objects.filter(user=request.user)
    for item in raw_cart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)
    cart_items = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cart_items:
        total_price = total_price + item.product.selling_price * item.product_qty
        
    userprofile = BillingAddress.objects.filter(user=request.user).first()
    
    context = {'cart_items':cart_items,'total_price':total_price , 'userprofile':userprofile}
    return render(request,'store/checkout.html',context) 

@login_required(login_url='accounts:loginview')
def placeorder(request):
    if request.method == 'POST':
        
        currentuser = UserTable.objects.filter(pk=request.user.pk).first()
        if not currentuser.first_name and currentuser.last_name:
            currentuser.first_name = request.POST.get('first_name')
            currentuser.last_name = request.POST.get('last_name')
            currentuser.save()
        
        if not BillingAddress.objects.filter(user=request.user):
            userprofile = BillingAddress()
            userprofile.user = request.user
            userprofile.phone = request.POST.get('phone')
            userprofile.address = request.POST.get('address')
            userprofile.city = request.POST.get('city')
            userprofile.state = request.POST.get('state')
            userprofile.country = request.POST.get('country')
            userprofile.pincode = request.POST.get('pin_code')
            userprofile.save()
        
        neworder = Order()
        neworder.user = request.user
        neworder.first_name = request.POST.get('first_name')
        neworder.last_name = request.POST.get('last_name')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.address = request.POST.get('address')
        neworder.city = request.POST.get('city')
        neworder.state = request.POST.get('state')
        neworder.country = request.POST.get('country')
        neworder.pincode = request.POST.get('pin_code')
        neworder.payment_mode = request.POST.get('payment_mode')
        
        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.selling_price * item.product_qty
        
        neworder.total_price = cart_total_price
        
        trackno = 'track'+str(random.randint(1111111,9999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = 'track'+str(random.randint(1111111,9999999))
        neworder.tracking_no = trackno
        neworder.save()
        
        neworderitems = Cart.objects.filter(user = request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order = neworder,
                product = item.product,
                price = item.product.selling_price,
                quantity = item.product_qty 
            )
            
            # To reduce from available stock
            
            orderproduct = Product.objects.filter(id=item.product.id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()
        
        # Clear Cart
        
        Cart.objects.filter(user=request.user).delete()
        messages.success(request,"Your Order has been Placed Successfully")
                    
    return redirect('/')