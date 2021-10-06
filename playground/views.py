from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cal(x,y):
    return x*y
def say_hello(request):
    x=10
    y=2
    z = cal(x,y)
    return render(request,'hello.html',{'name': 'Yarin'})