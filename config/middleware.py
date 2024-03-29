"""Middleewares catalog"""

#django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletationMiddleware:
    """Profile completation middleware.
    
    Ensure every user that is interacting with the platform have their 
    profile picture at biografy
    """

    def __init__(self, get_response):
        """Middleware initialitation"""
        self.get_response = get_response

    def __call__(self,request):
        """Code to be executed fot each request before the view is called"""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:logout'),reverse('users:update')]:
                        return redirect('users:update')
        
        response = self.get_response(request)
        return response