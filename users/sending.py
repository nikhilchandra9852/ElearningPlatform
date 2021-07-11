import smtplib,ssl
from email.mime.text import MIMEText


smtp_server = 'smtp.gmail.com'
port =465
sender_email = "elearningvrsec@gmail.com"
password = "vrsec2000"


def sendmail(email):

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server,port,context = context) as server:
		server.login(sender_email,password)
		msg = MIMEText("Your are registered to elearning email")
		msg['Subject']= 'elearning_vrsec'
		msg['From'] = sender_email
		msg['To']=email

		server.sendmail(sender_email,email,msg.as_string())
def sendingmarks(email,branch,marks):
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server,port,context = context) as server:
		server.login(sender_email,password)
		msg = MIMEText("You scored {0} in branch {1}".format(marks,branch))
		msg['Subject']= 'elearning_vrsec'
		msg['From'] = sender_email
		msg['To']=email
		server.sendmail(sender_email,email,msg.as_string())