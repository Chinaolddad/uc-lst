#Project for automatic clean the garbage file of folders
from os.path import isdir,join,splitext,getsize
from os import remove,listdir
import sys

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
        elif splitext(child)[1] in garbage_extension and getsize(child)<=20000:
            print(getsize(child))
            remove(child)
            print(child, "deleted....")

#call function
garbagefile_clean(path)
for path in sys.argv[1:]:
    if isdir(path):
        garbagefile_clean(path)
