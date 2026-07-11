from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from comunidad.models import Parish

# Create your views here.


@login_required
def choir_mainPage(request, slug):
    parish = get_object_or_404(Parish, slug=slug)
    return render(request, "coro/choir_mainPage.html", {"parish": parish})
