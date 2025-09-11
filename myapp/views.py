from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

def index(request):
    return HttpResponse("index page")

def about(request):
    return HttpResponse("<h1>Se está llamando a la función about</h1>")

def hello(request, username):
    return HttpResponse(f"<h1>parametro dentro de la etiqueta ({username})</h1>")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def task(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f'task: {task}')
