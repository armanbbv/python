import random
def sum(num):
    sum = 0
    for i in num:
        sum += i
    return sum
def arrange(num):
    sum = 0
    for i in num:
        sum += i
    return sum/len(num)
def min(num):
    a_min = num[0]
    for i in num:
        if i < a_min:
            a_min = i
    return a_min
def max(num):
    a_max = 0
    for i in num:
        if i > a_max:
            a_max = i
    return a_max
def incr(num):
    for i in range(0, len(num)):
        for j in range(i + 1, len(num)):
            if num[i] > num[j]:
                swap = num[i]
                num[i] = num[j]
                num[j] = swap
    return num
def decr(num):
    for i in range(0, len(num)):
        for j in range(i + 1, len(num)):
            if num[i] < num[j]:
                swap = num[i]
                num[i] = num[j]
                num[j] = swap
    return num
def deviation (num):
    x = int(input('Введите длину списка: '))
    y = int(input('Задайте диапазон списка: '))
    num_2 = []
    s = 0
    for i in range(0, x):
        num_2.append(random.randint(0, y))
    for i in range(0, x):
        if num[i] != 0:
            s+=((num[i] - num_2[i]) / (num[i]))

    return s