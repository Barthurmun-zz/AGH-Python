#!/usr/bin/python3
from math import sqrt

def eval_rad(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)

    delt = (b**2) - (4*a*c)
    print(delt)
    if (delt > 0):
        print("Rownanie ma 2 pierwiastki ! \t")
        x1 = (-b-sqrt(delt))/(2*a)
        x2 = (-b+sqrt(delt))/(2*a)
        print("x1 = {} \t x2 = {}".format(x1,x2))
    elif delt==0:
        print("Rownanie ma 1 pierwiastek ! \t")
        x1 = (-b)/(2*a)
        print(x1)
    else:
        print("Rownanie nie ma pierwiastkow !")
    
a = input("Podaj parametr a:")
b = input("Podaj parametr b:")
c = input("Podaj parametr c:")
eval_rad(a,b,c)