"""Gamers class"""



class Gamer:

    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.shticks = []
        self.errors = 0
        self.name = ''

    def input_number(self):
        while True:
            try:
                number_shtics = int(input())
                break
            except ValueError:
                print('Неправильно введен номер, попробуйте снова')
                return self.input_number()
        return number_shtics



