from django.shortcuts import render

def mysite(request):
    return render(request,'mysite.html')