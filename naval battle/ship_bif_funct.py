import random

def init_field(field):
    field = []
    for i in range(0, 10):
        field.append([0] * 10)
    return field
def inter(field):
    for y in range(0,10):
        print('\n')
        for x in range(0,10):
            if field[y][x] == 0 or field[y][x] == 1:
                print('_', end=" ")
            if field[y][x] == 'X':
                print('X', end=" ")
            elif field[y][x] == 'Z':
                print('Z', end=" ")
    print()
    return field
def ships_number():
    while True:
        ships_num = int(input('Введите количество кораблей'))
        if ships_num > 100:
            print('Все корабли не поместятся в море')
        else:
            print(f'Количество кораблей: {ships_num}')
            return ships_num
def ships_place(field, ships_num):
    ships_place_ = 0
    while ships_place_ < ships_num:
        a = random.randint(0,9)
        b = random.randint(0,9)
        if field[a][b] == 0:
            field[a][b] = 1
            ships_place_ += 1
def update(field):
    for row in field:
        print(row)
def att(field):
    while True:
        x = int(input('Введите координату х'))
        y = int(input('Введите координату y'))
        if 10 <= x or x < 0 and 10 <= y or y < 0:
            print('Неверные координаты')
            continue
        return x,y

