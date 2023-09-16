from django.urls import path
from . import views
from accounts.authentication import authview
app_name = "accounts"

urlpatterns = [
    path('register/',authview.registerview, name="registerview"),
    path('login/',authview.loginview, name="loginview"),
    path('logout/',authview.logoutview, name="logoutview"),
]