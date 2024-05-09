from django.urls import path
from .views import *           # importing views to be called for each route
from static import routes      # importing url routes from the static files in the project dir

urlpatterns = [
    path('profile/'+routes.LIST_MENTORS,listMentors,name='list-mentors'),
    path('profile/'+routes.MENTEE_PROFILE,menteeDetails,name="mentee-details")
]