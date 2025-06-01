from django.contrib import admin

from .models import contactus

from .models import contactus,acc_details

from .models import CustomUser
# Register your models here.


class contact(admin.ModelAdmin):
    list_display=('name','email','subject','descriptions')
    
admin.site.register(contactus,contact)


admin.site.register(CustomUser)   


class acca_details_content(admin.ModelAdmin):
    list_display=('semster','degree','course_type','course_dur')
    
admin.site.register(acc_details,acca_details_content)    

