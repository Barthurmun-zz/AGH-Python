#!/usr/bin/python3

import math

class LiczbyZespolone(object):
    '''Ta klasa przechowuje i pozwala na operacje na liczbach zespolonych'''
    def __init__(self,re,im):
        self.im = float(im)
        self.re = float(re)

    def add(a,b):
        '''Dodawanie dwóch liczb zespolonych'''
        c = LiczbyZespolone(0,0)
        c.re = a.re + b.re
        c.im = a.im + b.im
        return c

    def sub(a,b):
        '''Odejmowanie dwóch liczb zespolonych'''
        c = LiczbyZespolone(0,0)
        c.re = a.re - b.re
        c.im = a.im - b.im
        return c

    def mlt(a,b):
        '''Mnożenie dwóch liczb zespolonych'''
        c = LiczbyZespolone(0,0)
    
        if ((a.im and b.im) != 0):
            c.re = (a.re*b.re)-(a.im*b.im)
            c.im = (a.re*b.im)+(a.im*b.re)
        elif ((a.im == 0) and (b.im != 0)):
            c.re = a.re*b.re
            c.im = a.re*b.im
        elif ((a.im != 0) and (b.im == 0)):
            c.re = a.re*b.re
            c.im = b.re*a.im
        return c

    def __repr__(self):
        if (self.im > 0):
            return "{}+{}i".format(self.re,self.im)
        if (self.im < 0):
            return "{}{}i".format(self.re,self.im)
    
    def prtComplex(self,c=None):
        '''Wypisywanie stworzonej liczby zespolonej'''
        if c == None:
            if (self.im > 0):
                print("{}+{}i".format(self.re,self.im))
            if (self.im < 0):
                print("{}{}i".format(self.re,self.im))
        else:
            if (c.im > 0):
                print("{}+{}i".format(c.re,c.im))
            if (c.im < 0):
                print("{}{}i".format(c.re,c.im))


def main():
    f_complex_re = input("Podaj realis pierwszej liczby:")
    f_complex_im = input("Podaj imaginalis pierwszej liczby:")
    
    s_complex_re = input("Podaj realis drugiej liczby:")
    s_complex_im = input("Podaj imaginalis drugiej liczby:")
    
    f_complex = LiczbyZespolone(f_complex_re,f_complex_im)
    s_complex = LiczbyZespolone(s_complex_re,s_complex_im)
    
    add_comples = f_complex.add(s_complex)
    sub_comples = f_complex.sub(s_complex)
    mlt_comples = f_complex.mlt(s_complex)
    
    f_complex.prtComplex()
    s_complex.prtComplex()
    add_comples.prtComplex()
    sub_comples.prtComplex()
    mlt_comples.prtComplex()

if __name__ == '__main__':
    main()
