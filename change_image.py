#!/usr/bin/env python3
import os, sys
from PIL import image

source_path = 'supplier-data/images/'
size = '(600,400)' #Some reason this didn't work as a variable - check later
format = 'JPEG'

for pic in os.listdir(source_path):
  if pic.endswith('.tiff'):
    f, e = os.path.splitext(pic)
	image_path = source_path + pic
	outfile = source_path+f+'.jpeg'
	with Image.open(image_path) as img:
	  img.convert('RGB').resize((600,400)).save(outfile,format)
	img.close()