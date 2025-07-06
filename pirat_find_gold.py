import random as r
def main():
    point = 0
    x=int(input('Введите длину поля:'))
    y = int(input('Введите ширину поля:'))
    arena =[[0]*x for i in range (y)]

    a = r.randint(0, y-1)
    v = r.randint(0, x-1)
    arena[a][v] = 'H'


    sum_jewel = r.randint(1, x)
    jewel=0

    while jewel<sum_jewel:
        h = r.randint(0, y-1)
        z = r.randint(0, x-1)
        if arena[h][z] == 0:
            arena[h][z] = 'X'
            jewel+=1

    sum_barrier = r.randint(1, y)

    while sum_barrier > 0:
        d = r.randint(0, y - 1)
        t = r.randint(0, x - 1)
        if arena[d][t] == 0:
            arena[d][t] = 'B'
            sum_barrier -= 1
    for i in arena:
        print (i)
    while sum_jewel>0:
        print('Ваш ход:', 'A - влево', 'D - вправо', 'W - вверх', 'S - вниз', sep='\n')
        step = str(input())
        dx = 0
        dy = 0
        if step == 'A':
            dx = -1
            dy = 0
        elif step == 'D':
            dx = 0
            dy = +1
        elif step == 'W':
            dx = +1
            dy = 0
        elif step == 'S':
            dx = -1
            dy = 0

        if arena[a+dx][v + dy] == 'B':
            print('Препятствие!')
            arena [a][v] = 'H'
        elif arena[a + dx][v+dy] == 'X' or arena[a+dx][v + dy]==0:
            new_v = (v + dx) % x
            new_a = (a+dy) % y
            sum_jewel -= 1
            arena[a][v] = 0
            arena[new_a][new_v]='H'
            v = new_v
            a = new_a
            if arena[a + dx][v+dy] == 'X':
                point += 100
                print(f'Вы нашли сокровище!Сумма очков {point}')
        for i in arena:
            print(i)
    print(f'Все сокровища найдены! Сумма очков: {point}')


if __name__ == "__main__":
    main()









