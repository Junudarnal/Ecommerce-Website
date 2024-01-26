from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from user.forms import UserRegisterForm, LoginForm , ProfileForm ,ProfileimageUpdate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from products.models import Products
from .models import Cart, Order, Profile
from django.http import HttpResponseRedirect
from django.db.models import F, Sum
# import requests
# from django.views import View
from django.http.response import JsonResponse
# Create your views here
def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            image = form.cleaned_data.get('profile_pic')
            mobile = form.cleaned_data.get('mobile')
            Profile.objects.create(user=user, image=image, contact=mobile)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'user/signup.html', {'form': form})


def sign_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
        
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user_instance = authenticate(username=username, password = password)

           if user_instance is not None:
            login(request , user_instance)
            return redirect('/')

           else:
            messages.info(request, 'Username or Password is incorrect!!')
            return render(request, 'user/login.html', { 'form' : form})

    else:
        form = LoginForm()

    return render(request, 'user/login.html', { 'form' : form})


def signout(request):
    logout(request)
    return redirect('/')

def wishlist(request):
    pass

@login_required(login_url='/user/login/')
def addToCart(request, uuid, view):
    carts = Cart.objects.filter(user= request.user)
    user = request.user
    quantity = 1
        # print(quantity)
    product = Products.objects.get(uuid=uuid)
    template_to_redirect = view
    if not Cart.objects.filter(user = request.user , product=product, added_to_order=False):
        Cart.objects.create(user = user , product= product, quantity = quantity )
            # print("Here")
        messages.success(request, "Added to cart successfully")
        
        return redirect(f"/products/{template_to_redirect}/")
        # print("Here")
        # return render(request, "products/productdetails.html", {"ProductDetail": product , "cart": carts, "quantity": quantity})
    # return render(request, "products/productdetails.html", {"cart": carts})
    messages.error(request, "Already in cart")
    return redirect(f"/products/{template_to_redirect}/")


def removeItem(request, uuid):
     Cart.objects.all().filter(id=uuid).delete()
     return redirect('/user/cart/')

def remove_orderhistory(request, id):
    print(id)
    Cart.objects.all().filter(id=id).delete()
    return redirect('/user/orderhistory/')


@login_required(login_url='/user/login/')
def viewcart(request):
    user = request.user
    cart = Cart.objects.filter(user= user, added_to_order=False ).select_related('product').annotate(total_price=F('product__price')*F('quantity'))
    amount = 0 
    for p in cart:
        # print(p.quantity, p.product.price)
        value = p.quantity * p.product.price
        amount = amount + value
    totalamount = amount + 100 

    # print(cart[0].quantity)

    return render (request , 'user/cart.html', {"cart": cart , "amount": amount , "totalamount": totalamount})

@login_required(login_url='/user/login/')
def checkOut(request):
    if request.method == 'GET':
        cart_queryset = Cart.objects.filter(user=request.user, added_to_order=False).select_related('product').annotate(total_price=F('product__price')*F('quantity'))
        total_price = cart_queryset.aggregate(all_total=Sum('total_price'))['all_total']+100
        return render (request , "user/checkout.html", {"carts":cart_queryset, "all_total":total_price})
    elif request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            address = request.POST.get('address')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            district= request.POST.get('district')
            quantity = 2
            total = int(request.POST.get('all_total'))
            city = request.POST.get('city')
            payment_method = request.POST.get('payment_method')
            order = Order.objects.create(user=request.user, shipping_address=address, first_name = first_name, last_name = last_name, mobile = mobile , email = email, city = city , payment_method =payment_method , total = total , district =district)
            
            if payment_method == "KHALTI":
                # order.order_status = "ORDER COMPLETED"
                # order.save()
                # messages.success(request, "Your order will be delivered soon!!")
                return redirect( f"/user/khaltirequest/{order.id}/")
            else:
                for cart in Cart.objects.filter(user=request.user, added_to_order=False):
                    order.cart.add(cart)
                    cart.added_to_order=True
                    cart.save()
                order.order_status = "ORDER PENDING"
                order.save()
                messages.success(request, "Your order will be delivered soon!!")
                return redirect("/")
            
            # else:
            #     template = render_to_string('email.html', {'name': first_name})
            #     email = EmailMessage(
            #         'Thanks for purchasing',
            #         template,
            #         settings.EMAIL_HOST_USER,
            #         [email, settings.EMAIL_HOST_USER]
            #     )
            #     email.fail_silently = False
            #     email.send()
            #     items.update(status="Completed")
            #     return redirect('/wishlist/')
            
    return render(request , "user/checkout.html", {"shipping_address" : address, "first_name" : first_name , "last_name" : last_name , "mobile" : mobile , "email" : email, "quantity" :  quantity , "city" : city , "payment_method" : payment_method})

# def cashCheckout(request):
#     return render (request , "user/cashrequest.html")

  
def updateCart(request):
    # print("Here")
    if request.method == "POST":
        quantity = request.POST.get('quantity')
        cart_id = request.POST.get("cart_id")
        # print("Here", quantity, cart_id)
        cart = Cart.objects.get(id=cart_id)
        print(cart)
        cart.quantity = quantity
        cart.save()
        print(cart.quantity)
        return redirect('/user/cart/')

        
@login_required(login_url='/user/login/')
def KhaltiRequestView(request, id, *args, **kwargs):
    order = Order.objects.get(id= id)
    context= {
        "order":order,
        "total":order.total*100
    }
    return render(request, "user/khaltirequest.html", context)  

@login_required(login_url='/user/login/')
def KhaltiVerifyView(request):
    token = request.GET.get("token") 
    amount = request.GET.get("amount")
    o_id = request.GET.get("order_id")
    print(token,amount, o_id)
    #include <stdio.h>

    url = "https://khalti.com/api/v2/payment/verify/"

    payload = {
    'token': token,
    'amount': amount
    }

    headers = {
    'Authorization': 'Key test_secret_key_979c1c36c4b34ec99119bd41894c21d5'
    }
    order_obj = Order.objects.get(id=o_id)

    response = requests.post(url, headers=headers, data=payload)
    resp_dict = response.json()
    print(resp_dict)
    if int(response.status_code) in [200, 201]:
        # print("Till here")
        for cart in Cart.objects.filter(user=request.user, added_to_order=False):
            print(cart)
            order_obj.cart.add(cart)
            cart.added_to_order = True
            cart.save()
        success = True
        order_obj.payment_completed = True
        order_obj.order_status = "ORDER COMPLETED"
        order_obj.save()
    else:
        sucess = False
    
    data = {
        "success": success
    }
    return JsonResponse(data)




@login_required(login_url='/user/login/')
def profile(request):
    template_name ='user/profile.html'
    context = { 'name': 'profile'}
    return render(request,template_name,context)

def updateprofile(request):
    msg = None
    if request.method  == 'POST':
        form =  ProfileForm(request.POST, instance = request.user)
        # p_form = ProfileimageUpdate(request.POST, request.FILES, instance = request.user.Profile.image)
        if form.is_valid():
            form.save()
            
            msg = "Data has been saved"
    form = ProfileForm(instance = request.user)
    # p_form = ProfileimageUpdate(instance = request.user.Profile.image)
    return render(request, 'user/updateprofile.html', { 'form': form,'msg':msg})

def updatepassword(request):
    return render (request , "user/updatepassword.html")

def backtoprofile(request):
    user = request.user
    return redirect( "/user/profile/")

# @login_required(login_url='/user/login/')
# def userdash(request):
#     template_name ='user/userdash.html'
#     context = { 'name': 'userdash'}
#     return render(request,template_name,context)

@login_required(login_url='/user/login/')
def user_order_history(request):
    orders = Cart.objects.filter(user = request.user, added_to_order=True)
    cart_queryset = Cart.objects.filter(user=request.user).select_related('product').annotate(total_price=F('product__price')*F('quantity'))
    if cart_queryset.exists():
        total_price = cart_queryset.aggregate(all_total=Sum('total_price'))['all_total']+100
        context = { 'orders' : orders ,"cart_queryset" : cart_queryset , "total": total_price}
        return render(request, 'user/orderviewhistory.html', context)
    return render(request, "user/orderviewhistory.html")
    # user_product = Order.objects.filter(user=request.user).order_by('created_at')
    # print(user_product)
    # wishlist_items_ids = user_product.values_list('ordered_item', flat=True)
    # wishlist_items_queryset = WishList.objects.filter(id__in=wishlist_items_ids, status='Completed').order_by('-added_date')
    # # order_product = user_product.ordered_item.exclude(status="pending").exclude(status="In Review").exclude(
    # #     status="Canceled").order_by("created_at")
    # print(wishlist_items_queryset)
    # return render(request, 'user_orderHistory.html', {'wishlist_items_queryset': wishlist_items_queryset})

# @login_required()
# def profile(request):
#     return render(request, 'user/profile.html')

# def add_to_wishlist(request):
#     if request.method == 'POST':
#         quantity = int(request.POST.get('hidden-quantity-field'))
#         p_id = request.POST.get('item')
#         try:
#             product_object = Product.objects.get(id=p_id)
#         except ObjectDoesNotExist:
#             messages.error(request, "Product with that id does not exist")
#             return redirect('/')
#         if request.user.id == product_object.user.id:
#             messages.error(request, "You cannot buy this product")
#             return redirect('/')
#         if int(quantity) <= product_object.quantity:
#             if not WishList.objects.filter(user=request.user, wished_item=product_object).exclude(
#                     Q(status="Canceled") | Q(status="Completed") | Q(status="In Review")).exists():
#                 wishlist_instance = WishList.objects.create(user=request.user, wished_item=product_object,
#                                                             status="Pending")
#                 wishlist_instance.price = int(quantity) * wishlist_instance.wished_item.price

#                 wishlist_instance.product_qty = quantity

#                 wishlist_instance.save()
#                 product_object.quantity = product_object.quantity - int(quantity)
#                 product_object.save()
#             else:
#                 try:
#                     wishlist_inst = WishList.objects.get(user=request.user, wished_item=product_object,
#                                                          status="Pending")
#                     old_quantity = wishlist_inst.product_qty
#                     old_price = wishlist_inst.price
#                     wishlist_inst.product_qty += int(quantity)
#                     product_object.quantity -= int(quantity)
#                     wishlist_inst.price = int(quantity) * wishlist_inst.wished_item.price + old_price
#                     product_object.save()
#                     wishlist_inst.save()
#                 except ObjectDoesNotExist:
#                     messages.error(request, "Object does not exist")
#                     return redirect("/wishlist/")

#         else:
#             messages.error(request, "Ordered Quantity cannot be more than Available")
#             return redirect('/')
#     items = WishList.objects.filter(user=request.user, status="Pending")
#     total_price = sum([item.price if (item.status == "Pending") else 0 for item in items])
#     form = OrderForm()
#     return render(request, 'wish_list.html', {'wishlist_queryset': items, 'total_price': total_price, 'form': form})