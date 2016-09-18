import weather
import mailer

def get_emails():
	# Reading emails from files
	emails = {}
	try:
		email_file = open('emails2.txt', 'r')

		for line in email_file:
			(email, name) = line.split(',')
			emails[email] = name.strip()

	except FileNotFoundError as err:
		print(err)

	return emails
	email_file.close()

def get_schedule():
	# Reading schedules from our files
	try:
		schedule_file = open('schedule.txt', 'r')

		schedule = schedule_file.read()
	except FileNotFoundError as err:
		print(err)

	return schedule
	schedule_file.close()

def main():
	emails = get_emails()
	schedule = get_schedule()
	forecast = weather.get_weather_forecast()
	mailer.send_emails(emails, schedule, forecast)

main()