import os
import re

directory = raw_input('Enter a directory address: \n')
toreplace = raw_input("enter the pattern to remove:\n")
foldercheck = raw_input("Do you want to remove this pattern from folder also? Y/N ?\n")

def remov(strn):
    for f in os.listdir(strn) :
        print (f)
        prevpathname = (strn)
        pathname = os.path.join(strn, f)
        os.chdir(strn)
        if( not os.path.isdir(pathname)) :           
            if(toreplace in f):
                print(pathname)
                name1 = f.replace(toreplace, "")
                print ("old name: "+ f + "\nnew name:\n" + name1)
                os.rename(f,name1)
        else :
            print("current path:\n"+ pathname)
            os.chdir(pathname)
            remov(pathname)
            print("changing path back to:\n"+ prevpathname)
            os.chdir(prevpathname)

        if(foldercheck == "Y"):
            if(os.path.isdir(pathname)):
                if(toreplace in f):
                    print(pathname)
                    name1 = f.replace(toreplace, "")
                    print ("old name: "+ f + "new name:" + name1 + "\n")
                    os.rename(f,name1)

            
remov(directory)
