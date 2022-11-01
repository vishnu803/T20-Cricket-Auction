from datetime import datetime
from django.db import models

# Create your models here.
class matches:
    team1 : str
    team2 : str
    indx : int
    event_key : int
    def __init__(self, t1, t2, i, x) :
        self.team1  = t1
        self.team2 = t2
        self.indx = i
        self.event_key = x