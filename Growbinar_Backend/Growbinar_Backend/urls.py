from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404
from rest_framework.response import Response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Authentication.urls'))
]
