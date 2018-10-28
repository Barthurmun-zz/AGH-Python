import numpy as np

f_mother=np.random.random((4,4))

for i in range(4):
    for k in range(4):
        f_mother=f_mother*10

wyznaczynik = np.linalg.det(f_mother)
print(wyznaczynik)