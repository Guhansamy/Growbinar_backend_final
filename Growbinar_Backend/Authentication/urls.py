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
    path(routes.MENTEE_SIGNUP_ROUTE, MenteeSignup,name='mentee-signup'),
    path(routes.MENTOR_SIGNUP_ROUTE, MentorSignup,name='mentor-signup'),
    path(routes.VERIFY_MENTEE_ROUTE, VerifyMentee,name='verify-mentee-email'),
    path(routes.VERIFY_MENTOR_ROUTE, VerifyMentor,name='verify-mentor-email'),
    path(routes.MENTOR_DETAILS,getMentorDetails,name="get-mentor-details"),
    path(routes.MENTEE_DETAILS,getMenteeDetails,name="get-mentee-details"),
]