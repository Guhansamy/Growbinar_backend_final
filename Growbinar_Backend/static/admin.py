from django.contrib import admin
from .models import Mentee,Mentor,Experience

admin.site.register(Mentee)
admin.site.register(Mentor)
admin.site.register(Experience)