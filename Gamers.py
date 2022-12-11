"""Gamers class"""



class Gamer:

    def __init__(self):
        self.shticks = list([])
        self.count_shticks = 0
        self.shticks = {1: "0-0", 2: "0-1", 3: "0-2", 4: "0-3", 5: "0-4", 6: "0-5", 7: "0-6",
                           8: "1-1", 9: "1-2", 10: "1-3", 11: "1-4", 12: "1-5", 13: "1-6",
                           14: "2-2", 15: "2-3", 16: "2-4", 17: "2-5", 18: "2-6",
                           19: "3-3", 20: "3-4", 21: "3-5", 22: "3-6",
                           23: "4-4", 24: "4-5", 25: "4-6",
                           26: "5-5", 27: "5-6",
                           28: "6-6"}

    def input_number(self):
        while True:
            try:
                number_shtics = int(input())
                break
            except ValueError:
                print('Неправильно введен номер, попробуйте снова')
                return self.input_number()
        return number_shtics



