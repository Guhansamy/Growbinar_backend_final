from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.hashers import make_password

class Mentee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=100)
    profile_picture_url = models.CharField(max_length=200)
    areas_of_interest = ArrayField(models.CharField(max_length=100))
    description = models.TextField()
    role = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    is_experience = models.BooleanField()
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    def __str__(self):
        return str(self.first_name+" "+self.last_name)

class Mentor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture_url = models.CharField(max_length=150)
    areas_of_expertise = ArrayField(models.CharField(max_length=100))
    number_of_likes = models.IntegerField()
    languages = ArrayField(models.CharField(max_length=100))
    MentorExperience = models.FloatField()
    designation = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    is_top_rated = models.BooleanField()
    is_experience = models.BooleanField()
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    def __str__(self):
        return str(self.first_name+" "+self.last_name)
    

class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    from_duration = models.DateTimeField()
    to_duration = models.DateTimeField()
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    role_type = models.CharField(max_length=10, choices=[('mentor', 'Mentor'), ('mentee', 'Mentee')])
    referenced_id = models.IntegerField()
    mentorRef = models.ForeignKey(Mentor, on_delete=models.CASCADE, null=True, blank=True)
    menteeRef = models.ForeignKey(Mentee, on_delete=models.CASCADE, null=True, blank=True)

class Session(models.Model):
    id = models.AutoField(primary_key=True)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    slot_date = models.DateField()
    from_slot_time = models.TimeField()
    to_slot_time = models.TimeField()
    is_booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class RequestedSession(models.Model):
    session = models.OneToOneField(Session, on_delete=models.CASCADE, primary_key=True)
    mentee = models.ForeignKey(Mentee, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)

class BookedSession(models.Model):
    id = models.AutoField(primary_key=True)
    requested_session = models.OneToOneField(RequestedSession, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)

class SessionFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    booked_session = models.OneToOneField(BookedSession, on_delete=models.CASCADE)
    description = models.TextField()
    ratings = models.IntegerField()
    created_at = models.DateTimeField(null=False, auto_now_add=True)
