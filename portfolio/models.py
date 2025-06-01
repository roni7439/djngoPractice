from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager
from django.conf import settings

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
    def create_user(self, name=None, clg_roll=None, clg_reg=None, email=None, password=None, s_name=None, s_id=None):
        if not clg_roll and not s_id:
            raise ValueError("Either Student Roll or Staff ID is required")

        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(
            name=name,
            clg_roll=clg_roll or 'ADMIN',
            clg_reg=clg_reg or 'ADMIN',
            email=email,
            s_name=s_name,
            s_id=s_id,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        # Provide defaults for required fields that are missing
        extra_fields.setdefault('name', 'Admin')
        extra_fields.setdefault('clg_roll', 'ADMIN')
        extra_fields.setdefault('clg_reg', 'ADMIN')
        extra_fields.setdefault('s_name', None)
        extra_fields.setdefault('s_id', None)

        return self.create_user(
            name=extra_fields.get('name'),
            clg_roll=extra_fields.get('clg_roll'),
            clg_reg=extra_fields.get('clg_reg'),
            email=email,
            password=password,
            s_name=extra_fields.get('s_name'),
            s_id=extra_fields.get('s_id')
        )

class CustomUser(AbstractUser,PermissionsMixin):
    username=None
    name=models.CharField(max_length=30,blank=True,null=True)
    clg_roll=models.CharField(max_length=30,unique=False,blank=True,null=True)
    clg_reg=models.CharField(max_length=40,blank=True,null=True)
    email=models.EmailField(unique=True)
    
    #for teacher
    s_name=models.CharField(max_length=30,blank=True,null=True)
    s_id=models.CharField(max_length=10,blank=True,null=True)
    
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    
    objects=CustomUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['name']
    
    def __str__(self):
        return f'{self.name}-{self.clg_roll}'
    
    
class acc_details(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    semster=models.CharField(max_length=4)
    degree=models.CharField(max_length=40)
    course_type=models.CharField(max_length=20)
    course_dur=models.CharField(max_length=10)
    
    def __str__(self):
        return str(self.user)
    