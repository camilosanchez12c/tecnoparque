from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  #  relación con Project

    def __str__(self):
        return self.title
