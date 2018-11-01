import multiprocessing as mp
from multiprocessing import Pool
import numpy as np
import time

x = np.random.randint(0, 10, 1000000000)#Losujemy 100mln liczb z zakresu 0-10

no_cores = 2

def split(data, parts):
    data = data.tolist() #Robimy liste z tych wylosowanych liczb
    lenght = len(data)
    part = int(np.ceil(lenght/parts)) #Zaokrąglamy liczby w górę 0.1 -> 1
    return [data[part*i : part*(i+1)] for i in range(parts)]

def f(x): #Funkcja tworząca słownik przechowywujący informacje do histogramu
    dict = {}
    for i in x:
        if i in dict.keys():
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    return dict

s = split(x, no_cores)

t1 = time.time()
pool = Pool(no_cores) #Tworzymy obiekt który umożliwia nam tzw."multiprocessing"
out = pool.map(f, s)

d = {}

for i in out:
    for k in i:
        if k in d.keys():
            d[k] = d[k] + i[k]
        else:
            d[k] = i[k]

print(time.time() - t1)
print(d)
