from django.urls import path
import pages.views as views


urlpatterns = [

    path("", views.index, name="index"),
    path("buy", views.buy, name="buy"),
    path("invest", views.invest, name="invest"),
]