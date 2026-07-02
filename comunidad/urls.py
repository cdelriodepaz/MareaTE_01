from django.urls import path
from . import views

app_name = "comunidad"
urlpatterns = [
    path("<slug:slug>/", views.pagina_comunidad, name="pagina_comunidad"),
]
