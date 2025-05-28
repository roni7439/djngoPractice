
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.mainPage,name='mainPage'),
    path('login/',views.login_page,name='login_page'),
    path('signup/',views.signup_page,name='signup_page'),
    path('logout/',views.login_page,name='logout_page'),
    
    path('upload/', views.upload_image, name='upload_image'),
    path('user_queary/',views.user_queary,name='user_queary'),\
    path('user_queary_delete/<id>',views.user_queary_delete,name='user_queary_delete'),
    path('search_item_queary/',views.search_item_queary,name='search_item_queary'),
    path('user_queary_edit/<id>',views.user_queary_edit,name='user_queary_edit'),
    
    path('food_section/',views.food_section,name='food_section'),
    path('food_serach/',views.food_search,name='food_serach'),
    
]
