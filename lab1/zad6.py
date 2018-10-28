#!/usr/bin/python3

import os
import re

def location():
    loc = input("podaj sciezke do plikow:")
    return loc

def jpg_shearch():
    pattern = re.compile(r".*\.jpg")
    all_files = os.listdir(location())
    al_jpg=[]

    for f in all_files:
        if pattern.match(f):
            al_jpg.append(f)   
    return al_jpg

def conversion(argv):
    for f in argv:
        bar = f.split('.')
        name = bar[0]
        os.rename(f,name+".png")

conversion(jpg_shearch())
