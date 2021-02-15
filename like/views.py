from django.shortcuts import get_list_or_404, redirect
from django.views import View
from posts.models import Post
from like.models import Like



class LikeView(View):

    def post(self,request,*args,**kwargs):

        user = request.user
        post_id = kwargs['pk']

        post = Post.objects.get(pk=post_id)
        print(post)

        like = Like.objects.filter(user=user).filter(post=post_id)

        if like:
            like.delete()
        else:
            Like.objects.create(user=user,post=post)

        return redirect('/')

