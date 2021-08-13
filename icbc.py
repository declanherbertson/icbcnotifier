import myTime, constants, private
from api import get_bearer_token, get_available_appointments
from myEmail import Email
import time
from logger import Logger
from resultParser import ResultParser

def main():
  overview_logger = Logger(myTime.ymd_format(myTime.now()))
  details_logger = Logger(f"details-{myTime.ymd_format(myTime.now())}")
  last_count = 0
  bearer_token = ''
  while (True):
    code, reason, text = get_available_appointments(bearer_token)
    if code == 403:
      overview_logger.log("Refresh Login")
      bearer_token = get_bearer_token()
    elif code == 200:
      count = ResultParser.get_num_appointments(text)
      overview_logger.log(f"Appointments Available: {count}")
      if count > last_count:
        details_logger.log(text)
        Email.message(private.RECEIVER_EMAILS, "ICBC Appointments Available", text)
      last_count = count
    else:
      overview_logger.log(f"Unknown Error, status: {code}, reason: {reason}")
      exit()

    time.sleep(constants.SLEEP_TIME)
  
if __name__ == "__main__":
  main()
