from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(*args,**kwargs):
    return HttpResponse("<h1>this is home view<h1>")


def about_view(*args,**kwargs):
    return HttpResponse("<h1>this is about view<h1>")


def contact_view(*args,**kwargs):
    return HttpResponse("<h1>this is contact view<h1>")

def address_view(*args,**kwargs):
    return HttpResponse("<h1>this is address view<h1>")