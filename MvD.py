import os, glob

###
# Setup the source and Destination directories
###
downloadsDir = "~/Downloads"
musicDir = "~/Music"
videoDir = "~/Videos"
pdfDir = "~/Documents/PDFs"
ebookDir = "~/Documents/Ebooks"
docDir = "~/Documents"
installerDir = "~/DEBs"

###
# Lists of popular file extensions
###
installerList = [
    "deb",
    "run",
    "exe",
    "rpm"
]

pdfList = [
    "pdf",
    "xps",
]

musicList = [
    "mp3",
    "aac",
    "wma",
    "ogg"
]

videoList = [
    "wmv",
    "mp4",
    "flv"
]

ebookList = [
    "epub",
    "awz3",
    "mobi"
]

docList = [
    "doc",
    "docx",
    "odt",
    "ppt",
    "pptx",
    "xls",
    "xlsx"
]

###
# List of files to run this program for
###

runForList = {
    "installerFiles":[i for i in installerList],
    "pdfFiles":[i for i in pdfList],
    "musicFiles":[i for i in musicList],
    "videoFiles":[i for i in videoList],
    "ebookFiles":[i for i in ebookList],
    "docFiles":[i for i in docList]
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
        except:
            print("\tUnable to create the directory")
        finally:
            print("\tDirectory created")
        printUnderlines("*",len(os.path.expanduser(downloadsDir)) + 25)

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


###
# Print various Directories
###
printCwd()
print("\n")
print('Home directory: ' + os.path.expanduser('~'))
print("Downloads Directory: " + os.path.join(os.path.expanduser(downloadsDir)))
print("Music Directory: " + os.path.join(os.path.expanduser(musicDir)))
checkAndCreateDir(musicDir)
print("Videos Directory: " + os.path.join(os.path.expanduser(videoDir)))
checkAndCreateDir(videoDir)
print("PDFs Directory: " + os.path.join(os.path.expanduser(pdfDir)))
checkAndCreateDir(pdfDir)
print("EBooks Directory: " + os.path.join(os.path.expanduser(ebookDir)))
checkAndCreateDir(ebookDir)
print("Documents Directory: " + os.path.join(os.path.expanduser(docDir)))
checkAndCreateDir(docDir)
print("Installers Directory: " + os.path.join(os.path.expanduser(installerDir)))
checkAndCreateDir(installerDir)
print("\n")

###
# Switch to the Downloads directory
###
os.chdir(os.path.join(os.path.expanduser(downloadsDir)))
printCwd()
print("\n")


for fileType in runForList.keys():
    ###
    # Temporary dictionary to store the file names
    ###
    stagingDict = {}
    ###
    # Prepare lists of different installer files
    ###
    for fileType in runForList[fileType]:
        stagingDict[fileType] = glob.glob("*." + fileType)
    printFileNames()


# ###
# # Temporary dictionary to store the file names
# ###
# stagingDict = {}
# ###
# # Prepare lists of different PDF/XPS files
# ###
# for pdfFiles in pdfList:
#     stagingDict[pdfFiles] = glob.glob("*." + pdfFiles)
# printFileNames()
#
#
# ###
# # Temporary dictionary to store the file names
# ###
# stagingDict = {}
# ###
# # Prepare lists of different PDF/XPS files
# ###
# for videoFiles in videoList:
#     stagingDict[videoFiles] = glob.glob("*." + videoFiles)
# printFileNames()
#
#
# ###
# # Temporary dictionary to store the file names
# ###
# stagingDict = {}
# ###
# # Prepare lists of different PDF/XPS files
# ###
# for ebookFiles in ebookList:
#     stagingDict[ebookFiles] = glob.glob("*." + ebookFiles)
# printFileNames()
#
# ###
# # Temporary dictionary to store the file names
# ###
# stagingDict = {}
# ###
# # Prepare lists of different PDF/XPS files
# ###
# for musicFiles in musicList:
#     stagingDict[musicFiles] = glob.glob("*." + musicFiles)
# printFileNames()
#
# ###
# # Temporary dictionary to store the file names
# ###
# stagingDict = {}
# ###
# # Prepare lists of different PDF/XPS files
# ###
# for docFiles in docList:
#     stagingDict[docFiles] = glob.glob("*." + docFiles)
# printFileNames()

