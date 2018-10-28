#!/usr/bin/python3

import os

root="/dev"

def foo(bar):
    ilosc_plikow_katalogow = os.listdir(bar)
    return  ilosc_plikow_katalogow

list_all = foo(root)
print (list_all, "\n")