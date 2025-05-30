from django.shortcuts import render,redirect
from .models import contactus
from django.contrib import messages
import requests
from django.contrib.auth import authenticate, login

from .models import CustomUser
# Create your views here.
def main_page(request):
    return render(request,'portfolio/main_page.html')

from django.shortcuts import render,redirect
from .models import contactus
from django.contrib import messages

# Create your views here.
def main_page(request):
    return render(request,'portfolio/main_page.html')

def contact_submit(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        descriptions=request.POST.get('description')
        data=contactus(
                name=name,
                email=email,
                subject=subject,
                descriptions=descriptions,               
            )
        data.save()
        return redirect('main_page')          
    return redirect('main_page')

def weather_check(request):
    api_key='63311385f9b7bb0b44d483fa6c9d3966'
    context={}
    #https://api.openweathermap.org/data/2.5/weather?q=barasat&appid=63311385f9b7bb0b44d483fa6c9d3966&units=metric
    if request.method=='POST':
        city=request.POST.get('city_name')       
        api=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response=requests.get(api)
        
        if response.status_code==200:           
            data=response.json()
            context={
                'city':city,
                'tempareture':data['main']['temp'],
                'condition': data['weather'][0]['description'],
                'humidity':data['main']['humidity'],
                'speed': data['wind']['speed'],
            }
            messages.success(request,'Weather fetched')
            return render(request,'portfolio/weathercheck.html',context)
        else:
            messages.error(request,"Not fetched weather!!")
            return redirect('weather_check')
    return render(request,'portfolio/weathercheck.html')

def text_analyse(request):
    if request.method == "POST":
        text = request.POST.get('text', '')
        uppercase = request.POST.get('uppercase', 'off')
        lowercase = request.POST.get('lowercase', 'off')
        capitalize = request.POST.get('capitalize', 'off')
        removePunctuation = request.POST.get('removePunctuation', 'off')

        # 1. Remove punctuation
        if removePunctuation == 'on':
            punctuation = '''!@#$%^&*()-_=+[]{};:'"\|,.<>?/`~'''
            text = ''.join(char for char in text if char not in punctuation)

        # 2. Apply case transformation based on priority
        if capitalize == 'on':
            text = text.capitalize()
        elif lowercase == 'on':
            text = text.lower()
        elif uppercase == 'on':
            text = text.upper()

        context = {'analyse': text}
        return render(request, 'portfolio/textresult.html', context)

    return render(request, 'portfolio/text_index.html')

def text_result(request):
    return render(request,'portfolio/textresukt.html')

def management_page(request):
    return render(request,'portfolio/management_page.html')

def management_student_login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        user=authenticate(request,email=email,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('management_page')
        else:
            messages.error(request,"Invaild Email/Password!!")
            return redirect('management_student_login')
    return render(request,'portfolio/management_st_login.html')

def management_teacher_login(request):
    if request.method=='POST':
        staff_email=request.POST.get('s-email')
        password=request.POST.get('password')
        
        user=authenticate(request,email=staff_email,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('main_page')
        else:
            messages.error(request,"Invaild Email/Password!!")
            return redirect('management_student_login')
        
    return render(request,'portfolio/management_te_login.html')

def management_student_signup(request):
    if request.method=="POST":
        name=request.POST.get('name')
        clg_roll=request.POST.get('clg-roll')
        clg_reg=request.POST.get('clg-reg')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        if CustomUser.objects.filter(clg_roll=clg_roll).exists():
            messages.error(request,"Roll Number already exits")
            return redirect('management_student_signup')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request,"Email already exits")
            return redirect('management_student_signup')
            
        user=CustomUser.objects.create_user(
            name=name,           
            clg_roll=clg_roll,
            clg_reg=clg_reg,
            email=email,
            password=password
        )
        user.save()
        messages.success(request,"Acc Created")
        return redirect('management_student_login')
        
    return render(request,'portfolio/management_st_signup.html') 
 
def management_teacher_signup(request):
    if request.method=="POST":
        stf_name=request.POST.get('t-name')
        stf_id=request.POST.get('stf-id')
        stf_email=request.POST.get('stf-email')
        password=request.POST.get('password')
        
        if CustomUser.objects.filter(s_id=stf_id).exists():
            messages.error(request,"Staff Id already exits")
            return redirect('management_teacher_signup')
        
        if CustomUser.objects.filter(email=stf_email).exists():
            messages.error(request,"Staff email Id already exits")
            return redirect('management_teacher_signup')
        
        user=CustomUser.objects.create_user(
            s_name=stf_name,
            email=stf_email,
            s_id=stf_id,
            password=password,           
        )
        user.save()
        messages.success(request,"Teacher acc Created")
        return redirect('management_teacher_login')
    return render(request,'portfolio/management_te_signup.html')
