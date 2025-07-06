import random

a = []
x = 12
y = int(input())
for i in range(0,x):
    a.append(random.randint(0,y))
print(a)

def exp():
    exp_1 = 0
    for i in a:
        exp_1 += i
    return exp
print(f'Математическое ожидание: {exp()}')

def var():
    exp_1 = 0
    arith = 0
    c = 0
    d = 0
    var_1 = 0
    for i in a:
        c += i**2
        d = c/x
        exp_1 += i
        arith = exp_1/x
        var_1 = d - (arith**2)
    return var
print(f'Дисперсия: {var()}')

def f():
    f_1 = 0
    c = 0
    d = 0
    for i in a:
        c += i ** 2
        d = c / x
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                swap = a[i]
                a[i] = a[j]
                a[j] = swap
        f_1 = (a[6] + a[7])/2
    return f
print(f'Медианный доход: {f()}')

