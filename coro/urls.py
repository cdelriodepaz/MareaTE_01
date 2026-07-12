from django.urls import path
from . import views

app_name = "coro"

urlpatterns = [
    path("", views.choir_mainPage, name="choir_mainPage"),
    path("<int:project_id>/", views.choir_projectPage, name="project_page"),
]
