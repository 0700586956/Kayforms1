from django.urls import path
from . import views

app_name="main"

urlpatterns = [
    path("", views.mainpage, name="mainpage"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
]

