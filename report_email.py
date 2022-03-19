#!/usr/bin/env python3
import os
import datetime
import reports
import emails

def generate_pdf(path):
	pdf = ""
	files = os.listdir(path)
	for file in files:
		if file.endswith(".txt"):
			with open(path+file, 'r') as f:
				lines = f.readlines()
				name = lines[0].strip()
				weight = lines[1].strip()
				pdf += "name: "+name+"<br/>+"weight: "+weight+"<br/><br/>"
	return pdf

if __name__ == "__main__":
	#Report section
	date = datetime.datetime.now().strftime('%Y-%m-%d')
	title = 'Processed Update on '+date
	attachment = '/tmp/processed.pdf'	
	path = 'supplier-data/descriptions/'
	paragraph = generate_pdf(path)
	reports.generate(attachment, title, paragraph)
	
	#Email section
	sender = "automation@example.com"
	recipient = "{}@example.com".format(os.environ.get('USER'))
	subject = "Upload Completed - Online Fruit Store"
	body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
	message = emails.generate(sender, recipient, title, body, attachment)
	emails.send(message)