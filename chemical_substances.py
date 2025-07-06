class ChemicalSubstance:
    def __init__(self, name, molar, density):
        self.name = str(name)
        self.molar = float(molar)
        self.density = float(density)
    def calculate_moles(self, mass):
        self.mass = float(mass)
        self.n = self.mass / self.molar
        return self.n
    def calculate_volume(self, mass):
        self.mass = float(mass)
        self.volume = self.mass/ self.density
        return self.volume
    def  __str__(self):
        return (f'молярная масса: {self.molar} г/моль, плотность: {self.density} г/мл,'
                f'масса: {self.mass} г,  количество молей: {self.n}, объем: {self.volume} мл \n')
x = True
while x:
    name = input('Введите название вещества: ')
    mass = float(input('Введите массу вещества: '))
    molar = input('Введите молярную массу вещества: ')
    density = input('Введите плотность вещества: ')
    substance = ChemicalSubstance(name, molar, density)
    print(substance.calculate_moles(mass))
    print(substance.calculate_volume(mass))
    print(substance)
    print('Желаете ли вы продолжить?')
    y=input()
    if y == 'no':
        x = False

