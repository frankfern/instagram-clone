from django.urls import path

from . import views


urlpatterns = [
    path('list',views.list_posts,name= 'feed'),
    path("new", views.create_post, name="new")
]
