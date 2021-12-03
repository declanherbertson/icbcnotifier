import myTime, constants
from api import get_bearer_token, get_available_appointments
from myEmail import Email
import time
from logger import Logger
from resultParser import ResultParser
from users import Users

def main():
  overview_logger = Logger(myTime.ymd_format(myTime.now()))
  details_logger = Logger(f"details-{myTime.ymd_format(myTime.now())}")
  error_logger = Logger(f"errors-{myTime.ymd_format(myTime.now())}")
  users = Users()
  last_count = 0
  bearer_token = ''
  while (True):
    code, reason, text = get_available_appointments(bearer_token)
    if code == 403:
      overview_logger.log("Refresh Login")
      bearer_token = get_bearer_token()
    elif code == 200:
      filtered_appointments_text_json = ResultParser.get_json(text, constants.APPOINTMENT_RANGE)
      filtered_appointments_text = ResultParser.get_text(filtered_appointments_text_json)
      count = ResultParser.get_num_appointments(filtered_appointments_text)
      overview_logger.log(f"Appointments Available: {count}")
      if count > last_count:
        details_logger.log(filtered_appointments_text)
        Email.appointment_message(users.get_email_list(), "ICBC Appointments Available", filtered_appointments_text, logger=error_logger)
      last_count = count
    else:
      error_logger.log(f"Unknown Error, status: {code}, reason: {reason}")
      Email.admin_alert("ICBC Notifier Admin Alert : Service Crash", f"status: {code}, reason: {reason}", logger=error_logger)
      exit()

    time.sleep(constants.SLEEP_TIME)
  
if __name__ == "__main__":
  main()
