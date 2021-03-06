POSITION_LOOKUP = {
  9: 'Point Grey',
  275: 'Kingsway',
  8: 'North Vancouver',
  2: 'Burnaby',
  274: 'Wayburne Drive'
}

DATE_OPTIONS_WEEK = 'week'
DATE_OPTIONS_MONTH = 'month'
DATE_OPTIONS_ALL = 'all'

SLEEP_TIME = 30
# SLEEP_TIME = 5 # Test code

ignoreReserveTime = False
# ignoreReserveTime = True # Test code

examType = "7-R-1"
aPosID = 9
prfDaysOfWeek = "[0,1,2,3,4,5,6]"
prfPartsOfDay = "[0,1]"

# either the form 'range:yyyy-mm-dd:yyyy-mm-dd' or 'date:<DATE_OPTIONS>'
APPOINTMENT_RANGE = f"range:{DATE_OPTIONS_ALL}"
