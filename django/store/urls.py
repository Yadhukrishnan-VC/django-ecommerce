from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('',views.home, name="home"),
    path('collections/',views.Collections, name="collections"),
    path('collections/<str:slug>',views.Collectionsview, name="collectionsview"),
    path('collections/<str:cat_slug>/<str:prod_slug>',views.Productview, name="productview"),
]