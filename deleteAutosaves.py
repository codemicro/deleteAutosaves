import os
from datetime import datetime
import configparser
import sys
import subprocess

def check(key):
    try:
        config["paths"][key]
        return True
    except:
        return False

# this reads the configuration file
config = configparser.ConfigParser()
config.read("settings.ini")

logging = {"0":False, "1":True}[config["DEFAULT"]["logging"]]

# this loads the things to search from the configuration file
keys = config["DEFAULT"]["keys"].split(",")

# works out the number if dir.x entries in the config file
result = False
i = 0
while not result:
    i += 1
    string = "dir." + str(i)
    if not check(string):
        result = True

files = []

# makes an list of all the files in all the directories
for ii in range(1, i):
    path = config["paths"]["dir." + str(ii)]
    contents = os.listdir(path)
    for item in contents:
        if os.path.isfile(path + item):
            files.append(path + item)

deletion = []

print("Searching files...")

# goes through each item in the list and searches the filename - if it matches one of the keys
# then add it to another list pending erasure.
for item in files:
    allowDeletion = False
    for condition in keys:
        split = item.split("\\")[-1].split(".")
        if split[0].lower().find(condition.lower()) != -1:
            allowDeletion = True
    if allowDeletion:
        deletion.append(item)

# works out the directory the script is being run from
cut = sys.argv[0].split("/")[:-1]
string = ""
for item in cut:
    string = string + item + "/"
logDir = string + "logs/"

# makes a directory within the current script directory called "logs" which will store the logs
if not os.path.exists(logDir):
    os.mkdir(logDir)

# initialises the log file
if logging:
    logFName = logDir + datetime.today().strftime("%d %m %Y-%H %M %S") + ".log"
    open(logFName, "w")
    logF = open(logFName, "a+")
    logF.write("Deletion tool by Tom Pain - " + datetime.today().strftime('%Y-%m-%d %H:%M:%S') + "\n")
    logF.write("Search keys: {}\n\n".format(keys))

print("Deleting files...")

# this is all that deletes files
for file in deletion:
    print("Deleting " + file)
    os.remove(file)
    if logging:
        logF.write("Deleted " + file + "\n")

# writes a final closing bit to the file and shows it to the user.
if logging:
    logF.write("\nFinished. " + str(len(deletion)) + " files deleted.")
    logF.close()
    subArgs = ["notepad", logFName]
    subprocess.Popen(subArgs)

print("\nFinished operation")
