from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from store.models import Product,Cart,Wishlist
from accounts.forms import UserForm

@login_required(login_url='accounts:loginview')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render(request,'store/wishlist.html',context) 


def Addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if product_check:
                if (Wishlist.objects.filter(user_id=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status':'Product Already in Wishlist'})
                else:
                    Wishlist.objects.create(user=request.user,product_id=prod_id)
                    return JsonResponse({'status':'Product Added to Wishlist'})
                                            
            else:
                return JsonResponse({'status':'No such product found'})
                
        else:
            return JsonResponse({'status':'Login to continue'})
    return redirect('/')

def Deletewishlist(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if request.user.is_authenticated:
            if (Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                Wishlistitem = Wishlist.objects.get(product_id=prod_id,user=request.user)
                Wishlistitem.delete()
                return JsonResponse({'status':'Product Removed from Wishlist'})
            else:
                return JsonResponse({'status':'Product not found in Wishlist'})
        else:
            return JsonResponse({'status':'Login to continue'})
    return redirect('/')