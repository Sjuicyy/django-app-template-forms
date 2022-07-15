from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def student_view(*args,**kwargs):
    return HttpResponse("<h1>this is a student</h1>")

def student_result(request,*args,**kwargs):
    return render(request, 'student_result.html',{})
    