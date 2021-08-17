from notify import Notify
from resultParser import ResultParser
from constants import DATE_OPTIONS_ALL, DATE_OPTIONS_WEEK, DATE_OPTIONS_MONTH, POSITION_LOOKUP
from myEmail import Email

"""
user_map structure should look like the following:

{
  <location_id>: {
    'week': [<user email>],

    'month': [<user email>],

    'all': [<user email>]
  }
}

structured so that we can batch the emails to all users
Time complexity to build if assuming location_ids and date options are constant is O(len(users))
Time complexity to send emails given a location id is O(len(date options))
"""

class NotifyController:
  def __init__(self, logger):
    self.logger = logger
    self.notify = Notify()
    self._update_maps(*self.notify.get_users())

  def _update_maps(self, users, refetched):
    if not refetched:
      return
    user_map = {}
    for user in users:
      for location in user['locations']:
        if location not in user_map:
          user_map[location] = {}
        if user['date'] not in user_map[location]:
          user_map[location][user['date']] = []
        user_map[location][user['date']].append(user['email'])
    self.user_map = user_map

  
  def notify_users(self, loc_id, appointment_text):
    self._update_maps(*self.notify.get_users())
    for date_option in self.user_map[str(loc_id)]:
      filtered_appointments_text = ResultParser.get_text(ResultParser.get_json(appointment_text, { 'date': date_option }))
      if ResultParser.get_num_appointments(filtered_appointments_text) > 0 and len(self.user_map[loc_id][date_option]) > 0:
        self.logger.log(f"notifying users {self.user_map[loc_id][date_option]} for option {date_option} at loc {loc_id}")
        Email.appointment_message(
          self.user_map[loc_id][date_option],
          f"ICBC Appointments Available at {POSITION_LOOKUP[int(loc_id)]}",
          filtered_appointments_text
        )

if __name__ == "__main__":
  from test import TEST_TEXT
  from logger import Logger
  n = NotifyController(Logger('test'))
  n.notify_users('9', TEST_TEXT)
