from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        'name': "hello-world"

    }
    return render(request, 'pages/index.html', context=context)


def buy(request):
    context = {
        'name': "hello-world"

    }
    return render(request, 'pages/buy.html', context=context)


def invest(request):
    context = {
        'name': "hello-world"

    }
    return render(request, 'pages/invest.html', context=context)
