'''
List all files present in the directory recursively with last date modified
'''

import os
import datetime

directory = input('Enter a directory address: \n')
foldercheck = input("Do you want to print folder contents also? Y/N ?\n")
log = open("log.txt", "w")


def listing(strn):
    for files in os.listdir(strn):
        #print (f, datetime.datetime.fromtimestamp(os.path.getmtime(f)))
        pathname = os.path.join(strn, files)
        prevpathname = (strn)
        os.chdir(strn)
        if os.path.isfile(pathname):
            log.write (str(pathname) + "\t last modified:\t" + str(datetime.datetime.fromtimestamp(os.path.getmtime(pathname))) + "\n")
        if foldercheck == "Y":
            if os.path.isdir(pathname):
                log.write(str(pathname) +  "\tlast modified:\t" + str(datetime.datetime.fromtimestamp(os.path.getmtime(pathname))) + "\n")
        if os.path.isdir(pathname):
            #print("current path:\n"+ pathname)
            os.chdir(pathname)
            listing(pathname)
            #print("changing path back to:\n"+ prevpathname)
            os.chdir(prevpathname)


listing(directory)
