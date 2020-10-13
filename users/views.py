from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.views.generic import DetailView,FormView,UpdateView

from .models import Profile
from posts.models import Post
from .forms import SignupForm

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

class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = Profile
    template_name = 'users/update_profile.html'
    fields = ['website','biography','phone_number','picture']

    def get_object(self):
        """ Return user's profile"""       
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile """
        username = self.object.user.username
        return reverse('users:detail',kwargs={'username':username})

class SignupView(FormView):

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self,form):
        """Save form data"""
        form.save()
        return super().form_valid(form)



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

