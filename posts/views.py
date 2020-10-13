# django
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView,CreateView

# utilities
from datetime import datetime

#custom
from .forms import PostForm
from .models import Post

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "posts/feed.html"
    queryset = Post.objects.all()
    context_object_name = 'posts'
    ordering = ('-created',)
    paginate_by = 2

class PostDetailView(LoginRequiredMixin,DetailView):

    template_name = "posts/detail.html"
    queryset = Post.objects.all()
    context_object_name = 'post'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'

class PostCreateView(LoginRequiredMixin,CreateView):

    template_name = "posts/new.html"
    success_url = reverse_lazy('posts:feed')
    form_class = PostForm

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile

        return context
    




@login_required
def create_post(request):
    """Create new post"""

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()
    

    return render(
        request=request,
        template_name='posts/new.html',
        context=
        {
            'form':form,
            'user':request.user,
            'profile': request.user.profile
        })
        

