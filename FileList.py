# Program:  FileList.py
# This program will prompt a user to select a directory and will create a csv file in that directory with a list of all files in that directory as well as all children directories

import Tkinter
from tkFileDialog   import askdirectory
import os
import datetime

# Get the Directory to search
def UsersDirectory():
	gui = Tkinter.Tk()
	rootDir = askdirectory()
	# print "you entered this path: " + rootDir
	gui.destroy()
	return rootDir

def CreateDirList(rootDir):
	# rootDir is returned from the user's selection

	# create (if it doesn't exist) a .csv to hold the list.  Open it and create the first row headers.
	iWarnings = 0
	iErrors = 0
	ofPath = rootDir + '\\' + 'ListofFiles.csv'
	of = open(ofPath, 'w')
	entry = str('FullName' + ',' + 'Directory' + ',' + 'FileName' + ',' + 'Extension' + ',' + 'Size(Bytes)' + ',' + 'Owner' + ',' + 'LastModified' + ',' + 'LastAccessed' + '\n')
	of.write(entry)

	# Loop thru directory and return the API's parameters
	for dirName, subdirList, fileList in os.walk(rootDir):

		# Loop thru the files in a directory, ofrmat the data to be captured and write a row to the .csv
		for fname in fileList:
			# print ('\t%s' % fname)
			fileFullName = dirName + '\\' + fname
			# retrieve meta data about file using OS.Stat method
			fileStats = os.stat(fileFullName)
			fsize = fileStats.st_size
			fOwner = fileStats.st_uid
			# convert long date format into formatted date string
			sMod = datetime.datetime.fromtimestamp(fileStats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
			sAccess = datetime.datetime.fromtimestamp(fileStats.st_atime).strftime('%Y-%m-%d %H:%M:%S')

			if fileFullName.find(',')> -1:
				fileFullName.replace(',', '-')
				print ('**** Changed comma to dash for ' + fileFullName)

			tmpname, fextension = os.path.splitext(fileFullName)

			try:
				entry = str(fileFullName + ',' + dirName + ',' + fname + ',' + fextension + ',' + str(fsize) + ',' + str(fOwner) + ',' + sAccess + ',' + sMod + '\n')
				print (entry)
				of.write(entry)
			except UnicodeEncodeError:
				print ("***** There was a UnicodeEncodeError error.  Couldn\'t write this file to listing *****")
				of.write('***** UnicodeEncodeError *****   *** Missing Entry ***')
				iErrors = iErrors + 1
	of.write("Results:   # of Errors: " + str(iErrors) + ';        # of Warnings: ' + str(iWarnings) + '\n')
	of.close()


# Control the process
CreateDirList(UsersDirectory())

