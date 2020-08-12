from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import datetime
from datetime import datetime
import time

# Create your models here.
class Task(models.Model):
    
	task_type=models.IntegerField()
	task_desc=models.TextField()

	

class TaskTracker(models.Model):
    task_type=models.IntegerField(choices=list(zip(range(1, 5), range(1, 5))), unique=True)
    update_type=models.DateField(default='%d %b, %Y')
    email=models.EmailField(max_length=254)
    
    def __str__(self):
        return self.email



	
    