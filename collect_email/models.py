from django.db import models

# Create your models here.
from django.shortcuts import render
from django.db import models


# Create your views here.
class Click(models.Model):
    ip_address = models.CharField(max_length=100)
    machine_name = models.TextField()
    username = models.CharField(max_length=100)
    clicked_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"Clicked by {self.username} on {self.machine_name} at {self.clicked_at}"