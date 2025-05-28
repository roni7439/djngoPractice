from django.db import models

# Create your models here.

class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='test/',max_length=250)
    
    def __str__(self):
        return self.title
    
class userquary(models.Model):
    name=models.CharField(max_length=30)
    queary_sub=models.CharField(max_length=50)
    details=models.CharField(max_length=200)    
    
    def __str__(self):
        return self.name
    
