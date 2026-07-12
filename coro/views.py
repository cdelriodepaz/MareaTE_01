from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from comunidad.models import Parish
from .models import Project

# Create your views here.


@login_required
def choir_mainPage(request, slug):
    parish = get_object_or_404(Parish, slug=slug)
    projects = Project.objects.filter(parish=parish)
    return render(
        request, "coro/choir_mainPage.html", {"parish": parish, "projects": projects}
    )


@login_required
def choir_projectPage(request, slug, project_id):
    parish = get_object_or_404(Parish, slug=slug)
    project = get_object_or_404(Project, id=project_id)
    return render(
        request, "coro/song_page.html", {"parish": parish, "project": project}
    )
