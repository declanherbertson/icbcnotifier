import smtplib
import ssl
import private
from resultParser import ResultParser

class Email:
  @staticmethod 
  def message(to, subject, formatted_body):
    port = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
      server.login(private.SENDER_EMAIL, private.EMAIL_PASSWORD)

      email_text = """\
From: %s
Subject: %s

%s
      """ % (private.SENDER_EMAIL, subject, formatted_body)

      server.sendmail(private.SENDER_EMAIL, to, email_text)

  @staticmethod
  def appointment_message(to, subject, text):
    Email.message(to, subject, Email.build_body(text))
  
  @staticmethod
  def admin_alert(subject, message):
    Email.message(private.ADMIN_EMAILS, subject, message)

  @staticmethod
  def build_body(text):
    count = ResultParser.get_num_appointments(text)
    dates = ResultParser.get_available_times(text)
    nl = "\n"

    return f"There are {count} appointments available.{nl}{nl.join(dates)}"
  
if __name__ == "__main__":
  from test import TEST_TEXT
  Email.appointment_message(private.ADMIN_EMAILS, "Test", TEST_TEXT)
  Email.admin_alert("Service failed", "service threw a 500 and exited.")
