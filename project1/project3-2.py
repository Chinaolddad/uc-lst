from os.path import isdir, join, splitext, getsize, isfile
from os import remove, listdir
import os
import time


def garbagefile_clean_mode1(path, N: int):
    res = []
    for file in listdir(path):
        child = join(path, file)
        if isdir(child):
            garbagefile_clean_mode1(child, N)
        elif isfile(child):
            lastmodifytime = os.stat(child).st_mtime
            endfiletime = time.time() - 3600 * 24 * N  # Set delete file since last modify(N = days you want)
            if endfiletime > lastmodifytime:
                res.append(child)
                remove(child)
                print(child, "deleted success")
    return res


def garbagefile_clean_mode2(path, N: int):
    res = []
    garbage_extension = ['tmp', '.log', '.obj', '.jpg', '.PNG', '.txt']
    for file in listdir(path):
        child = join(path, file)
        if isdir(child):
            garbagefile_clean_mode2(child, N)
        elif isfile(child):
            if splitext(child)[1] in garbage_extension and getsize(child) <= N:
                res.append(child)
                remove(child)
                print(child, "deleted success")
    return res
