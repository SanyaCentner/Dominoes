"""Gamers class"""



class Gamer:

    def __init__(self, name):
        self.name = name
        self.count_shticks = 0
        self.shticks = list([])

    def input_number(self):
        while True:
            try:
                number_shtics = int(input())
                break
            except ValueError:
                print('Неправильно введен номер, попробуйте снова')
                return self.input_number()
        return number_shtics



