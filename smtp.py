
import smtplib

# Type Your messeage down below in the message section
Message='''From:
To: 
subject:
body:'''

# add your email and gmail application password
gmail_user=""
gamil_app_password=""
sent_from="sender's mail"
sent_to="receivers's mail"
email_text=Message

server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.ehlo()
server.login(gmail_user,gamil_app_password)
server.sendmail(sent_from,sent_to,email_text)
server.close()
print("Successfully sent email")

# voila! the work is done 