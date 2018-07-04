from django.db import models

# Create your models here.

class Jobprofile(models.Model):
    Jobid = models.CharField(max_length=5)
    Role = models.CharField(max_length=500)
    Skills = models.CharField(max_length=5000)
    Positions = models.IntegerField(default=1)
    Location = models.CharField(max_length=50,default="Chennai")



