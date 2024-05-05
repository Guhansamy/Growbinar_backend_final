from django.core.mail import send_mail

def sendVerificationMail(url, email_id):
    send_mail(
        subject="Verify your mail by clicking the below link",
        from_email="admin@growbinar.com",
        message='http://localhost:5000/'+url,
        recipient_list=[email_id,]
    )
    print("mail sent")