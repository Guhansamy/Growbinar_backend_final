from static.models import Mentee,Mentor
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MentorSerializer,MenteeSerializer
from static.message_constants import invalidCred,userCreated,emailExists,signupError,verifiedUserEmail,errorVerifingUserEmail
from static.routes import VerifyMenteeEmail,VerifyMentorEmail
from django.contrib.auth.hashers import make_password,check_password
from .emailVerification import sendVerificationMail
import logging

@api_view(['POST'])
def MenteeSignup(request):
    logger = logging.getLogger("Authentication")
    logger.debug("Entered mentee-signup")
    try:
        # chekking weather email already exixts
        if Mentee.objects.filter(email_id=request.data['email_id']).exists():
            logger.debug("Email already exists as a mentee")
            return Response({"message":emailExists['message']},status=emailExists['status'])

        request.data['is_emal_verified']=False
        serializer = MenteeSerializer(data=request.data)
        print(request.data)
        # validating the payload
        valid=serializer.is_valid()
        if valid:
            # creating mentor object
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
            instance.save()
            logger.debug("signup successfull")
            sendVerificationMail(VerifyMenteeEmail+"?id="+str(instance.id),request.data['email_id'])
            return Response({'message':userCreated['message']}, status=userCreated['status'])
        else:
            # sending bad request response for invalid payload
            logger.warn("invalid credentails for signup")
            return Response({"message":invalidCred['message']},status=invalidCred['status'])
    except Exception as e:
        logger.error("Error creating a mentee"+str(e))
        return Response({'message':signupError['message']}, status=signupError['status'])

@api_view(['POST'])
def MentorSignup(request):
    logger = logging.getLogger("Authentication")
    logger.debug("Entered mentor-signup")
    try:
        # chekking weather email already exixts
        if Mentor.objects.filter(email_id=request.data['email_id']).exists():
            logger.debug("Email already exists")
            return Response({"message":emailExists['message']},status=emailExists['status'])

        request.data['is_emal_verified']=False
        serializer = MentorSerializer(data=request.data)
        print(request.data)
        # validating the payload
        valid=serializer.is_valid()
        if valid:
            # creating mentor object
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
                MentorExperience=request.data['MentorExperience'], 
                designation=request.data['designation'], 
                company=request.data['company'], 
                is_top_rated=False,  
                is_experience=request.data['is_experience'], 
            )
            instance.save()
            logger.debug("signup successfull")
            sendVerificationMail(VerifyMentorEmail+"?id="+str(instance.id),request.data['email_id'])
            return Response({'message':userCreated['message']}, status=userCreated['status'])
        else:
            # sending bad request response
            logger.warn("invalid credentails for signup")
            print(serializer.errors)
            return Response({"message":invalidCred['message']},status=invalidCred['status'])
    except Exception as e:
        logger.error("Error creating a mentor"+str(e))
        return Response({'message':signupError['message']}, status=signupError['status'])

@api_view(['GET'])
def VerifyMentee(request):
    logger = logging.getLogger("Authentication")
    logger.debug('Entered email verification of mentee')
    try:
        # Getting mentee id from the url and setting is_email_verified to True
        menteeID = request.GET.get('id')
        mentee = Mentee.objects.get(id=menteeID)
        mentee.is_email_verified = True
        mentee.save()
        logger.debug('Email verification sucess for '+menteeID)
        return Response({'message':verifiedUserEmail['message']},status=verifiedUserEmail['status'])
    except Exception as e:
        logger.error("Error verifying email "+str(e))
        return Response({'message':errorVerifingUserEmail['message']},status=errorVerifingUserEmail['status'])

@api_view(['GET'])
def VerifyMentor(request):
    logger = logging.getLogger("Authentication")
    logger.debug('Entered emailverification mentor')
    try:
        # Getting mentor id from the url and setting is_email_verified to True
        mentorID = request.GET.get('id')
        mentor = Mentor.objects.get(id=mentorID)
        mentor.is_email_verified = True
        mentor.save()
        logger.debug('Email verification sucess for '+mentorID)
        return Response({'message':verifiedUserEmail['message']},status=verifiedUserEmail['status'])
    except Exception as e:
        logger.error("Error verifying email "+str(e))
        return Response({'message':errorVerifingUserEmail['message']},status=errorVerifingUserEmail['status'])