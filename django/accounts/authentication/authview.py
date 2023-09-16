from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from accounts.forms import UserForm
# Create your views here.

def registerview(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered Successfully \n Login to continew")
            return redirect('/login')
    context = {'form' : form}
    return render(request,"auth/register.html",context)

def loginview(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already Logged in')
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request=request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,"Loged in successfully")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
            
    return render(request,'auth/login.html')

def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        messages.warning(request,'You are loged out successfully')
    return redirect('/')