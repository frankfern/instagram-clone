from .forms import CommentForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView



class CommentCreateView(LoginRequiredMixin,CreateView):

    template_name = "posts/new.html"
    success_url = reverse_lazy('posts:feed')
    form_class = CommentForm

    def get_context_data(self, **kwargs):

        post_id = kwargs['pk']
        post = Post.objects.get(pk=post_id)

        context = super().get_context_data(**kwargs)
        
        context['user'] = self.request.user
        context['post'] = post

        return context