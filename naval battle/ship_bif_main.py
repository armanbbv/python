import ship_bif_funct as funct

def main():
    print('***Морской бой***\n')
    field = funct.init_field(10)
    ships_num = funct.ships_number()
    funct.ships_place(field,ships_num)
    damage = 0

    while damage < ships_num:
        funct.inter(field)
        x,y = funct.att(field)

        if field[y][x] == 1:
            print("Точно в цель!!")
            field[y][x] = 'X'
            damage += 1
        elif field[y][x] == 0:
            print("Попробуй еще раз")
            field[y][x] = 'Z'
        else:
            print("Кажется, выстрел сюда уже был")
    print("***Игра завершена***")

if __name__=='__main__':
    main()