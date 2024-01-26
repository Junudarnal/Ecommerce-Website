from django.shortcuts import render
from products.models import Products
from django.views import View
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import redirect
# from .constant import PRODUCTCATEGORY
# Create your views here.
def jacketswet(request):
    template_name ='products/jacketswet.html'
    jack_swets = Products.objects.filter(category="JACKET_AND_SWEATER", status = "PUBLISH" )
    context = { 'jackswets': jack_swets}
    return render(request,template_name,context)

def pant(request):
    template_name ='products/pants.html'
    pants = Products.objects.filter(category="PANTS", status = "PUBLISH" )
    context = { 'pants': pants}
    return render(request,template_name,context)

def top(request):
    template_name ='products/tops.html'
    tops = Products.objects.filter(category="TOPS", status = "PUBLISH" )
    context = { 'tops': tops}
    return render(request,template_name,context)

def tshirt(request):
    template_name ='products/tshirt.html'
    tshirt = Products.objects.filter(category="T-SHIRT", status = "PUBLISH" )
    context = { 'tshirts': tshirt}
    return render(request,template_name,context)

def ProductDetail(request, uuid):
    try:
        product = Products.objects.get(uuid=uuid)
    except Products.DoesNotExist:
        return HttpResponse("Invalid uuid passed")
    return render(request, "products/productdetails.html", {"ProductDetail": product})

def search(request):
    if request.method == "POST":
        search = request.POST.get('searchproduct')
        if not search:
            return redirect('/')
        data = Products.objects.filter(Q(name__icontains=search) |Q(category__icontains=search) )
        return render(request ,'home/search.html', {"data":data, "search" : search})
    return redirect('/')

# def  product(request):
#     product = Products.objects.filter(status = 'Publish')
#     pass

#     context = {
#         'product': product,
#         'categories': categories
#     }

#     return render(request, 'home/base.html', context)