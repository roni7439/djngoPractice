from django.contrib import admin
from .models import contactus
# Register your models here.

class contact(admin.ModelAdmin):
    list_display=('name','email','subject','descriptions')
    
admin.site.register(contactus,contact)    
