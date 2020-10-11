from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.db.utils import IntegrityError

from .models import Profile
from .forms import ProfileForm,SignupForm

def update_profile(request):

    """Update a user's profile view"""

    profile =request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')
 
            
    else:
        form =ProfileForm()

    context= {
        'profile':profile,
        'user': request.user,
        'form': form,

    }
    return render(request,'users/update_profile.html',context)


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
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
        return render(request,'users/signup.html',{'form':form})





   
