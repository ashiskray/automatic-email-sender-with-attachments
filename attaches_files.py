import ssl
import smtplib 
from email.message import EmailMessage
import mimetypes 

email=EmailMessage()

subject="lets look at this beautifull image"
email.set_content(subject)

file_path=r"wallpapers.png"  #path of the file 

with open (file_path,"rb") as f:
    file_data=f.read()
    file_name=f.name
    mime_type,_=mimetypes.guess_type(file_path)
    maintype,subtype=mime_type.split('/')
email.add_attachment(file_data,maintype=maintype,subtype=subtype,filename=file_name)

sender_email="sendermail@gmail.com"     # keep your mail id here 
receiver_email="receivermail@gmail.com"  # receiver mail here
app_password="abcdefghgfel"              #password here

email['from']=sender_email
email['to']=receiver_email
email['subject']=subject

context= ssl.create_default_context() 
with smtplib.SMTP_SSL("smtp.gmail.com",465,context =context) as smtp :
    smtp.login(sender_email,app_password)
    smtp.send_message(email)

print ("done brooooo") 
