#!/usr/bin/env python3
import psutil
import shutil
import socket
import os
import emails

sender = automation@example.com
recipient = '{}@example.com'.format(os.environ.get('USER'))
body = 'Please check your system and resolve the issue as soon as possible.'

def CPU_Usage():
	if psutil.cpu_percent > 80:
		subject = 'Error - CPU usage is over 80%'
		email_warning(subject)

def Disk_Usage():
	disk_usage = shutil.disk_usage('/')
	disk_total = disk_usage.total
	disk_used = disk_usage.used
	disk_available = disk_used/disk_total * 100
	if disk_available < 20:
		subject = 'Available disk space is lower than 20%'
		email_warning(subject)
		
def Mem_Usage():
	threshold = 500 * 1024 * 1024 #500 mb
	if psutil.virtualmemory.available < threshold:
		subject = 'Error - Available memory is less than 500MB'
		email_warning(subject)
		
def Host_Res():
	local_host_ip = socket.gethostbyname('localhost')
	if local_host_ip != '127.0.0.1':
		subject = 'Error - localhost cannot be resolved to 127.0.0.1'
		email_warning(subject)
	
def email_warning(topic):
	message = emails.generate(sender, recipient, subject, body)
	emails.send(message)
	
if __name__ == "__main__":
	CPU_Usage()
	Disk_Usage()
	Mem_Usage
	Host_Res