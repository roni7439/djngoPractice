
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.main_page,name="main_page"),
    path('contact_submit/',views.contact_submit,name='contact_submit'),
    path('weather_check/',views.weather_check,name='weather_check'),
    path('text_analyse/',views.text_analyse,name='text_analyse'),
    path('text_result/',views.text_result,name='text_result'),
    path('management_page/',views.management_page,name='management_page'),
    path('management_student_login',views.management_student_login,name='management_student_login'),
    path('management_teacher_login',views.management_teacher_login,name='management_teacher_login'),
    path('management_student_signup/',views.management_student_signup,name='management_student_signup'),
    path('management_teacher_signup/',views.management_teacher_signup,name='management_teacher_signup'),

    path('student_management/',views.student_management,name='student_management'),
    path('accademic_details/',views.accademic_details,name='accademic_details'),
    path('logout_page/',views.logout_page,name='logout_page'),
    

]
