from django.urls import path

from . import views

app_name = "kantin"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create/", views.create, name="create"),
    path("item/<str:id>/", views.item, name="item"),
    path("balance", views.balance, name="balance")
]