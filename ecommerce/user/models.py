from django.db import models
from django.contrib.auth.models import User
from products.models import Products
from products.constant import ORDER_STATUS, METHOD


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    product = models.ForeignKey (Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(null = False, blank = False)
    created_at = models.DateTimeField(auto_now_add=True)
    added_to_order = models.BooleanField(default=False)



class Order(models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE, null = True , blank = True)
    cart = models.ManyToManyField(Cart, null = True , blank = True)
    first_name = models.CharField(max_length = 200, default= "Abc")
    last_name = models.CharField(max_length = 200 , default= "Abc")
    shipping_address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=10)
    zip = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField(null = True, blank = True)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null = True , blank=True)
    subtotal = models.PositiveIntegerField(null=True,  default= 0)
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices= ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length = 20, choices= METHOD, default = "CASH ON DELIVERY" )
    payment_completed = models.BooleanField(default = False , null = True, blank = True)

    def __str__(self):
        return "Order : " + str(self.id)

    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics', default='media/img/profileicon.jpg')
    contact = models.PositiveBigIntegerField(max_length= 10)
    





    