import smtplib

def send_emails(emails, schedule, forecast):
	# Connect to the SMTP server
	server = smtplib.SMTP('smtp.gmail.com', '587')

	# Start TLS encryption
	server.starttls()

	# Login
	password = input("What's your password?")
	from_email = "username@gmail.com"
	server.login(from_email, password)

	# Send to entire email list
	for to_email, name in emails.items():
		message = 'Subject: Welcome to the Circus!\n'
		message += 'Hi ' + name + ',\n\n'
		message += schedule + '\n\n'
		message += forecast
		message += '\n\nHope to see you there'
		server.sendmail(from_email, from_email, message)

	server.quit()