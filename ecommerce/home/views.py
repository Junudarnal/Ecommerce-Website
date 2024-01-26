from django.shortcuts import render, redirect
from products.models import Products

# Create your views here.
def display(request):
    template_name ='home/homepage.html'
    context = { 'name': 'home'}
    if not request.user.is_superuser:
        return render(request,template_name,context)
    else:
        return redirect('/user/login/')

def contact(request):
    pass

def product(request):
    pass

