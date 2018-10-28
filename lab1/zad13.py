import numpy as np

f_mother = np.random.random((8,8))
s_mother = np.random.random((8,8))


for w in range(8):
    for k in range(8):
        s_mother[w,k]=s_mother[w,k]*20
        f_mother[w,k]=f_mother[w,k]*10

t_mother = f_mother*s_mother
print(t_mother)