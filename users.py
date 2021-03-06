from datetime import datetime
import sqlite3 as sl
CACHE_REFRESH_THRESHOLD = 5

class Users:
  def __init__(self):
    self.con = sl.connect('notifier.db')
    self._refresh_cache()
    self.refetched = False
    self.on_start = True

  def _parse_user(self, user_tuple):
    return {
      'email': user_tuple[1],
    }

  def _refresh_cache(self):
    self.users = self._get_users()
    self.cached_time = datetime.utcnow()
    self.refetched = True

  def _get_users(self):
    with self.con:
      return [self._parse_user(user) for user in self.con.execute("SELECT * FROM USER").fetchall()]

  def get_users(self):
    if (datetime.utcnow() - self.cached_time).seconds > (CACHE_REFRESH_THRESHOLD * 60):
      self._refresh_cache()
      self.refetched = True
    else:
      self.refetched = False
    retval = (self.users, self.on_start or self.refetched)
    self.on_start = False
    return retval

  def get_email_list(self):
    return [user['email'] for user in self.get_users()[0]]
  
if __name__ == "__main__":
  n = Users()
  print(n.get_users())
  print(n.get_users())
  print(n.get_email_list())