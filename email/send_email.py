import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(toMail, subject, content):

    fromMail= "karaguzeleda1@gmail.com"
    server= smtplib.SMTP("smpt.gmail.com",587)


    server.starttIs()

    server.login(fromMail, "edakaraguzel6@gmail.com")

    message = MIMEMultipart('alternative')
    message['Subject']= subject 

    htmlContent =  MIMEText(content, 'html')
    message.attach(htmlContent)

    server.sendmail(
       fromMail,
       toMail,
       message.as_string()

    )
    print("Eposta gonderildi!")

    server.quit()
