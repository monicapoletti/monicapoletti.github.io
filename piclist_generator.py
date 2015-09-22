#!/usr/bin/python

import sys
import os

# Set up input path and file to write output
album = sys.argv[1]
input_path = "albums/" + album
f = open(sys.argv[1] + "_piclist.txt", "w")

# Get list of items (photos) in directory specified by input path
pic_list = os.listdir(input_path)

# Write the line for each photo to a text file
# Can use this list to create a new album's html page
for pic in pic_list:
	if pic != ".DS_Store":
		f.write("<li><a href=\"" + input_path + "/" + pic + "\" " 
		"title=\"\"><img src=\"" + input_path + "/" + pic + "\" " 
		"alt=\"\"></a></li>\n\n")