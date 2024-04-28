from django.urls import path
from .views import * 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('authtoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authtoken/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('mentee-signup/',MenteeSignup,name='MenteeSignup'),
    path('mentor-signup/',MentorSignup,name='MentorSignup')
    
]