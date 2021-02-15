from django.urls import path

from . import views


urlpatterns = [
    path("<str:pk>/", views.CommentCreateView.as_view(), name="comment"),
]
