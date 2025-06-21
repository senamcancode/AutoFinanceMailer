from email.encoders import encode_base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
import smtplib
import os
import logging
from src.utils.email_config import gmail_pass, user, host, port

def send_email_w_report_attachment(receiver, _from, subject, body, filename):
    message = MIMEMultipart()

    message['To'] = Header(receiver)
    message['From'] = Header(_from)
    message['Subject'] = Header(subject)

    message.attach(MIMEText(body, 'plain', 'utf-8'))

    attachment_name = os.path.basename(filename)
    opened_file = open(filename, 'rb')
    attachment = MIMEApplication(opened_file.read(), _subtype="pdf", _encoder = encode_base64)
    opened_file.close()
    attachment.add_header('Content-Disposition', 'attachment', filename=attachment_name)
    message.attach(attachment)


    try:
        server = smtplib.SMTP_SSL(host, port)
        server.login(user, gmail_pass)
        server.sendmail(_from, receiver, message.as_string())
        server.quit()

        return attachment_name

    except smtplib.SMTPException as e:
        logging.error(f"SMTP error while sending email: {e}")
        raise 