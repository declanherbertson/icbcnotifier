import datetime
from backports.datetime_fromisoformat import MonkeyPatch
MonkeyPatch.patch_fromisoformat()
import pytz

def ymd_format(d):
  return d.strftime("%Y-%m-%d")

def ymdhm_format(d):
  return d.strftime("%Y-%m-%d-%H-%M")

def now():
  return datetime.datetime.now(pytz.timezone("America/Vancouver"))

def tomorrow():
  return now() + datetime.timedelta(days=1)

def timestamp():
  return ymdhm_format(now())

def timeDeltaInDays(day_str):
  return (now() - datetime.datetime.fromisoformat(day_str).replace(tzinfo=pytz.timezone("America/Vancouver"))).days
  