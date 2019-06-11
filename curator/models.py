from django.db import models

# Create your models here.
from django.db import models


class SubjectArea(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    resources = models.CharField(max_length=1000) 
    pub_date = models.DateTimeField('date published')


class Goals(models.Model):
    Subject_arrea = models.ForeignKey(SubjectArea, on_delete=models.CASCADE)
    goal = models.CharField(max_length=400)