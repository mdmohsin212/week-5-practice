from django.db import models

# Create your models here.

class MusicianModel(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=20)
    Instrument_type = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.First_name} {self.Last_name}'
    