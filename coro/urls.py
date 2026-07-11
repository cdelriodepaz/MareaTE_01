from django.urls import path
from . import views

app_name = "coro"

urlpatterns = [
    path("", views.choir_mainPage, name="choir_mainPage"),
]
