from django.urls import path
from . import views
from store.controller import cart,wishlist,checkout

app_name = "store"

urlpatterns = [
    path('',views.home, name="home"),
    path('collections/',views.Collections, name="collections"),
    path('collections/<str:slug>',views.Collectionsview, name="collectionsview"),
    path('collections/<str:cat_slug>/<str:prod_slug>',views.Productview, name="productview"),
    # Cart
    path('add-to-cart',cart.Addtocart, name="addtocart"),
    path('cart',cart.CartView, name="cartview"),
    path('update-cart',cart.Updatecart, name="updatecart"),
    path('delete-cart-item',cart.Deletecart, name="delete-cart-item"),
    # Wishlist
    path('wishlist',wishlist.index, name="wishlist"),
    path('add-to-wishlist',wishlist.Addtowishlist, name="addtowishlist"),
    path('delete-wishlist-item',wishlist.Deletewishlist, name="delete-wishlist-item"),
    # Checkout
    path('checkout',checkout.index, name="checkout"),
    path('placeorder',checkout.placeorder, name="placeorder"),
]