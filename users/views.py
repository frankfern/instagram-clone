from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.db.utils import IntegrityError

from .models import Profile

def update_profile(request):
    """Update a user's profile view"""
    return render(request,'users/update_profile.html')


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username= username,password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request,'users/login.html',{'error':'Invalid username or password'} )
        
    return render(request, 'users/login.html' )

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def sign_up(request):


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password_confirmation']
        

        if password != password2:
            return render(request, 'users/signup.html',{'error':'password confirmation doesnt match'})

        try:
            user = User.objects.create_user(username=username,password=password)
        
        except IntegrityError:
            return render(request, 'users/signup.html',{'error':'Username is already in user'})

        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()


        profile=Profile(user=user)
        profile.save()

        return redirect('login')


    return render(request, 'users/signup.html' )
