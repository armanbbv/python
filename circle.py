def main():
    a=[]
    x = int(input('Введите длину поля: '))
    y = int(input('Введите ширину поля: '))
    a=[[0]*x for i in range (y)]
    centre_x=int(input('Введите координату центра по x: '))
    centre_y=int(input('Введите координату центра по y: '))
    r = int(input('Задайте радиус окружности: '))
    a[centre_x][centre_y]='X'


    if r <= (x-1)/2 or r <= (y-1)/2 :
        for i in range(0, x):
            for j in range(0, y):
                if (centre_x - i) ** 2 + (centre_y - j) ** 2 <= r**2:
                    a[i][j] = 'X'

        for i in range(0, x):
            print('\n')
            for j in range(0, y):
                if a[i][j] == 0:
                    print(' ', end=" ")
                elif a[i][j] == 'X':
                    print('X', end=" ")
    else:
        print('Слишком большой радиус')


if __name__=="__main__":
    main()



