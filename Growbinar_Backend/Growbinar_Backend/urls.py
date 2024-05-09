from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404
from rest_framework.response import Response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Authentication.urls')),
    path('',include('profile_details.urls'))
]


def handle404(request, *args, **kwargs):
    return Response({"message":"Invalid url"},status=404)

handler404 = handle404