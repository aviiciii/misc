import re
import smtplib
import dns.resolver
import socket
import sys


def validate(email_address):
	# https://stackoverflow.com/questions/22233848/how-to-verify-an-email-address-in-python-using-smtplib
	
	#Step 1: Check email
	#Check using Regex that an email meets minimum requirements, throw an error if not
	addressToVerify = email_address

	#Step 2: Getting MX record
	#Pull domain name from email address
	domain_name = email_address.split('@')[1]

	#get the MX record for the domain
	records = dns.resolver.resolve(domain_name, 'MX')
	mxRecord = records[0].exchange
	mxRecord = str(mxRecord)

	#Step 3: ping email server
	#check if the email address exists

	# Get local server hostname
	host = socket.gethostname()

	# SMTP lib setup (use debug level for full output)
	server = smtplib.SMTP()
	server.set_debuglevel(0)

	# SMTP Conversation
	server.connect(mxRecord)
	server.helo(host)
	server.mail('me@domain.com')
	code, message = server.rcpt(str(addressToVerify))
	server.quit()

	# Assume 250 as Success
	if code == 250:
		return True
	else:
		return False


print(validate('sec20cs999@sairamtap.edu.in'))


