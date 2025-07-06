class Fighter:
    def __init__(self):
        self.health = 100
        self.beef = 15
        self.armor = 100
        self.log1 = Loger()
        self.log1.log_list.append(f'Здоровье бойца 1: {self.health}\n Здоровье бойца 2: {self.health}\n '
                             f'Броня бойца 1: {self.armor}\n Броня бойца 2: {self.armor}')
    def update_log(self):
        self.log1.log_list.clear()
        self.log1.log_list.append(f'Здоровье бойца 1: {self.health}\n Здоровье бойца 2: {self.health}\n '
                                  f'Броня бойца 1: {self.armor}\n Броня бойца 2: {self.armor}')

class Loger:
    def __init__(self):
        self.log_list = []
    def get_log(self):
        log =''
        for mes in self.log_list:
            log += mes+'\n'
        return log

def main():
    ret = Fighter()

    a = []
    for i in range(0,2):
        fighter_i = Fighter()
        a.append(fighter_i)
    while True:
        for enemy in a:
            if enemy.armor > 0:
                enemy.armor -= ret.beef
            else:
                enemy.health -= ret.beef
            if ret.armor > 0:
                ret.armor -= enemy.beef
            else:
                ret.health -= enemy.beef
        for enemy in a:
            enemy.update_log()
            print(enemy.log1.get_log())
        print('================')
        ret.update_log()
        print(ret.log1.get_log())
        input()

if __name__=='__main__':
    main()
