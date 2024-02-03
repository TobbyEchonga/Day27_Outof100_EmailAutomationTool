import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpassm

class EmailAutomationTool:
    def __init__(self, smtp_server, smtp_port, sender_email):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email

    def send_email(self, to_email, subject, body):
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = to_email
        message['Subject'] = subject

        # Attach the body as plain text
        message.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                # Log in to the email server
                server.starttls()
                sender_password = getpass(prompt=f"Enter password for {self.sender_email}: ")
                server.login(self.sender_email, sender_password)

                # Send the email
                server.sendmail(self.sender_email, to_email, message.as_string())

            print("Email sent successfully.")

        except Exception as e:
            print(f"Error: {e}")

def main():
    # Replace with your SMTP server details and sender email
    smtp_server = 'your_smtp_server'
    smtp_port = 587
    sender_email = 'your_sender_email@example.com'

    # Create an instance of the EmailAutomationTool
    email_tool = EmailAutomationTool(smtp_server, smtp_port, sender_email)

    # Input: Recipient email, subject, and body
    to_email = input("Enter recipient email: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")

    # Send the email
    email_tool.send_email(to_email, subject, body)

if __name__ == "__main__":
    main()
