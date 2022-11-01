from datetime import datetime
import string
from django.db import models

# Create your models here.
class playpts :
    player : string
    points : int
    index : int
    def __init__(self, x, y, i) :
        self.player = x
        self.points = y
        self.index = i
