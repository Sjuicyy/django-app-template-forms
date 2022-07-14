from multiprocessing import context
from tkinter import NONE
from django.shortcuts import render

# Create your views here.
from .forms import ProductsForm

def product_create_view(request):
    context ={
    }
    return render (request, "products/product.html", context)