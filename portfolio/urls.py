
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.main_page,name="main_page"),
    path('contact_submit/',views.contact_submit,name='contact_submit'),
    path('weather_check/',views.weather_check,name='weather_check')
]
