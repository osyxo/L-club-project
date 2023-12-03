from django.shortcuts import render

from home.models import Gnev

def home_view(request):
    context = {
        "site_name": "Gnev",
        "gnevs": Gnev.objects.all()
    }
    return render(request, "home/home.html", context)