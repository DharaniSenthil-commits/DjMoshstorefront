from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request) :
    #return HttpResponse("Hello Dharani , You Rock !")
    #return render(request,'index.html')
    x=1
    y=2
    return render(request,'index.html',{'name':'Dharani'})

