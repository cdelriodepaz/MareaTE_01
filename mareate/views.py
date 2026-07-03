from django.shortcuts import render
from comunidad.models import Parish


# Create your views here.
def pagina_principal(request):
    parishes = Parish.objects.filter(active=True)
    return render(request, "pagina_principal.html", {"parishes": parishes})
