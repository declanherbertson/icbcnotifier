# TODO send SMS when increase in spots available
import myTime, constants, private
from api import get_bearer_token, get_available_appointments
from myEmail import Email
import time
from logger import Logger
import json

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
      json_value = json.loads(text)
      count = len(json_value)
      overview_logger.log(f"Appointments Available: {count}")
      if count > last_count:
        details_logger.log(text)
        Email.message(private.RECEIVER_EMAILS, "ICBC Appointments Available", f"There are {count} appointments available.")
      last_count = count
    else:
      overview_logger.log(f"Unknown Error, status: {code}, reason: {reason}")
      exit()

    time.sleep(constants.SLEEP_TIME)
  
if __name__ == "__main__":
  main()

