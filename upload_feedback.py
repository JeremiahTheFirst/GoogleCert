#!/usr/bin/env python3

import os
import requests

fb_path = '/data/feedback'
data_keys = ['title', 'name', 'date', 'feedback']

ip_address = '<enter IP>'
fb_url = 'http://{}/feedback/'.format(ip_address)

def upload_feedback():
  for fb in os.listdir(fb_path):
	fb_file = os.path.join(fb_path, fb)
    fb_data = {}
	with open(fb_file, 'r') as fb_dl:
		lines = fb_dl.readlines()
		
		for fb_key,fb_line in zip(data_keys, lines):
			fb_data.update({fb_key: fb_line})
	
	response = requests.post(fb_url, json=fb_data)
	response.raise_for_status()
	
def main():
	print('Accessing feedback from {}'.format(fb_path))
	upload_feedback()
	
if __name__ == '__main__':
	main()