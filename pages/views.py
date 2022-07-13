from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request, "home.html",{})

def about_view(request,*args,**kwargs):
    my_context = {
        "my_name":"my name is sammy",
        "my_age":55,
        "my_list": [123,456,789,135,579],
    }
    return render(request, "about.html",my_context)


def contact_view(request,*args,**kwargs):
    return render(request, "contact.html",{})

def address_view(request,*args,**kwargs):
    return render(request, "address.html",{})