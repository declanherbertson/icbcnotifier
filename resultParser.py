import json
from constants import POSITION_LOOKUP, DATE_OPTIONS_ALL, DATE_OPTIONS_WEEK, DATE_OPTIONS_MONTH
import myTime

class ResultParser:
  @classmethod
  def get_text(cls, json_value):
    return json.dumps(json_value)

  @classmethod
  def get_json(cls, text, filter_opts=None):
    try:
      json_value = json.loads(text)
      if filter_opts is None:
        return json_value
      date_option = filter_opts.get('date', DATE_OPTIONS_ALL)
      range_option = filter_opts.get('range', None)
      if range_option is not None:
        r1, r2 = range_option.split(':')[1:]
        # print(f'comparing {r1} and {r2} to {[v["appointmentDt"]["date"] for v in json_value if v["appointmentDt"]["date"] >= r1 and v["appointmentDt"]["date"] <= r2]}')
        return [v for v in json_value if v['appointmentDt']['date'] >= r1 and v['appointmentDt']['date'] <= r2]
      elif date_option == DATE_OPTIONS_ALL:
        return json_value
      elif date_option == DATE_OPTIONS_WEEK:
        return [v for v in json_value if myTime.timeDeltaInDays(v['appointmentDt']['date']) <= 7]
      elif date_option == DATE_OPTIONS_MONTH:
        return [v for v in json_value if myTime.timeDeltaInDays(v['appointmentDt']['date']) <= 31]
      else:
        raise ValueError('Invalid date option')
    except:
      return []

  @classmethod
  def get_num_appointments(cls, text, filter_opts=None):
    appointmentJson = cls.get_json(text, filter_opts)
    return len(appointmentJson)
  
  @classmethod
  def get_available_times(cls, text, filter_opts=None):
    json_value = cls.get_json(text, filter_opts)
    return [f"{v['appointmentDt']['dayOfWeek'][:3]} {v['appointmentDt']['date']}, {v['startTm']}-{v['endTm']} at {POSITION_LOOKUP[v['posId']]}" for v in json_value]


if __name__ == "__main__":
  from test import TEST_TEXT
  print(ResultParser.get_num_appointments(TEST_TEXT))
  print('\n'.join(ResultParser.get_available_times(TEST_TEXT)))
  