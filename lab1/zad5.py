#!/usr/bin/python3

import os

def foo(bar):
    ilosc_plikow_katalogow = os.listdir(bar)
    al = []

    for i in ilosc_plikow_katalogow:
        path = os.path.join(bar, i)
        if os.path.isdir(os.path.join(bar,i)):
            al=al + foo(path)
        else:
            al.append(path)

    return  al           

root = input("Podaj sciezke:")
list_all = foo(root)
print (list_all, "\n")