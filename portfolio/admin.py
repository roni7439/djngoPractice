from django.contrib import admin
<<<<<<< HEAD
from .models import contactus
=======
from .models import contactus,acc_details
>>>>>>> a651631 (Initial commit: add Django project files)
from .models import CustomUser
# Register your models here.

class contact(admin.ModelAdmin):
    list_display=('name','email','subject','descriptions')
    
admin.site.register(contactus,contact)

<<<<<<< HEAD
admin.site.register(CustomUser)   
=======
admin.site.register(CustomUser)

class acca_details_content(admin.ModelAdmin):
    list_display=('semster','degree','course_type','course_dur')
    
admin.site.register(acc_details,acca_details_content)    
>>>>>>> a651631 (Initial commit: add Django project files)
