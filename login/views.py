from django.shortcuts import render
from django.http import HttpResponse
from login.models import userdata
# Create your views here.
from django.db import connection
cursor=connection.cursor()
def home(request):
    return render(request,'welcome.html')

def admin(request):
    return render(request,'admin.html')

def user(request):
    return render(request,'user.html')

def adm_login(request):
    username=request.GET['username']
    passw=request.GET['password']
    if username!='admin' or passw!='admin':
        return render(request,'admin.html',{"data":'username or password incorrect'})
    else:
        users=userdata.objects.all()
        return render(request,'adminhome.html',{"data":'login successfull',"users":users})

def user_signup(request):
    return render(request,'user_signup.html')

def update_profile(request):
    email=request.GET['email']
    type=request.GET['type']
    value=request.GET['value']
    cursor.execute('update login_userdata set '+type+" = '"+value+"' where email="+email)
    user=userdata.objects.get(email=email)
    return render(request,'user_profile.html',{"user":user})

def validate(request):
    username=request.GET['username']
    passw=request.GET['password']
    user=userdata.objects.filter(name=username,password=passw)
    if len(user)==0:
        return render(request,'user.html',{"data":'username or password incorrect'})
    else:
        return render(request,'user_profile.html',{"user":user[0]})
def signup(request):
    username=request.GET['username']
    password=request.GET['password']
    email=request.GET['email']
    number=request.GET['number']
    entry=userdata(name=username,password=password,email=email,phone=number)
    entry.save()
    return render(request,'user.html',{"data":'signup successfull'})

