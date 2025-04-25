import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .models import task

def index(request):
    context = {}
    return render(request, 'to_do/index.html', context)

@login_required
def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        tarea = task(user=request.user, title=title)
        tarea.save()
        return redirect('add')  

    # Si el método no es POST, se ejecuta esto
    to_do_task = task.objects.filter(user=request.user)
    context = {'to_do_task': to_do_task}
    return render(request, 'to_do/add.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add')  
        else:
            error_message = "Usuario o contraseña incorrectos"
            return render(request, 'to_do/login.html', {'error_message': error_message})
    else:
        context = {}
        return render(request, 'to_do/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        print(user)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add') 
    else:
        context = {}
        return render(request, 'to_do/register.html', context)
    
def plan(request):
    context = {}
    return render(request, 'to_do/plan.html', context)

def update_task_status(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        try:
            # Obtén el objeto de la tarea y actualiza su estado completado
            task_obj = task.objects.get(id=task_id)
            current_state = task_obj.completed
            if current_state == False:
                task_obj.completed = True
            else:
                task_obj.completed = False
            task_obj.save()
            return redirect('add')  # Redirige al usuario a una página específica después de actualizar la tarea
        except task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'La tarea no existe'})
    # Si la solicitud no es POST, devuelve un error
    return JsonResponse({'success': False, 'error': 'Solicitud no válida'})

def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task_obj = task.objects.get(pk=task_id)
        task_obj.delete()
    return redirect('add')  

def completed_tasks(request):
    completed_tasks = task.objects.filter(completed=True, user=request.user)
    return render(request, 'to_do/completed.html', {'completed_tasks': completed_tasks})

def add_view(request):
  context = {}
  if request.path == '/add/':
    context['add_link_color'] = '#f00'

  return render(request, 'add.html', context)