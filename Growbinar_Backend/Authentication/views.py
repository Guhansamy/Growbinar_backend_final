from static.models import Mentee,Mentor
from rest_framework.decorators import api_view
from static.message_constants import LOGIN_SUCCESS,INVALID_ROLE,LOGIN_ERROR,INVALID_CREDENTIALS,STATUSES,USER_NOT_FOUND
from django.contrib.auth.hashers import check_password
from .LoggerMessage import log
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.decorators import api_view
from django.http import JsonResponse


@api_view(['POST'])
def user_login(request):
    print("Request has Entered into User Login Page")
    log("Entered User-Login ",1)

    try:
        print(request.data)
        email = request.data.get('email')
        password = request.data.get('password')
        user_role = request.data.get('user_role')  # 'mentor' or 'mentee'

        if user_role == 'mentor':
                 # Request entered where the user exist
            user = Mentor.objects.filter(email_id=email).first()
            log("User is Mentor",1)

        elif user_role == 'mentee':
            user = Mentee.objects.filter(email_id=email).first()
            log("User is Mentee",1)
            
        else:
            log("Invalid user_role",3)
            return JsonResponse({'message' : INVALID_ROLE},status = STATUSES['BAD_REQUEST'])
            

       

        print(user)

        if not user:
                    # Request entered were user not exist
            if user_role == 'mentor':
                log("User Not Found",2)
                return JsonResponse({'message' : USER_NOT_FOUND }, status = STATUSES['BAD_REQUEST'])
            
            else :
                log("User Not Found",2)
                return JsonResponse({'message' :USER_NOT_FOUND},status = STATUSES['BAD_REQUEST'])
            
        if check_password(password, user.password):
        # if (password == user.password):
            token = AccessToken.for_user(user)
            log("User Logged In",1)
            return JsonResponse({
                'message': LOGIN_SUCCESS,  # Using 'message' key
                'token': str(token),
                'data' : {
                    'name' : user.first_name + user.last_name,
                    'email' : email,
                    'role' : user_role
                }
            }, status= STATUSES['SUCCESS'])
        
        else:
            log("Invalid Credentials",3)
            return JsonResponse({'message' : INVALID_CREDENTIALS}, status = STATUSES['BAD_REQUEST'])
            
    except Exception as ex:
        print(ex)
        log('Error while Login  ' + str(ex),3)
        return JsonResponse({'message' : LOGIN_ERROR}, status = STATUSES['INTERNAL_SERVER_ERROR'])
