from django.db import models
from musician.models import Musician
# Create your models here

class Album(models.Model):
    name = models.CharField(max_length=200,default='')
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE,default='')
    rerelease_date = models.DateField(default= '')
    REATING = [('1','One'),
               ('2','Two'),
               ('3','Three'),
               ('4','Four'),
               ('5','Five')
               ]
    reating = models.CharField(choices=REATING,max_length=50)
    def __str__(self) -> str:
        return f"Album Name: {self.name} : {self.musician}"
    
   