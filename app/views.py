from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.
def hey_you(request,name: HttpRequest)->HttpResponse:
    return HttpResponse(f"Hey, {name}")

def how_old(request,birthyear,end: HttpRequest)->HttpResponse:
    age = end - birthyear
    return HttpResponse(age)

def order(request,burgers,fries,drinks: HttpRequest)->HttpResponse:
    bur = burgers * 4.5
    fri = fries * 1.5 
    dri = drinks * 1
    total = fri + bur + dri 
    return HttpResponse(f"{total:.2f}")