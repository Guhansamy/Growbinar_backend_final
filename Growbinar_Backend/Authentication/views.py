from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Mentee,Mentor
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.contrib.auth.hashers import make_password,check_password
from rest_framework_simplejwt.tokens import AccessToken

@api_view(['POST'])
def MenteeSignup(request):
    try:
        print(request.data)
        instance = Mentee.objects.create(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            password=make_password(request.data['password']),
            country=request.data['country'],
            email_id=request.data['email_id'],
            phone_number=request.data['phone_number'],
            gender=request.data['gender'],
            date_of_birth=request.data['date_of_birth'],
            city=request.data['city'],
            areas_of_interest=request.data['areas_of_interest'],
            profile_picture_url=request.data['profile_picture_url'],
            description=request.data['description'],
            role=request.data['role'],
            organization=request.data['organization'],
            is_experience=request.data['is_experience'],
            )

        # instance.set_password(request.data['password'])
        instance.save()

        return Response(json.dumps({'message':'Mentee created sucessfully'}), status=201)
    except Exception as e:
        print('error da ',e)
        return Response(json.dumps({'message':'Error creating Mentee'}), status=500)


@api_view(['POST'])
def MentorSignup(request):
    try:
        print(request.data)
        instance = Mentor.objects.create(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            country=request.data['country'],
            email_id=request.data['email_id'],
            phone_number=request.data['phone_number'],
            password=make_password(request.data['password']),
            gender=request.data['gender'],
            date_of_birth=request.data['date_of_birth'],
            city=request.data['city'],
            bio=request.data['bio'],  
            profile_picture_url=request.data['profile_picture_url'],
            areas_of_expertise=request.data['areas_of_expertise'], 
            number_of_likes=0, 
            languages=request.data['languages'], 
            experienceMentor=request.data['experienceMentor'], 
            designation=request.data['designation'], 
            company=request.data['company'], 
            is_top_rated=False,  
            is_experience=request.data['is_experience'], 
        )
        
        instance.save()

        return Response(json.dumps({'message':'Mentor created sucessfully'}), status=201)
    except Exception as e:
        print('error da ',e)
        return Response(json.dumps({'message':'Error creating Mentor'}), status=500)
    

@api_view(['POST'])
def MentorLogin(request):
    try:
        print(request.data)
        email = request.data.get('email')
        password = request.data.get('password')

        mentor = Mentor.objects.filter(email_id=email).first()
        print(mentor)

        if mentor and check_password(password, mentor.password):
            token = AccessToken.for_user(mentor)
            return Response(json.dumps(
                {
                'Message': 'Mentor logged in successfully',
                'token': str(token)
            }), status=200)
            
        else:
            return Response(json.dumps({'Message': 'Invalid User'}), status=400)

    except Exception as ex:
        print(ex)
        return Response(json.dumps({'Message': 'An error occurred while logging in'}), status=500)
    
    
@api_view(['POST'])
def MenteeLogin(request):
    try:
        print(request.data)
        email = request.data.get('email')
        password = request.data.get('password')

        mentee = Mentee.objects.filter(email_id=email).first()
        print(mentee)

        if mentee and check_password(password, mentee.password):
            token = AccessToken.for_user(mentee)
            return Response(json.dumps(
                {
                'Message': 'Mentee logged in successfully',
                'token': str(token)
            }), status=200)
            
        else:
            return Response(json.dumps({'Message': 'Invalid User'}), status=400)

    except Exception as ex:
        print(ex)
        return Response(json.dumps({'Message': 'An error occurred while logging in'}), status=500)

