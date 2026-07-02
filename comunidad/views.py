from django.shortcuts import render, get_object_or_404
from .models import Parroquia


# Create your views here.
def pagina_comunidad(request, slug):
    parroquia = get_object_or_404(Parroquia, slug=slug)
    return render(request, "comunidad/pagina_comunidad.html", {"parroquia": parroquia})
