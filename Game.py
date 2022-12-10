"""Main Game"""


from Gamers import Gamer
import random

class Game:
    """Основная часть игры"""

    min_of_end_point = 101
    def __init__(self):
        self.gamer_one = Gamer()
        self.gamer_two = Gamer()
        self.gamer_three = Gamer()
        self.gamer_four = Gamer()
        self.point_team_one = 0
        self.point_team_two = 0
        self.end_round = True
        self.end_game = True
        self.all_shtick = {'1': "0-0", '2': "0-1", '3': "0-2", '4': "0-3", '5': "0-4", '6': "0-5", '7': "0-6",
                           '8': "1-1", '9': "1-2", '10': "1-3", '11': "1-4", '12': "1-5", '13': "1-6",
                           '14': "2-2", '15': "2-3", '16': "2-4", '17': "2-5", '18': "2-6",
                           '19': "3-3", '20': "3-4", '21': "3-5", '22': "3-6",
                           '23': "4-4", '24': "4-5", '25': "4-6",
                           '26': "5-5", '27': "5-6",
                           '28': "6-6"}
        self.doubles = [1, 8, 14, 19, 23, 26, 28]

    def examination_distribution(self, list_of_shtick):
        for i in range(0, 4):
            count_doubles = 0
            for number in self.doubles:
                if number in list_of_shtick[i * 7, i * 7 + 7]:
                    count_doubles += 1
            if count_doubles >= 5:
                return False
        return True

    def chip_distribution(self):
        tmp = list(range(1, 28))
        random.shuffle(tmp)

        if (self.examination_distribution(tmp) == True):
            self.gamer_one.shticks = tmp[:7]
            self.gamer_two.shticks = tmp[7:14]
            self.gamer_three.shticks = tmp[14:21]
            self.gamer_four.shticks = tmp[21:28]
        else:
            tmp = list(range(1, 28))
            random.shuffle(tmp)
            self.chip_distribution(tmp)

    def start_round(self):
        while self.end_round:
            print('Начало раунда')
            self.chip_distribution()


    def start_game(self):
        print('Начало игры')
        while self.end_game:
            self.start_round()




