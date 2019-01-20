from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

from ownit.secret import EMAIL_USER


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
    try:
        dep = float(request.GET["deposito"])
        ing = float(request.GET["ingresos"])
        city = request.GET["ciudad"]
        value_home = dep + (ing * 8)  # * config.d_city[city]
        value_bank = 4.5 * ing + dep
        cntx["missing"] = False
        cntx["value_home"] = int(value_home)
        cntx["value_bank"] = int(value_bank)
        cntx["dep"] = int(dep)

        perc = dep / value_home
        cntx["perc_insuficient"] = perc < 0.05
        cntx["dep_suf"] = int(0.05 * value_home)

        cntx["percentage"] = round(float(perc * 100), 2)
    except:
        cntx["missing"] = True
        value_home = 0
        value_bank = 0
        dep = 0

    return render(request, 'pages/search.html', context=cntx)


def contact(request):
    if request.method == "POST":

        try:
            name = request.POST["name"]
            email = request.POST["email"]
            phone = request.POST["phone"]
            message = request.POST["message"]

            send_mail(
                "Ownit more info request",
                "The user with name {name} with email {email}, phone number {phone} is interested and sent the following message:\n{message}".format(
                    name=name, email=email, phone=phone, message=message),
                EMAIL_USER,
                (EMAIL_USER,),
                fail_silently=True
            )

            messages.success(request, "Tu solicitud ha estado enviada correctamente!")
        except:
            # messages.error(request, "Ha habido algun error con tu solicitud, vuelve a probar en otro momento!")
            messages.error(request, "Ha habido algun error con tu solicitud, vuelve a probar en otro momento!")

    else:

        messages.error(request, "Ha habido algun error con tu solicitud, vuelve a probar en otro momento!")

    return redirect("invest")
