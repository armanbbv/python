import random as r
import game_dvij as l
import game_bif as b
def main():
    x=int(input('Введите длину поля:'))
    y=int(input('Введите ширину поля:'))
    sum_players = int(input('Введите количество игроков на поле:'))
    arena=[[0]*x for i in range (y)]
    counter = 0

    h, z = None, None
    while True:
        a = r.randint(0, y-1)
        v = r.randint(0, x-1)
        if arena[a][v] == 0:
            arena[a][v] = 'X'
            break

    while counter < sum_players:
        h=r.randint(0,y-1)
        z=r.randint(0,x-1)
        if arena[h][z] == 0:
            arena[h][z] = 1
            counter += 1
    characteristic_x = [100,100]
    characteristic_1 = [100,100]
    counter_1=0
    new_characteristic_x = [0, 0]
    new_characteristic_1 = [0, 0]
    while counter_1 < sum_players:
        for i in arena:
            print(i)
        b.beeff(arena, a, v, counter_1, y, x, characteristic_1, characteristic_x, new_characteristic_x, new_characteristic_1)
        input('Нажмите Enter')
        a,v = l.step_x(arena, a, v, x, y)
        for _ in arena:
            h,z = l.step_1(arena, z, h, x, y)
            print(_)
    if counter_1==sum_players:
        print(f'Вы победили всех врагов, количество убийств:{counter_1}')
    elif characteristic_x[0]==0:
        print(f'Вы проиграли, количество убийств:{counter_1}')











if __name__ == '__main__':
    main()