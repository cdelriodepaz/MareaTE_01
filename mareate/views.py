from django.shortcuts import render
from comunidad.models import Parroquia


# Create your views here.
def pagina_principal(request):
    parroquias = Parroquia.objects.filter(activa=True)
    return render(request, "pagina_principal.html", {"parroquias": parroquias})
