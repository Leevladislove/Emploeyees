from django.shortcuts import render
from .models import Visit


def show_visit(request):
    visits = Visit.objects.all()
    return render(request, 'visits/show_visit.html', context={'visits': visits})
