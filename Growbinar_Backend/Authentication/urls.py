from django.urls import path
from .views import *                                    # importing views to be called for each route
from static import routes             # importing url routes from the static files in the project dir
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('authtoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authtoken/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(routes.MenteeSignupRoute, MenteeSignup,name='mentee-signup'),
    path(routes.MentorSignupRoute, MentorSignup,name='mentor-signup'),
    path(routes.VerifyMenteeEmail, VerifyMentee,name='verify-mentee-email'),
    path(routes.VerifyMentorEmail, VerifyMentor,name='verify-mentor-email'),
    path(routes.MentorDetails,getMentorDetails,name="get-mentor-details"),
    path(routes.MenteeDetails,getMenteeDetails,name="get-mentee-details"),
]