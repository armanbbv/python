characteristic = [70, 90, 70]
semesters = 0
sem = 4
while semesters < sem:
    print(f'Семестр {semesters + 1}: Ум: {characteristic[0]}, Здоровье: {characteristic[1]}, Сила: {characteristic[2]}')
    act = input("Чем заняться  в этом семестре? (учиться/работать/прогуливать): ")

    if act == "учиться":
        characteristic[0] += 30
        characteristic[1] -= 15
        characteristic[2] -= 15
    elif act == "работать":
        characteristic[0] -= 20
        characteristic[1] -= 10
        characteristic[2] -= 30
    elif act == "прогуливать":
        characteristic[0] -= 25
        characteristic[1] += 10
        characteristic[2] += 30
    else:
        print('Выбрано неверное действие')
        continue

    characteristic = [max(0, min(100, attr)) for attr in characteristic]

    if characteristic[0] == 0:
        print("Вы отчислены!")
        break

    semesters += 1

if semesters == sem:
    print("Вас ждет написание диплома))")
    act_1 = input('Вы хотите написать и защитить диплом? (да/нет)')
    if act_1 == 'да':
        print('Идет защита диплома...\n')
        print('\nДиплом успешно защищен. Поздравляем с окончанием университета!!')
    else:
        print('Вы отчислены!')
