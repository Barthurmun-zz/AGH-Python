#!/usr/bin/python3

import random

def bouble_sort(N):
    #Tworzenie N-elementowej listy do posortowania
    sort=[]
    N=int(N)  

    for i in range(0,N):
        sort.append(random.randint(0,100))

    print("przed sortowaniem: {}".format(sort))

    for i in range(0,N-1):
        for j in range(0,N-1):
            if sort[j] < sort[j+1]:
                temp = sort[j+1]
                sort[j+1] = sort[j]
                sort[j] = temp
    
    return sort

N = input("Podaj dlugosc listy do posortowania:")
print("Posortowana lista:{}".format(bouble_sort(N)))

