#!/usr/bin/env python3
import os, sys
import requests

user = os.getenv('USER')
text_source = '{}/supplier-data/descriptions/'.format(user)
fruit_url = 'http://'+ip_address+'/fruits/'

for file in os.listdir(text_source):
	fruitlist = {}
	text_file = os.path.join(text_source,file)
	with open(text_file,'r') as txt_dl:
		lines = txt_dl.readlines()
		fruitlist["name"] = lines[0].strip('\n')
		fruitlist["weight"] = lines[1].strip('\n').strip("lbs")
		fruitlist["description"] = lines[2].strip('\n')
		fruitlist["image_name"] = os.path.splitext(file)[0]+'.jpeg'
	response = requests.post(fruit_url, json=fruitlist)
	response.raise_for_status()