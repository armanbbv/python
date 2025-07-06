import game_act as t


def beeff(arena, a, v, counter_1, x, y,
          characteristic_1, characteristic_x, new_characteristic_x, new_characteristic_1):

    neighbors = [(a - 1, v),(a + 1, v),(a, v - 1), (a, v + 1)]

    for row, col in neighbors:

        if 0 <= row < x and 0 <= col < y and arena[row][col] == 1:
            print('Вам предстоит сражение с врагом, приготовьтесь к бою')

            while True:

                new_characteristic_1, new_characteristic_x = t.act(characteristic_1, characteristic_x, new_characteristic_1, new_characteristic_x)

                characteristic_x[0] = new_characteristic_x[0]
                characteristic_x[1] = new_characteristic_x[1]
                characteristic_1[0] = new_characteristic_1[0]
                characteristic_1[1] = new_characteristic_1[1]


                if new_characteristic_1[0] <= 0:
                    counter_1 += 1
                    arena[row][col] = 0
                    print(f'Враг побеждён! Количество убийств: {counter_1}')
                    characteristic_x = [100, 100]
                    characteristic_1 = [100, 100]
                    break
                elif new_characteristic_x[0] <= 0:
                    print('Попробуйте ещё раз!')
                    characteristic_x = [100, 100]
                    break


                if new_characteristic_x[1] == 0:
                  while new_characteristic_x[1] == 0:
                    print('Восстановите силы! ')
                    action_x = input('Нажмите <c>')
                    if action_x == 'c':
                      t.c_x(new_characteristic_x)
                    else:
                      print('Выбрано неверное действие:(')

                if new_characteristic_1[1] == 0:
                    t.c_1(new_characteristic_1)

                new_characteristic_x = [100, 100]
                new_characteristic_1 = [100, 100]