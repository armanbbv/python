import random as r



def act(characteristic_1, characteristic_x, new_characteristic_1, new_characteristic_x):

    print('Выберите действие: a - увернуться', 'b - нанести урон', 'c - выпить зелье', sep='\n')
    action_x = str(input("Выберите действие:"))


    d_x_0 = 0
    d_x_1 = 0
    d_1_0 = 0
    d_1_1 = 0
    actt_x = str('hhh')
    actt_1 = str('hhh')

    if action_x == 'b':
        actt_x = "Хороший удар!"
        d_x_1 = -20
        d_1_0 = -25

    action_1 = r.choice(['a', 'b', 'c'])

    if action_1 == 'b':
        actt_1 = "атакует!"

        d_1_1 = -20
        d_x_0 = -25

    new_characteristic_x[0] = characteristic_x[0] + d_x_0
    new_characteristic_x[1] = characteristic_x[1] + d_x_1
    new_characteristic_1[0] = characteristic_1[0] + d_1_0
    new_characteristic_1[1] = characteristic_1[1] + d_1_1

    if action_x == 'a':
        actt_x = "Вы увернулись от удара!"
        new_characteristic_x[0] = new_characteristic_x[0] - d_x_0
        new_characteristic_x[1] = new_characteristic_x[1] - 5
    elif action_1 == 'a':
        actt_1 = "Увернулся от удара!"
        new_characteristic_1[0] = new_characteristic_1[0] - d_1_0
        new_characteristic_1[1] = new_characteristic_1[1] - 5

    if action_x == 'c':
        actt_x = str('Cилы восстановлены!')
        new_characteristic_x[0] += 15
        new_characteristic_x[1] += 30

    if action_1 == 'c':
        actt_1 = str('восстановил силы!')
        new_characteristic_1[0] += 15
        new_characteristic_1[1] += 30



    new_characteristic_x[0] = max(0, min(100, new_characteristic_x[0]))
    new_characteristic_x[1] = max(0, min(100, new_characteristic_x[1]))
    new_characteristic_1[0] = max(0, min(100, new_characteristic_1[0]))
    new_characteristic_1[1] = max(0, min(100, new_characteristic_1[1]))

    print(f'{actt_x} Так держать! Враг {actt_1} \n',
          f'Ваше здоровье: {new_characteristic_x[0]}, ваша сила: {new_characteristic_x[1]}\n',
          f'Здоровье врага: {new_characteristic_1[0]}, сила врага: {new_characteristic_1[1]}')
    return new_characteristic_1, new_characteristic_x


def c_x(new_characteristic_x):
    new_characteristic_x[0] += 15
    new_characteristic_x[1] += 30
    print('Силы восстановлены! Продолжите сражение')


def c_1(new_characteristic_1):
    new_characteristic_1[0] += 15
    new_characteristic_1[1] += 30
    print('Враг восстановил силы, можете продолжить сражение!')