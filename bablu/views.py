from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from . models import UserProfile
# Create your views here.

#login views
def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        if not request.user.is_anonymous:
            return redirect('home')
        return render(request,'index.html')

#home views
@login_required(login_url='login')
def Home(request):
    user=request.user
    pro=UserProfile.objects.get(user=user)
    con={'username':user.username,'status':pro.status,'location':pro.location}
    return render(request,'home.html',con)
#profile views
@login_required(login_url='login')
def Profile(request):
    user=request.user
    pro=UserProfile.objects.get(user=user)
    con={'username':user.username,'status':pro.status,'location':pro.location,'image':pro.pic}
    return render(request,'profile.html',con)
def Logout(request):
    logout(request)
    return redirect('login')
def Register(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            user=User(username=username)
            user.set_password(password1)
            user.save()
            pro=UserProfile(user=user)
            pro.save()
            return redirect('login')
        else:
            return redirect('login')
        
def Update_profile(request):
    if request.method=='POST':
        status=request.POST['status']
        loc=request.POST['location']
        pro=UserProfile.objects.get(user=request.user)
        pro.status=status
        pro.location=loc
        pro.save()
        return redirect ('profile')
    else:
        return redirect ('profile')




