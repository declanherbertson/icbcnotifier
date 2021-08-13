import myTime

class Logger:
  def __init__(self, log_name):
    self.log_name = log_name

  def log(self, message):
    with open(f"{self.log_name}.txt", "a") as file:
      file.write(f"{myTime.timestamp()} :: {message}\n")
      