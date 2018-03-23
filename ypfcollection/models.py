from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Player(models.Model):
     name = models.CharField(max_length=200)
     amount = models.IntegerField(default=0) 

class Team(models.Model):
     player = models.ForeignKey(Player, on_delete=models.CASCADE)
     match_date = models.DateTimeField('date published')
	 
class Match(models.Model):
     amount = models.IntegerField(default=0) 
     match_date = models.DateTimeField('date published')
	 
