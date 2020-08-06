from django.shortcuts import render

from .models import Flight

# Create your views here.


def index(request):
    return render(request, "flights/index.html", {
        "flight": Flight.objects.all()
    })
