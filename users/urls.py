from django.urls import path


from . import views


urlpatterns = [
    path("signup/",views.SignupView.as_view(), name="sign_up"),


    path('login/',views.login_view,name='login'),
    path("logout/",views.logout_view, name="logout"),

    path("me/profile/",views.ProfileUpdateView.as_view() , name="update"),
    path("<str:username>/", views.UserDetailView.as_view(), name="detail"),

]
