from multiprocessing import context
from tkinter import NONE
from django.shortcuts import render
from product.models import Products

# Create your views here.
from .forms import ProductsForm , RawProductForm



def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
      my_form = RawProductForm(request.POST)
      if my_form.is_valid():
          print(my_form.cleaned_data)
          Products.objects.create(**my_form.cleaned_data)
      else:
          print(my_form.error)
      context ={
        "form":my_form 
    }
    return render (request, "products/product.html", context)








# def product_create_view(request):
#     if request.GET:
#         print(request.GET)
        
#     if request.POST:
#         print(request.POST)
        
#     context ={}
#     return render (request, "products/product.html", context)