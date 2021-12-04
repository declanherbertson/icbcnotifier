# TITLE
Notifier Bot For ICBC Road Tests

# USAGE
1) Setup SQLITE3 database with db.py (you can change the populate dummy data to populate your own email / email -> phone number value ie '<number>@msg.telus.com')
2) create private.py
define the following values:
For authentication purposes
- lastName -> string (all caps),
- drvrLastName -> string (first letter cap),
- licenceNumber -> string (drivers licence number), 
- keyword -> string (security keyword ie mothers maiden name)

For admininstration purposes
- SENDER_EMAIL -> string (email messages will be sent from)
- EMAIL_PASSWORD -> string (password for email, if google mail you will need to enable app passwords)
- ADMIN_EMAILS -> [string] (email it sends logistics and errors to)

3) configure which location and type of test you want to be notified for in constants.py via aPosId (location), ExamType and APPOINTMENT_RANGE
4) run via 'python3 icbc.py'
  
  
# FUTURE PLANS
work on scalabilty aspect so that emails can be sent out to multiple different users with different preferences efficently. Part of the work is on the scalability branch and some design choices such as using a database for recipient emails and the ResultsParser stem from that goal.
