from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.display, name ='home'),
    path('contact/', views.contact, name ='contact'),
    path('product/', views.product, name ='product'),
    
]