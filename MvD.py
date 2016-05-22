import os
import glob
import shutil
import time
from ExtensionList import *

###
# Setup the source and destination directories
###
directoryList = {
	"Logs":"~/Downloads/Logs",
	"downloadsDir":"~/Downloads",
	"musicDir":"~/Music/MvD",
	"videoDir":"~/Videos/MvD",
	"pdfDir":"~/Documents/MvD",
	"ebookDir":"~/Documents/MvD",
	"docDir":"~/Documents",
	"installerDir":"~/Downloads/EXEs",
	"picDir":"~/Pictures/MvD",
	"imageDir":"~/Downloads/ISOs",
	"archiveDir":"~/Downloads/Archives",
	"scriptDir":"~/Downloads/Scripts",
	"TBDDir":"~/Downloads/TBD"
}

###
# List of files to run this program for
###
runForList = {
	"installerFiles":[[i for i in installerList],directoryList["installerDir"]],
	"pdfFiles":[[i for i in pdfList],directoryList["pdfDir"]],
	"musicFiles":[[i for i in musicList],directoryList["musicDir"]],
	"videoFiles":[[i for i in videoList],directoryList["videoDir"]],
	"ebookFiles":[[i for i in ebookList],directoryList["ebookDir"]],
	"docFiles":[[i for i in docList],directoryList["docDir"]],
	"picFiles":[[i for i in picList],directoryList["picDir"]],
	"imageFiles":[[i for i in imageList],directoryList["imageDir"]],
	"archiveFiles": [[i for i in archiveList],directoryList["archiveDir"]],
	"scriptFiles": [[i for i in scriptList],directoryList["scriptDir"]],
	"TBDFiles": [[i for i in TBDList],directoryList["TBDDir"]]
}


def printCwd():
	"""Function to print the current working directory"""
	print('Current working directory: ' + os.getcwd())
	f.write('Current working directory: ' + os.getcwd() + "\n")


def printUnderlines(delimiter, length):
	"""Print underlines"""
	print("\t" + delimiter * length)
	f.write("\t" + delimiter * length + "\n")



def checkAndCreateDir(dirName):
	"""Function to check if a directory exist,
	otherwise create the directory
	"""
	if not (os.path.isdir(os.path.join(os.path.expanduser(dirName)))):
		printUnderlines("*",len(os.path.expanduser(dirName)) + 25)
		print("\tDirectory " + os.path.join(os.path.expanduser(dirName)) + " doesnt exists")
		f.write("\tDirectory " + os.path.join(os.path.expanduser(dirName)) + " doesnt exists" + "\n")
		print("\tCreating directory " + os.path.join(os.path.expanduser(dirName)))
		f.write("\tCreating directory " + os.path.join(os.path.expanduser(dirName)) + "\n")
		try:
			os.makedirs(os.path.join(os.path.expanduser(dirName)))
			print("\tDirectory created")
			f.write("\tDirectory created+\n")
		except:
			print("\tUnable to create the directory")
			f.write("\tUnable to create the directory\n")
		printUnderlines("*",len(os.path.expanduser(directoryList["downloadsDir"])) + 25)
		print(" ")
	else:
		print(" ")
		f.write("\n")


def printFileNames():
	"""Print files from the Staging Dictionary"""
	for keys in stagingDict.keys():
		if (len(stagingDict[keys]) > 0):
			print(str(len(stagingDict[keys])) + " " + keys + " file(s) found")
			f.write(str(len(stagingDict[keys])) + " " + keys + " file(s) found\n")
			print('*' * (15 + len(keys)))
			f.write('*' * (15 + len(keys)) + "\n")
			for files in stagingDict[keys]:
				print(files)
				f.write(files)
			print("\n")
			f.write("\n")

def moveFiles(dirName):
	for keys in stagingDict.keys():
		if(len(stagingDict[keys]) > 0):
			for files in stagingDict[keys]:
				try:
					shutil.move(files,os.path.expanduser(dirName))
					print("File " + files + " moved from " + directoryList["downloadsDir"] + " to " + os.path.expanduser(dirName))
					f.write("File " + files + " moved from " + directoryList["downloadsDir"] + " to " + os.path.expanduser(dirName) + "\n")
				except:
					print("Unable to move file " + files + " from " + directoryList["downloadsDir"] + " to " + os.path.expanduser(dirName))
					f.write("Unable to move file " + files + " from " + directoryList["downloadsDir"] + " to " + os.path.expanduser(dirName) + "\n")
			print("\n")
			f.write("\n")


def printDirs():
	"""Print the various source 
	and target directories
	"""
	for dirType in directoryList.keys():
		maxLength = 50

		print(dirType.ljust(20) + ": " + directoryList[dirType])
		f.write(dirType + ": \t" + directoryList[dirType] + "\n")
		checkAndCreateDir(directoryList[dirType])

###
# Switch to the Downloads directory
###
if not (os.path.isdir(os.path.join(os.path.expanduser(directoryList["Logs"])))):
	try:
		os.makedirs(os.path.join(os.path.expanduser(directoryList["Logs"])))
		print("Logs Directory created")
	except:
		print("Unable to create the Logs directory")

logFile = os.path.join(os.path.expanduser(directoryList["Logs"]),"moveDownloads_" + str(time.time()) + ".log")
f = open(logFile,'w')
print("Logfile name: " + logFile)
f.write("Logfile name: " + logFile + "\n")

os.chdir(os.path.join(os.path.expanduser(directoryList["downloadsDir"])))
printCwd()
print("\n")
f.write("\n")
printDirs()
print("\n")
f.write("\n")

for fileType in runForList.keys():
	###
	# Temporary dictionary to store the file names
	###
	stagingDict = {}
	###
	# Prepare lists of different installer files
	###
	for fileTypes in runForList[fileType][0]:
		stagingDict[fileTypes] = glob.glob("*." + fileTypes)
	printFileNames()
	moveFiles(runForList[fileType][1])