from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager

# Create your models here.

class contactus(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    subject=models.CharField(max_length=20)
    descriptions=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

#create custom signup
class CustomUserManager(BaseUserManager):
    def create_user(self,name=None,clg_roll=None,clg_reg=None,email=None,password=None,s_name=None,s_id=None):
        
         # Only validate clg_roll if it's a student
        if not clg_roll and not s_id:
            raise ValueError("Either Student Roll or Staff ID is required")
           
        user=self.model(
            name=name,
            clg_roll=clg_roll,
            clg_reg=clg_reg,
            email=email,
            s_name=s_name,
            s_id=s_id,
        )
        user.set_password(password) 
        user.save(using=self._db)
        return user
    def create_superuser(self, name, clg_roll, clg_reg, email, password,s_name=None,s_id=None):
        user = self.create_user(name, clg_roll, clg_reg, email, password,s_name,s_id)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser,PermissionsMixin):
    username=None
    name=models.CharField(max_length=30,blank=True,null=True)
    clg_roll=models.CharField(max_length=30,unique=True,blank=True,null=True)
    clg_reg=models.CharField(max_length=40,blank=True,null=True)
    email=models.EmailField(unique=True)
    
    #for teacher
    s_name=models.CharField(max_length=30,blank=True,null=True)
    s_id=models.CharField(max_length=10,blank=True,null=True)
    
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects=CustomUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['name']
    
    def __str__(self):
        return f'{self.name}-{self.clg_roll}'