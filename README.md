# Send Email with Attachment in Python  

This Python script sends an email with an attachment (like an image or PDF) using Gmail’s SMTP server.  
It connects securely, logs in with your Gmail App Password, and sends your file to the receiver.  

##  How It Works  
1. Import required modules:  
   - ssl → For secure connection  
   - smtplib → Send email via SMTP  
   - EmailMessage → Create and format email  
   - mimetypes → Detect file type automatically  

2. Create an email object and set:  
   - From, To, Subject, Content  

3. Read and attach the file:  
   - Detects type (image/pdf/etc.)  
   - Attaches it properly  

4. Connect and send:  
   - Uses Gmail’s SMTP server with SSL (smtp.gmail.com, port 465)  
   - Logs in with *App Password*  
   - Sends the email  


## Additional information
* Provide the email id of the sender
* Provide the email id of the receiver
* Done 2-step verification in senders mail
* Make app password in google app password and use this password 
