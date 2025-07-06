product_1 = "fridge"
product_2 = "mixer"
product_3 = "multi_cooker"
price_1 = 40000
price_2 = 3000
price_3 = 7000
money = 20000
num_of_prod_1 = 0
num_of_prod_2 = 0
num_of_prod_3 = 0
sum_of_prod = 0

print("exit or choice of products")
choice_1 = str(input())
while choice_1 == 'choice of products':
    choice_2 = str(input('product: '))
    if choice_2 == product_1 :
        if price_1 > money:
            print('not enough money')
        else:
            sum_of_prod += price_1
            num_of_prod_1 += 1
            money -= price_1
    elif choice_2 == product_2:
        if price_2 > money:
           print('not enough money')
        else:
            sum_of_prod += price_2
            num_of_prod_2 += 1
            money-= price_2
    elif choice_2 == product_3:
            if price_3 > money:
                print('not enough money')
            else:
                sum_of_prod += price_3
                num_of_prod_3 += 1
                money -= price_3
    else:
        print('incorrect choice')

    cont = input('continue the selection?')
    if cont != 'yes':
        break

print('your cheque\n')
print(f'number of prod_1: {num_of_prod_1}')
print(f'number of prod_2: {num_of_prod_2}')
print(f'number of prod_3: {num_of_prod_3}')
print(f'total cost: {sum_of_prod}')
print(f'your money: {money}')