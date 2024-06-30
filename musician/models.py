from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=200,default='')
    last_name = models.CharField(max_length=200,default='')
    email = models.EmailField(default='')
    phone_number = models.CharField(max_length=14,default='')
    instrument_type = models.CharField(max_length=100,default='')
    def __str__(self):
        return f'Musician : {self.first_name} {self.last_name}'
    
