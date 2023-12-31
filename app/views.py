from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest


# Create your views here.
def hey_you(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse(f"Hey, {name}!")


def how_old(request: HttpRequest, birthyear: int, end: int) -> HttpResponse:
    age = end - birthyear
    return HttpResponse(age)


def order(request: HttpRequest, burgers: int, fries: int, drinks: int) -> HttpResponse:
    bur = burgers * 4.5
    fri = fries * 1.5
    dri = drinks * 1
    total = fri + bur + dri
    return HttpResponse(f"{total}")
