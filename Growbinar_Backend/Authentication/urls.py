from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('authtoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authtoken/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]