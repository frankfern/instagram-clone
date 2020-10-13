from django.urls import path

from . import views


urlpatterns = [
    path('list',views.PostListView.as_view(),name= 'feed'),
    path("<str:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("new", views.create_post, name="new")
]
