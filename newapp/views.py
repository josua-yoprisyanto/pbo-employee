from django.shortcuts import redirect, render
from .models import Employee

def index(request):
    mem = Employee.objects.all()
    return render(request, 'index.html', {'mem': mem})

def add(request):
    return render(request, 'add.html')

def addrec(request):
    firstname = request.POST['first']
    lastname = request.POST['last']
    contact = request.POST['contact']
    position = request.POST['position']
    status = request.POST['status']
    mem = Employee(firstname=firstname, lastname=lastname, contact=contact, position=position, status=status)
    mem.save()
    return redirect("/")

def delete(request, id):
    mem = Employee.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request, id):
    mem = Employee.objects.get(id=id)
    return render(request, 'update.html', {'mem': mem})

def uprec(request, id):
    firstname = request.POST['first']
    lastname = request.POST['last']
    contact = request.POST['contact']
    position = request.POST['position']
    status = request.POST['status']
    mem = Employee.objects.get(id=id)
    mem.firstname = firstname
    mem.lastname = lastname
    mem.contact = contact
    mem.position = position
    mem.status = status
    mem.save()
    return redirect("/")
