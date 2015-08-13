import os, glob, shutil

from ExtensionList import *

###
# Setup the source and Destination directories
###


directoryList = {
    "downloadsDir":"~/Downloads",
    "musicDir":"~/Music",
    "videoDir":"~/Videos",
    "pdfDir":"~/Documents/PDFs",
    "ebookDir":"~/Documents/Ebooks",
    "docDir":"~/Documents",
    "installerDir":"~/DEBs",
    "picDir":"~/Pictures",
    "imageDir":"~/ISOs",
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

###
# Function to print the current working directory
###
def printCwd():
    print('Current working directory: ' + os.getcwd())


###
# Print underlines
###
def printUnderlines(delimiter, length):
    print("\t"+delimiter * length)


###
# Function to check if a directory exist,
# otherwise create the directory
###
def checkAndCreateDir(dirName):
    if not (os.path.isdir(os.path.join(os.path.expanduser(dirName)))):
        printUnderlines("*",len(os.path.expanduser(dirName)) + 25)
        print("\tDirectory " + os.path.join(os.path.expanduser(dirName)) + " doesnt exists")
        print("\tCreating directory " + os.path.join(os.path.expanduser(dirName)))
        try:
            os.makedirs(os.path.join(os.path.expanduser(dirName)))
            print("\tDirectory created")
        except:
            print("\tUnable to create the directory")
        printUnderlines("*",len(os.path.expanduser(directoryList["downloadsDir"])) + 25)

###
# Print files from the Staging Dictionary
###
def printFileNames():
    for keys in stagingDict.keys():
        if (len(stagingDict[keys]) > 0):
            print(len(stagingDict[keys]), keys + " file(s) found")
            print('*' * (15 + len(keys)))
            for files in stagingDict[keys]:
                print(files)
            print("\n")

def moveFiles(dirName):
    for keys in stagingDict.keys():
        if(len(stagingDict[keys])>0):
            for files in stagingDict[keys]:
                try:
                    shutil.move(files,os.path.expanduser(dirName))
                    print("File "+files+" moved from "+directoryList["downloadsDir"]+" to "+os.path.expanduser(dirName))
                except:
                    print("Unable to move file "+files+" from "+directoryList["downloadsDir"]+" to "+os.path.expanduser(dirName))
            print("\n")


###
# Print various Directories
###
# printCwd()
# print("\n")
# print('Home directory: ' + os.path.expanduser('~'))
# print("Downloads Directory: " + os.path.join(os.path.expanduser(downloadsDir)))
# print("Music Directory: " + os.path.join(os.path.expanduser(musicDir)))
# checkAndCreateDir(musicDir)
# print("Videos Directory: " + os.path.join(os.path.expanduser(videoDir)))
# checkAndCreateDir(videoDir)
# print("PDFs Directory: " + os.path.join(os.path.expanduser(pdfDir)))
# checkAndCreateDir(pdfDir)
# print("EBooks Directory: " + os.path.join(os.path.expanduser(ebookDir)))
# checkAndCreateDir(ebookDir)
# print("Documents Directory: " + os.path.join(os.path.expanduser(docDir)))
# checkAndCreateDir(docDir)
# print("Installers Directory: " + os.path.join(os.path.expanduser(installerDir)))
# checkAndCreateDir(installerDir)
# print("\n")

def printDirs():
    for dirType in directoryList.keys():
        print(dirType+": \t"+directoryList[dirType])
        checkAndCreateDir(directoryList[dirType])

###
# Switch to the Downloads directory
###
os.chdir(os.path.join(os.path.expanduser(directoryList["downloadsDir"])))
printCwd()
print("\n")
printDirs()
print("\n")

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
