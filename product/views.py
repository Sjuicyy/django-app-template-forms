from multiprocessing import context
from tkinter import NONE
from django.shortcuts import render
from product.models import Products

# Create your views here.
from .forms import ProductsForm

def product_create_view(request):
    my_title = request.POST.get('title')
    my_price = request.POST.get('price')
    my_description = request.POST.get('description')
    print(my_title)
    print(my_price)
    print(my_description)
    
    context ={}
    return render (request, "products/product.html", context)