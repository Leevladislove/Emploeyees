from django.shortcuts import render, redirect

from visits.models import Visit
from .forms import EmployeeForm
from .models import Employee


def add_new(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect(f'/detail/{instance.id}')

    else:
        form = EmployeeForm()
    return render(request, 'blog/index.html', {'form': form})


def index(request):
    employees = Employee.objects.all()
    return render(request, 'blog/show.html', context={'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'blog/edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, request.FILES, instance=employee)
    if form.is_valid():
        form.save()
        return redirect(f'/detail/{id}')
    return redirect(f'/detail/{id}')


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')


def detail(request, id):
    employee = Employee.objects.get(id=id)
    visits = Visit.objects.filter(employee__id=id)
    return render(request, 'blog/detail.html', {'employee': employee,  'visits': visits})

