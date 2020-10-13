from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.views.generic import DetailView

from django.db.utils import IntegrityError

from .models import Profile
from posts.models import Post
from .forms import ProfileForm,SignupForm

class UserDetailView(LoginRequiredMixin,DetailView):
    model = User
    template_name = "users/detail.html"
    slug_field = 'username'
    slug_url_kwarg = 'username' 
    queryset = User.objects.all()
    contetx_object_name = 'user'

    def get_context_data(self, **kwargs):
        """ADd  post to user context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["posts"] = Post.objects.filter(user=user).order_by("-created")
        return context
    


@login_required
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

            # url = reverse('users:detail',kwargs={'username':request.user.username})

            # return redirect('')
 
            
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
            return redirect('posts:feed')
        else:
            return render(request,'users/login.html',{'error':'Invalid username or password'} )
        
    return render(request, 'users/login.html' )

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')


def sign_up(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()
        return render(request,'users/signup.html',{'form':form})





   
