from django.contrib import admin
from .models import ImageUpload,userquary

class desImage(admin.ModelAdmin):
    list_display=('title','image')
admin.site.register(ImageUpload,desImage)


class user_des(admin.ModelAdmin):
    list_display=('name','queary_sub','details')
admin.site.register(userquary,user_des)        