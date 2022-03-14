#Project for automatic clean the garbage file of folders
from os.path import isdir,join,splitext,getsize,isfile
from os import remove,listdir
import sys
import time


#point to directtory
path = input("The folder you want clean: ")
#file type
garbage_extension = ['.tmp', '.log', '.obj', '.txt', '.jpg', '.PNG']

# def clean the files from child of parent
def garbagefile_clean(path):
    for parents in listdir(path):
        child = join(path,parents)
        if isdir(child):
            garbagefile_clean(child)
        #Size define as bite plz conversion first
        if splitext(child)[1] in garbage_extension and getsize(child)<=20000:
            print(getsize(child))
            remove(child)
            print(child, "deleted success")
        #Delete by time 
        elif os.path.isfile(filename):
            lastmodifytime = os.stat(filename).st_mtime #Time adj
            endfiletime = time.time() - 3600 * 24 * N #Set delete file since last modify(N = days you want)
        if endfiletime > lastmodifytime:
            remove(child)
            print(child, "deleted success")

#call function
garbagefile_clean(path)
for path in sys.argv[1:]:
    if isdir(path):
        garbagefile_clean(path)
