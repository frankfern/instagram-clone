from django.urls import path

from . import views


urlpatterns = [
    path('login/',views.login_view,name='login'),
    path("logout/",views.logout_view, name="logout"),
    path("signup/",views.sign_up, name="sign_up"),
    path("me/profile/",views.update_profile , name="update_profile")
]