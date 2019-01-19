from django.shortcuts import render
from django.http import HttpResponse

from . import config


# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'pages/index.html', context=context)


def invest(request):
    context = {

    }
    return render(request, 'pages/invest.html', context=context)


def login(request):
    context = {

    }
    return render(request, 'pages/login.html', context=context)


def register(request):
    context = {

    }
    return render(request, 'pages/register.html', context=context)


def search(request):
    cntx = {}

    if request.GET["ingresos"] and request.GET["deposito"] and request.GET["ciudad"]:
        dep = float(request.GET["deposito"])
        ing = float(request.GET["ingresos"])
        city = request.GET["ciudad"]
        value_home = dep + (ing * 8)  # * config.d_city[city]
        cntx["missing"] = False
    else:
        cntx["missing"] = True
        value_home = 0

    cntx["value_home"] = int(value_home)

    return render(request, 'pages/search.html', context=cntx)
