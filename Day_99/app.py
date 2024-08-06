from dotenv import load_dotenv #type:ignore
import scraper
import os
import time
import schedule #type:ignore
import smtplib
from email.mime.multipart import MIMEMultipart # Import the mime library to create multipart messages
from email.mime.text import MIMEText # Import the mime library to create text messages

load_dotenv()
psw = os.getenv("psw")
username = os.getenv("username")

def getMail():
    email = "Latest Replit Events"
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host = server, port = port)
    s.starttls()
    s.login(username, psw)

    msg = MIMEMultipart() # Creates the message
    msg['To'] = username
    msg['From'] = username
    msg['Subject'] = scraper.scrape()
    msg.attach(MIMEText(email, 'html')) # Attaches the email content to the message as html
    s.send_message(msg)
    del msg # Deletes the message from memory
    s.quit()

schedule.every(24).hours.do(getMail)

while True:
    schedule.run_pending()
    time.sleep(1)