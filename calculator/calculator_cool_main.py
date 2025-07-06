import calculator_cool_funct as functions
import random

def main():
    while True:
        num = []
        x = int(input('Введите длину списка: '))
        y = int(input('Задайте диапазон списка: '))
        for i in range(0, x):
            num.append(random.randint(0, y))
        operation = str(input('Выберите операцию: '))
        if operation == 'sum':
            print(num)
            print(functions.sum(num))
        elif operation == 'arrange':
            print(num)
            print(functions.arrange(num))
        elif operation == 'min':
            print(num)
            print(functions.min(num))
        elif operation == 'max':
            print(num)
            print(functions.max(num))
        elif operation == 'incr':
            print (functions.incr(num))
        elif operation == 'decr':
            print(functions.decr(num))
        elif operation == 'deviation':
            print(functions.deviation(num))
        z = input("Continue?")
        if z == "no":
            break
if __name__ == "__main__":
    main()