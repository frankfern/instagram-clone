from django.urls import path

from . import views


urlpatterns = [
    path("<str:pk>/", views.LikeView.as_view(), name="like"),
]
