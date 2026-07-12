from django.urls import path
from . import views

app_name = "comunidad"
urlpatterns = [
    path("<slug:slug>/", views.pagina_comunidad, name="pagina_comunidad"),
    path(
        "<slug:slug>/avisos/", views.community_publications, name="pagina_publicaciones"
    ),
    path(
        "<slug:slug>/avisos/<int:publication_id>/",
        views.community_publication_closeup,
        name="pagina_publicacion",
    ),
]
