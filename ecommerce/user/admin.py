from django.contrib import admin
from .models import Cart, Order, Profile

# Register your models here.
admin.site.register(Cart)
admin.site.register([Order, Profile])

