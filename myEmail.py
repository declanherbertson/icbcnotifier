import smtplib
import ssl
import private

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
      """ % (private.SENDER_EMAIL, ", ".join(to), subject, text)

      server.sendmail(private.SENDER_EMAIL, to, email_text)
  
if __name__ == "__main__":
  Email.message(private.RECEIVER_EMAILS, "Test", "Hello World!")