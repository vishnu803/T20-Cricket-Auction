from django.db import models
from T20predictions.settings import BASE_DIR

# Create your models here.
class Rooms(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img  = models.ImageField(upload_to = 'pics')
    RoomId= models.IntegerField(default=0)