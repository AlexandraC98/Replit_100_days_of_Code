from dotenv import load_dotenv #type:ignore
import os
import time
import schedule #type:ignore
import smtplib
from email.mime.multipart import MIMEMultipart # Import the mime library to create multipart messages
from email.mime.text import MIMEText # Import the mime library to create text messages
import quotes

load_dotenv()
psw = os.getenv("psw")
username = os.getenv("username")


def sendMail():
    email = "Quote of the day"
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host = server, port = port) # Creates the server connection using the host and port details
    s.starttls() # Sets the encryption mode
    s.login(username, psw) # Logs into the email server

    msg = MIMEMultipart() # Creates the message
    msg['To'] = username
    msg['From'] = username
    msg['Subject'] = quotes.getQuote() # Sets the subject of the message
    msg.attach(MIMEText(email, 'html')) # Attaches the email content to the message as html
    s.send_message(msg) # Sends the message
    del msg # Deletes the message from memory
    s.quit()


schedule.every(24).hours.do(sendMail)

while True:
    schedule.run_pending()
    time.sleep(1)