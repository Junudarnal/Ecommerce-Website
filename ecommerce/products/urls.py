from django.urls import path
from .import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('jacketswet/', views.jacketswet, name ='jacketswet'),
    path('pants/', views.pant, name ='pants'),
    path('tops/', views.top, name ='tops'),
    path('tshirts/', views.tshirt, name ='tshirts'),
    path('search/', views.search, name ='search'),
    path("productdetail/<str:uuid>/", views.ProductDetail, name= "product_detail"),
]

