import matplotlib.pyplot as plt
import numpy as np
A=10**13
E = int(input("Введите значение энергии"))
R = 8.314
a = float(input("Введите начальное значение температуры:"))
b = float(input("Введите конечное значение температуры:"))
c = float(input("Введите шаг:"))
if a<=0 or b<=0:
    print("Температура не может быть 0 или меньше")
elif a>b:
    print("Первое значение должно быть меньше")
T = np.arange (a,b,c)
k=A*np.exp(-E/(R*T))
plt.bar(T,k, label = "k(T)", color='red')
plt.xlabel('Температура')
plt.ylabel('Скорость реакции')
plt.grid(True)
plt.legend()
plt.show()
