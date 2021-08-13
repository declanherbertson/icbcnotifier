import requests
import myTime, constants, private

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
  