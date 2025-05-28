from django.db import models

# Create your models here.

class contactus(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    subject=models.CharField(max_length=20)
    descriptions=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name