import json
from constants import POSITION_LOOKUP

class ResultParser:
  @classmethod
  def _get_json(cls, text):
    try:
      return json.loads(text)
    except:
      return []

  @classmethod
  def get_num_appointments(cls, text, filterOpts=None):
    appointmentJson = cls._get_json(text)
    if filterOpts is None:
      return len(appointmentJson)
    # TODO add options
    raise NotImplemented("filterOpts not implemented")
  
  @classmethod
  def get_available_times(cls, text):
    json_value = cls._get_json(text)
    return [f"{v['appointmentDt']['dayOfWeek'][:3]} {v['appointmentDt']['date']}, {v['startTm']}-{v['endTm']} at {POSITION_LOOKUP[v['posId']]}" for v in json_value]


if __name__ == "__main__":
  from test import TEST_TEXT
  print(ResultParser.get_num_appointments(TEST_TEXT))
  print('\n'.join(ResultParser.get_available_times(TEST_TEXT)))
  