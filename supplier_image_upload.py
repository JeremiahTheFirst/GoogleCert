#!/usr/bin/env python3
import os, sys
import requests

source_path = 'supplier-data/images/'
url = 'http://localhost/upload/'

for pic in os.listdir(source_path):
	f, e = os.path.splitext(pic)
	if e == '.jpeg':
		with open(source_path + pic, 'rb') as opened:
			r = requests.post(url, files={'file': opened})