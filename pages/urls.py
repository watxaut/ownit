from django.urls import path
import pages.views as views


urlpatterns = [

    path("", views.index, name="index"),
    path("invest", views.invest, name="invest"),
    path("search", views.search, name="search"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
]