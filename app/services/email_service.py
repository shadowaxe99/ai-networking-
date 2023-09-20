
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailService:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = smtplib.SMTP('smtp.gmail.com', 587)

    def send_email(self, to_email, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        self.server.starttls()
        self.server.login(self.email, self.password)
        text = msg.as_string()
        self.server.sendmail(self.email, to_email, text)
        self.server.quit()
