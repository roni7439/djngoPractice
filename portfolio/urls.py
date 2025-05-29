
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.main_page,name="main_page"),
    path('contact_submit/',views.contact_submit,name='contact_submit'),
    path('weather_check/',views.weather_check,name='weather_check'),
    path('text_analyse/',views.text_analyse,name='text_analyse'),
    path('text_result/',views.text_result,name='text_result'),
]
