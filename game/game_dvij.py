import random as r

def step_x(arena, a, v, x, y):
    print('Ваш ход:', '1 - влево', '2 - вправо', '3 - вверх', '4 - вниз', '5 - влево вниз по диагонали',
          '6 - вправо вниз по диагонали', '7 - влево вверх по диагонали', '8 - вправо вверх по диагонали',
          sep='\n')
    while True:
        step=str(input('Ваш шаг:'))
        if step in ('1', '2', '3', '4', '5', '6', '7', '8'):
            break
        else:
            print ('Неверный ход! Выберите число от 1-8')

    if step == '1':
        dx = -1
        dy = 0
    elif step == '2':
        dx = +1
        dy = 0
    elif step == '3':
        dx = 0
        dy = -1
    elif step == '4':
        dx = 0
        dy = +1
    elif step == '5':
        dx = -1
        dy = +1
    elif step == '6':
        dx = +1
        dy = +1
    elif step == '7':
        dx = -1
        dy = -1
    elif step == '8':
        dx = +1
        dy = -1

    new_a = (a + dy) % y
    new_v = (v + dx) % x
    if arena[new_a][new_v] == 0:
        arena[a][v]=0
        arena[new_a][new_v] = 'X'
        return new_a, new_v
    else:
        return a,v

def step_1(arena, z, h, x, y):
    dx=r.randint(-1,1)
    dy=r.randint(-1,1)
    new_h = (h+dy) % y
    new_z = (z+dx) % x
    if arena[new_h][new_z] == 0:
        arena[h][z] = 0
        arena[new_h][new_z] = 1
        return new_h, new_z
    else:
        return h,z

