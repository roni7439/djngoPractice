from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import userquary
import requests


from .forms import ImageUploadForm

@login_required(login_url='login_page')
def mainPage(request):
    show_data=userquary.objects.all().order_by("queary_sub")
    context={
        'show_data': show_data,
    }
    return render(request,'mainPage.html',context)
def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(
            username=username,
            password=password,
        )
        if user is None:
            messages.error(request,"Invalid Password or Email")
            return redirect('login_page')
        else:
            login(request,user)
            messages.success(request,"Acc Crated!")
            return redirect('mainPage')  
    return render(request,'login_page.html')

def signup_page(request):
    if request.method=="POST":
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email ALrady Present")
            return redirect('signup_page')
        elif User.objects.filter(username=username).exists():
            messages.error(request,"Username already present")
            return redirect('signup_page')
        else:
            user=User.objects.create(
                email=email,
                username=username,
            )
            user.set_password(password)
            user.save()
            return redirect('login_page')
    return render(request,'signup_page.html')

def logout_page(request):
    if request.method=="POST":
        logout(request)
    return redirect('login_page')


def upload_image(request):
    if request.method=='POST':
        form=ImageUploadForm(request.POST, request.FILIES)
        if form.is_valid():
           form.save()
        else:
            form=ImageUploadForm()   
    return render(request,'mainPage.html',{'form':form})

def user_queary(request):
    queary=None
    if request.method=="POST":
        username=request.POST.get('name')
        user_queary_sub=request.POST.get('sub-q')
        user_details=request.POST.get('details')
        
        queary=userquary(
            name=username,
            queary_sub=user_queary_sub,
            details=user_details,
        )
       
        queary.save()
        
    else:
        messages.error(request,"Not Submited")

    return redirect('mainPage')

def user_queary_edit(request,id):
    queary=get_object_or_404(userquary,id=id)
    if request.method=="POST":
        queary.name=request.POST.get('name')
        queary.queary_sub=request.POST.get('sub-q')
        queary.details=request.POST.get('details')
        
        queary.save()
        return redirect('mainPage')
    return redirect('mainPage')
def user_queary_delete(request,id):
    detele_data=get_object_or_404(userquary,id=id)
    detele_data.delete()
    return redirect('mainPage')

def search_item_queary(request):
    search=None
    if request.method=="POST":
        search=request.POST.get('search_item')
        if search != None:
            show_data=userquary.objects.filter(name__icontains=search)
        else:
            show_data=userquary.objects.all()
        return render(request,'mainPage.html',{'show_data':show_data,'search_item':search})  
    return redirect('mainPage')

def food_section(request):
    return render(request,'food.html')

# def food_search(request):
    
#     #api key-  https://www.themealdb.com/api/json/v2/1/search.php?s=steak
#     context={}
#     if request.method=="POST":
#         food_name=request.POST.get('food')
#         api_key=f'https://www.themealdb.com/api/json/v2/1/search.php?s={food_name}'
#         response=requests.get(api_key)
        
#         if response.status_code==200:
#             data=response.json()
#             context={
#                 'dish_namw': data[meals][0][strMeal]
#             }
        
#     return redirect('food.html',context)

def food_search(request):
    context = {}
    if request.method == "POST":
        food_name = request.POST.get('food')
        api_url = f'https://www.themealdb.com/api/json/v1/1/search.php?s={food_name}'

        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            meals = data.get('meals',[])
            
            context={
                'meals':  meals,
                'value': food_name,
            }
        else:
            messages.error(request,'Failed to fetch data from API.')

    return render(request, 'food.html', context)
