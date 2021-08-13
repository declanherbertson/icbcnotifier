import smtplib
import ssl
import private
from resultParser import ResultParser

class Email:
  @staticmethod
  def message(to, subject, text):
    port = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
      server.login(private.SENDER_EMAIL, private.EMAIL_PASSWORD)

      email_text = """\
From: %s
To: %s
Subject: %s

%s
      """ % (private.SENDER_EMAIL, ", ".join(to), subject, Email.build_body(text))

      server.sendmail(private.SENDER_EMAIL, to, email_text)

  @staticmethod
  def build_body(text):
    count = ResultParser.get_num_appointments(text)
    dates = ResultParser.get_available_times(text)
    nl = "\n"

    return f"There are {count} appointments available.{nl}{nl.join(dates)}"


  
if __name__ == "__main__":
  from test import TEST_TEXT
  Email.message(private.RECEIVER_EMAILS, "Test", TEST_TEXT)
