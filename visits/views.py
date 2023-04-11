from django.shortcuts import render, redirect

from .forms import VisitForm
from .models import Visit


def show_visit(request):
    visits = Visit.objects.all()
    return render(request, 'visits/show_visit.html', context={'visits': visits})


def add_new_visit(request):
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('/visits/')
    else:
        form = VisitForm()
    return render(request, 'visits/index_visit.html', context={'form': form})


def edit_visit(request, id):
    form = VisitForm()
    visits = Visit.objects.get(id=id)
    return render(request, 'visits/edit_visit.html', context={'visits': visits, 'form': form})


def update_visit(request, id):
    visit = Visit.objects.get(id=id)
    form = VisitForm(request.POST, request.FILES, instance=visit)
    if form.is_valid():
        form.save()
        return redirect(f'/visits/detail/{id}')
    return redirect('/visits')


def detail_visit(request, id):
    visits = Visit.objects.get(id=id)
    return render(request, 'visits/detail_visit.html', context={'visits': visits})


def destroy_visit(request, id):
    visits = Visit.objects.get(id=id)
    visits.delete()
    return redirect('/visits')
