from static.models import Mentee,Mentor,Experience
from rest_framework.response import Response
from rest_framework.decorators import api_view
from static.message_constants import STATUSES,INVALID_CREDENTIALS,USER_CREATED,EMAIL_EXISTS,SIGNUP_ERROR,VERIFIED_USER_EMAIL,ERROR_VERIFYING_USER_EMAIL,USER_DETAILS_SAVED,ERROR_SAVING_USER_DETAILS,EMAIL_NOT_VERIFIFED,ERROR_GETTING_MENTOR_DETAILS
from static.routes import VERIFY_MENTEE_ROUTE,VERIFY_MENTOR_ROUTE
from .assets import urlShortner,log

@api_view(['GET'])
def listMentors(request):
    log("Entered list Mentors",1)
    try:
        # getting required fields from the mentor table for each mentor
        mentors = Mentor.objects.raw("SELECT id,profile_picture_url,is_top_rated,is_experience,languages,first_name,last_name,designation,company,mentor_experience FROM static_mentor;")
        data = []
        # iterating through the query set to convert each instance to an proper list 
        for mentor in mentors:
            value = dict()
            value['mentor_id']=mentor.id 
            value['profile_picture_url']=urlShortner(mentor.profile_picture_url) # implementing url shortner
            value['languages']=mentor.languages
            value['name'] = mentor.first_name + " " + mentor.last_name
            value['role'] = mentor.designation
            value['organization'] = mentor.company
            value['experience'] = mentor.mentor_experience
            # checking for mentor tags like toprated and exclusive
            if mentor.is_top_rated:
                value['tag'] = 'TopRated'
            elif mentor.is_experience:
                value['tag'] = 'Exclusive'
            else:
                value['tag'] = None
            
            data.append(value)
        log("Mentors listed successfully",1)
        return Response({'data':data},status=STATUSES['SUCCESS'])
    except Exception as e:
        log("Error in list mentors"+str(e), 3)
        return Response({'message':ERROR_GETTING_MENTOR_DETAILS},status=STATUSES['INTERNAL_SERVER_ERROR'])

@api_view(['POST'])
def menteeDetails(request):
    log("Entered mentee details",1)
    try:
        print(request.data)
        id = request.data['id']
        # getting the requested mentee details from the table
        mentee = Mentee.objects.raw(f"SELECT id,is_experience,first_name,last_name,languages,role,organization,profile_picture_url,city,is_experience,description,areas_of_interest FROM static_mentee WHERE id={id};")[0]
        
        # urlShortner(mentee.profile_picture_url) # implementing url shortner
        experience = Experience.objects.raw(f"SELECT id,company,from_duration,to_duration FROM static_Experience WHERE referenced_id={mentee.id} and role_type=\'mentee\'")
        experience_list = []
        # iterating through the experience to list it
        for i in experience:
            value = dict()
            value['institution_name'] = i.company
            value['Date'] = {
                'startDate':i.from_duration,
                'endDate':i.to_duration
            }
            experience_list.append(value)
        data = {
            "name":mentee.first_name+" "+mentee.last_name,
            "languages":mentee.languages,
            "location":mentee.city,
            "overview":mentee.description,
            "areas_of_interest":mentee.areas_of_interest,
            "experience":experience_list
        }
        # background languages experience
        log("Mentor details provided sucessfully",1)
        return Response({'data':data},status=STATUSES['SUCCESS'])
    except Exception as e:
        print(e)
        return Response({'message':"Error"})