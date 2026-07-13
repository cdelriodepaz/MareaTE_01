from django.shortcuts import render, get_object_or_404
from .models import Parish, Publication


# Create your views here.
def pagina_comunidad(request, slug):
    parish = get_object_or_404(Parish, slug=slug)
    return render(request, "comunidad/pagina_comunidad.html", {"parish": parish})


def community_publications(request, slug):
    parish = get_object_or_404(Parish, slug=slug)
    publications = Publication.objects.filter(parish=parish, published=True).order_by(
        "-date"
    )
    return render(
        request,
        "comunidad/community_publications.html",
        {"publications": publications, "parish": parish},
    )


def community_publication_closeup(request, slug, publication_id):

    parish = get_object_or_404(Parish, slug=slug)
    publication = get_object_or_404(Publication, id=publication_id)
    return render(
        request,
        "comunidad/community_publications_closeup.html",
        {"publication": publication, "parish": parish},
    )
