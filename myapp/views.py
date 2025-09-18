from django.shortcuts import render, redirect,get_list_or_404
from django.http import HttpResponse
from .models import Project, Task
from .forms import CreateNewTask,CreateNewProject

def index(request):
    title = 'Djando courseeee !!!!'
    return render(request, "index.html", {'title': title})   

def about(request):
    username = 'fazt'
    return render(request, "about.html", {'username': username})

def hello(request, username):
    return HttpResponse(f"<h1>parametro dentro de la etiqueta ({username})</h1>")

def projects(request):
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {'projects': projects})

def task(request):
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {'tasks': tasks})

def create_task(request):
    if request.method == 'GET':
        form = CreateNewTask()
        return render(request, 'tasks/create_task.html', {'form': form})
    else:  # POST
        form = CreateNewTask(request.POST)
        if form.is_valid():
            Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                project_id=2   # 👈 usa project_id, porque en models es "project"
            )
            return redirect('tasks')
        else:
            return render(request, 'create_task.html', {'form': form})

def create_project(request):
   if request.method=='GET':
        return render(request,'projects/create_project.html',
                  {
                      'form' : CreateNewProject()
                  }
                  )
   else:
        project= Project.objects.create(name=request.POST["name"])
        return redirect('projects')

def project_detail(request, id):
    project = Project.objects.get(id=id)
    tasks = Task.objects.filter(project_id=id)  # tareas relacionadas al proyecto
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })
