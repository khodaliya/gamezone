# from _typeshed import Self
from django.core import paginator
from django.http import request
from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from .models import CATAGORY_CHOICE,Contact, Product
from django.views import View
from django.contrib import messages
from math import ceil
from django.core.paginator import Paginator
# Create your views here.


# front page
# def home(request):
#     params = {'blog_name': 'Game Zone'}
#     return render(request, 'index.html', params)

class productview(View):
    def get(Self, request):
        gaming_computers = Product.objects.filter(catagory='GC').order_by('-id')[:10]
        gaming_laptops = Product.objects.filter(catagory='GL').order_by('-id')[:10]
        gaming_mobiles = Product.objects.filter(catagory='GM').order_by('-id')[:10]
        gaming_cpu = Product.objects.filter(catagory='CPU').order_by('-id')[:10]
        gaming_moniter = Product.objects.filter(catagory='GMT').order_by('-id')[:10]
        gaming_headphone = Product.objects.filter(catagory='GH').order_by('-id')[:10]
        keybord_mouse = Product.objects.filter(catagory='KM').order_by('-id')[:10]

        products = {'gaming_computers': gaming_computers, 'gaming_laptops': gaming_laptops,
                                             'gaming_mobiles': gaming_mobiles, 'gaming_moniter': gaming_moniter, 'keybord_mouse': keybord_mouse, 
                                             'gaming_cpu': gaming_cpu,'gaming_headphone':gaming_headphone}
        return render(request, 'home.html', products)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Yor Message has been Send')
    params = {'blog_name': 'Game Zone'}
    return render(request, 'contact.html', params)


# gaming devices page

def gaming_computer(request):
    computers = Product.objects.filter(catagory='GC').order_by('-id')
    paginator = Paginator(computers,5)
    page_number = request.GET.get('page')
    computerfinal = paginator.get_page(page_number)
    totalpage = computerfinal.paginator.num_pages
    data = {
        'computers':computerfinal,
        'totalpagelist':[n+1 for n in range(totalpage)]
    }
    return render(request, 'gaming_computer.html',data)


def gaming_laptops(request):
    laptops = Product.objects.filter(catagory='GL').order_by('-id')
    paginator = Paginator(laptops,5)
    page_number = request.GET.get('page')
    laptopsfinal = paginator.get_page(page_number)
    totalpage = laptopsfinal.paginator.num_pages
    data = {
        'laptops':laptopsfinal,
        'totalpagelist':[n+1 for n in range(totalpage)]
    }
    return render(request, 'gaming_laptops.html',data)


def gaming_mobiles(request):
    mobiles = Product.objects.filter(catagory='GM').order_by('-id')
    paginator = Paginator(mobiles,5)
    page_number = request.GET.get('page')
    mobilesfinal = paginator.get_page(page_number)
    totalpage = mobilesfinal.paginator.num_pages
    data = {
        'mobiles':mobilesfinal,
        'totalpagelist':[n+1 for n in range(totalpage)]
    }
    return render(request, 'gaming_mobiles.html',data)


def gaming_moniter(request):
    moniters = Product.objects.filter(catagory='GMT').order_by('-id')
    paginator = Paginator(moniters,5)
    page_number = request.GET.get('page')
    monitersfinal = paginator.get_page(page_number)
    totalpage = monitersfinal.paginator.num_pages
    data = {
        'moniters':monitersfinal,
        'totalpagelist':[n+1 for n in range(totalpage)]
    }
    return render(request, 'gaming_moniter.html',data)


def gaming_headphone(request):
    headphone = Product.objects.filter(catagory='GH').order_by('-id')
    paginator = Paginator(headphone,5)
    page_number = request.GET.get('page')
    headphonefinal = paginator.get_page(page_number)
    totalpage = headphonefinal.paginator.num_pages
    data = {
        'headphone':headphonefinal,
        'totalpagelist':[n+1 for n in range(totalpage)]
    }
    return render(request, 'gaming_headphone.html',data)

def keybord_mouse(request):
    keybordmouse=Product.objects.filter(catagory='KM').order_by('-id')
    paginator = Paginator(keybordmouse,5)
    page_number = request.GET.get('page')
    keybordmousefinal = paginator.get_page(page_number)
    totalpage = keybordmousefinal.paginator.num_pages
    data = {
        'keybordmouse':keybordmousefinal,
        'totalpagelist':[n+1 for n in range(totalpage)]
    }
    return render(request, 'keybord_mouse.html',data)
# product detail pages
def products(request, slug):
    laptops = Product.objects.filter(slug=slug)
    return render(request, 'product_detail.html', {'laptops': laptops[0]})


# def searchMatch(query, item):
#     if query in item.title or query in item.category:
#         return True
#     else:
#         return False

def search(request):
    # keybord = Product.objects.all()
    query = request.GET.get('search')
    if len(query)!=0:
        keybord = Product.objects.filter(title__icontains=query)   
    else:
        return render(request, 'search.html') 
    return render(request, 'search.html',{'keybord':keybord})  

# def error(request,exception):
#     return render(request, 'error.html')    

def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'error.html', data)
