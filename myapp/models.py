from django.db import models

#esta parte es para la crecacion de las tablas en la base de datos 
class Project(models.Model):
    name=models.CharField(max_length=200)


class Task(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    project=models.ForeignKey(Project,on_delete=models.CASCADE)#con el foreignkey esto es para hacer la relacion con la otra tabla de project