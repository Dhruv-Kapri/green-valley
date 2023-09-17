from email.message import EmailMessage
import ssl
import smtplib



def email_send(name, email, event_name, event_date, event_time, event_location, event_detail, organiser_contact):
    email_sender = 'greenvalley.events.2022@gmail.com'
    email_password = 'hgxdujejmlxpdpwf'
    email_reciever = email
    
    
    subject = 'Registration succesfull'
    body = """

Hello {},

Thankyou for registering for the event {}. We at GreenValley are focused on working on 
solving major environment related issues by hosting events and meetups to spread more 
awareness and to perform tasks to keep our environment clean and green.

We really appreciate your time and efforts to help us contribute and achieve our 
objective to save our environment.
Below are the details of the event you have registered for:

1. Name                 : {}
2. Location             : {}
3. Date                 : {}
4. Time                 : {}
5. Details              : {}
6. Organiser Contact    : {}

See ya soon on {} date.

Regards 
GreenValley
""".format(name, event_name, event_name, event_location, event_date, event_time, event_detail, organiser_contact, event_date)
    
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body)
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context ) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())