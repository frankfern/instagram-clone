from django.db import models
from django.contrib.auth import get_user_model

User= get_user_model()


class Comment(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    post = models.ForeignKey('posts.Post',on_delete=models.CASCADE,related_name='comments')

    text = models.CharField(blank=False,null=False,max_length=50)