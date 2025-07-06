temp_room = 25
temp_hot = 100
water_vol = float(input('Сколько воды комнатной температуры у вас есть? (объем укажите в л)'))
temp_required = int(input('Какая температура воды вам нужна?'))
m_1 = (water_vol*(temp_hot - temp_required))/abs(temp_room - temp_hot)
p = 1
vol = float(m_1*p)
print(f'Необходимо долить {vol} л кипятка')