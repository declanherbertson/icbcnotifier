# TODO send SMS when increase in spots available
import requests
import myTime, constants, private
import time
from logger import Logger
import json

APPOINTMENTS_ENDPOINT = "https://onlinebusiness.icbc.com/deas-api/v1/web/getAvailableAppointments"
LOGIN_ENDPOINT = "https://onlinebusiness.icbc.com/deas-api/v1/webLogin/webLogin"

LOGIN_JSON = {
  "drvrLastName": private.drvrLastName,
  "licenceNumber": private.licenceNumber,
  "keyword": private.keyword
}

def get_appointment_json():
  return {
    "aPosID": constants.aPosID,
    "examType": constants.examType,
    "examDate": myTime.ymd_format(myTime.tomorrow()),
    "ignoreReserveTime": constants.ignoreReserveTime,
    "prfDaysOfWeek": constants.prfDaysOfWeek,
    "prfPartsOfDay": constants.prfPartsOfDay,
    "lastName": private.lastName,
    "licenseNumber": private.licenceNumber
  }

def get_available_appointments(bearer_token):
  r = requests.post(APPOINTMENTS_ENDPOINT, json=get_appointment_json(), headers={
    "Authorization": bearer_token
  })
  return r.status_code, r.reason, r.text

def get_bearer_token():
  r = requests.put(LOGIN_ENDPOINT, json=LOGIN_JSON)
  bearer_token = r.headers["Authorization"]
  return bearer_token

def main():
  overview_logger = Logger(myTime.ymd_format(myTime.now()))
  details_logger = Logger(f"details-{myTime.ymd_format(myTime.now())}")
  bearer_token = ''
  while (True):
    code, reason, text = get_available_appointments(bearer_token)
    if code == 403:
      overview_logger.log("Refresh Login")
      bearer_token = get_bearer_token()
    elif code == 200:
      json_value = json.loads(text)
      overview_logger.log(f"Appointments Available: {len(json_value)}")
      if len(json_value) != 0:
        details_logger.log(text)
    else:
      overview_logger.log(f"Unknown Error, status: {code}, reason: {reason}")
      exit()

    time.sleep(constants.SLEEP_TIME)
  
if __name__ == "__main__":
  main()

