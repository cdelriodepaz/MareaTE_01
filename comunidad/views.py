from django.shortcuts import render, get_object_or_404
from .models import Parish


# Create your views here.
def pagina_comunidad(request, slug):
    parish = get_object_or_404(Parish, slug=slug)
    return render(request, "comunidad/pagina_comunidad.html", {"parish": parish})
