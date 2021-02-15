from django.db import models
from django.contrib.auth import get_user_model

User= get_user_model()

class Like(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    post = models.ForeignKey('posts.Post',on_delete=models.CASCADE,related_name='likes')