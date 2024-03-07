from django.shortcuts import render


def homePage(request):
    return render(request,"index.html")

def DASHBOARD(request):
    return render(request,"DASHBOARD.html")

def CONTACTUS(request):
    return render(request,"CONTACTUS.html")

def ABOUTUS(request):
    return render(request,"ABOUTUS.html")

def LOGIN(request):
    return render(request,"LOGIN.html")

def registrationpage(request):
    return render(request,"register.html")