from rest_framework import serializers
from Models.models import Mentee,Mentor

class MenteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentee
        fields = '__all__'