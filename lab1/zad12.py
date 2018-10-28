import numpy as np 

a = np.random.random((128,128))
b = np.random.random((128,128))

c = a + b
print("Pierwsza macierz: {},\n Druga macierz: {}, \n \
        Trzecia macierz (wynik dodawania): {}".format(a,b,c))
