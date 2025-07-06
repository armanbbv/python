import numpy as np
length = 3
volume=np.arange(length, dtype = np.float64)
for i in range (length):
    x = float(input(f"Введите {i+1}-ое значение объема:"))
    volume[i]=x
    mask = x!=0
    print(mask)
print(volume)
mass=np.arange(length, dtype = np.float64)
for i in range (length):
    c = float(input(f"Введите {i+1}-ое значение массы:"))
    mass[i]=c
print(mass)
print(np.where(volume != 0, mass/volume, 'НЕТ'))
