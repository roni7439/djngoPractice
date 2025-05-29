from django.shortcuts import render,redirect
from .models import contactus
from django.contrib import messages
import requests

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
