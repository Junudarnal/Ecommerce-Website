from django.urls import path
from .import views

urlpatterns = [
    path('signup/', views.signup, name ='signup'),
    path('login/', views.sign_in, name ='login'),
    path('signout/', views.signout, name ='logout'),
    path('wishlist/', views.wishlist, name ='wishlist'),
    path('cart/', views.viewcart, name ='cart'),
    path('profile/', views.profile, name ='profile'),
     path('updateprofile/', views.updateprofile, name ='update_profile'),
     path('password/', views.updatepassword, name ='updatepassword'),
    #  path('userdash/', views.userdash, name ='userdash'),
    path('orderhistory/', views.user_order_history, name ='orderhistory'),
    path('addtocart/<str:uuid>/<str:view>/', views.addToCart, name ='add_to_cart'),
    path('removeitem/<str:uuid>/', views.removeItem, name ='remove_item'),
    path('backtoprofile/', views.backtoprofile, name ='backtoprofile'),
    path('khaltirequest/<int:id>/', views.KhaltiRequestView, name ='khaltirequest'),
    path('cart-update/', views.updateCart, name ='cart_update'),
    path('deletehistory/<int:id>/', views.remove_orderhistory, name = "delete_orderhistory"),
    # path('cashcheckout/', views.cashCheckout, name ='cashcheckout'),
    path('checkout/', views.checkOut, name ='checkout'),
    path('khalti-verify/', views.KhaltiVerifyView, name ='khaltiverify'),
   
    
    # path('profile/', views.profile, name ='profile'),

]
# 