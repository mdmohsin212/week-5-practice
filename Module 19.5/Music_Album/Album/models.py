from django.db import models
from Musicians.models import MusicianModel
import datetime

# Create your models here.

class AlbumModel(models.Model):
    Album_Name = models.CharField(max_length=30)
    Date = models.DateField(null=True, blank=True, default=datetime.date.today)
    musicians = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    CHOISE = {
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    }
    Rating = models.IntegerField(choices=CHOISE)
    
    def __str__(self):
        return self.Album_Name