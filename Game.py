"""Main Game"""
import os
import sys
os.environ["SDL_VIDEODRIVER"] = "dummy"
from Gamers import Gamer
import random
import pygame
from pygame.color import THECOLORS


class Game:
    """Основная часть игры"""

    min_of_end_point = 101

    def __init__(self, name_one, name_two, name_three, name_four):
        self.gamer_one = Gamer(name_one)
        self.gamer_two = Gamer(name_two)
        self.gamer_three = Gamer(name_three)
        self.gamer_four = Gamer(name_four)
        self.board = list([])
        self.players = list([self.gamer_one, self.gamer_two, self.gamer_three, self.gamer_four])
        self.count_round = 1
        self.number_first_move = 0
        self.point_team_one = 0
        self.point_team_two = 0
        self.end_round = True
        self.end_game = True
        self.all_shtick = {1: "0-0", 2: "0-1", 3: "0-2", 4: "0-3", 5: "0-4", 6: "0-5", 7: "0-6",
                           8: "1-1", 9: "1-2", 10: "1-3", 11: "1-4", 12: "1-5", 13: "1-6",
                           14: "2-2", 15: "2-3", 16: "2-4", 17: "2-5", 18: "2-6",
                           19: "3-3", 20: "3-4", 21: "3-5", 22: "3-6",
                           23: "4-4", 24: "4-5", 25: "4-6",
                           26: "5-5", 27: "5-6",
                           28: "6-6"}
        self.doubles = [1, 8, 14, 19, 23, 26, 28]

    def examination_distribution(self, list_of_shtick):
        """ Проверка разданных фишек на наличие 5 и больше дублей """
        for i in range(0, 4):
            count_doubles = 0
            for number in self.doubles:
                if number in list_of_shtick[i * 7: i * 7 + 7]:
                    count_doubles += 1
            if count_doubles >= 5:
                return False
        return True

    def match_list(self, count):
        """ Функция выбора порядка ходов """
        match count:
            case 1:
                return list([1, 2, 3, 4])
            case 2:
                return list([2, 3, 4, 1])
            case 3:
                return list([3, 4, 1, 2])
            case 4:
                return list([4, 1, 2, 3])

    def find_first_move(self):
        """ Выбор игрока, у которого 1-1 """
        tmp = 1
        for player in self.players:
            for elem in player.shticks:
                if elem == 8:
                    return self.match_list(tmp)
            tmp += 1

    def order(self):
        """Возвращаем порядок"""
        if self.count_round == 1:
            return self.find_first_move()
        else:
            return self.match_list(self.number_first_move)

    def chip_distribution(self):
        """ Раздача фишек и возврат """
        tmp = list(range(1, 29))
        random.shuffle(tmp)

        if (self.examination_distribution(tmp) == True):
            self.gamer_one.shticks = sorted(tmp[:7])
            self.gamer_one.count_shticks = 7
            self.gamer_two.shticks = sorted(tmp[7:14])
            self.gamer_two.count_shticks = 7
            self.gamer_three.shticks = sorted(tmp[14:21])
            self.gamer_three.count_shticks = 7
            self.gamer_four.shticks = sorted(tmp[21:28])
            self.gamer_four.count_shticks = 7
        else:
            tmp = list(range(1, 29))
            random.shuffle(tmp)
            self.chip_distribution(tmp)

    def options(self, value):
        """Возможные варианты которые можно поставить"""
        tmp_lst = list([])
        for key in self.all_shtick:
            if ((self.all_shtick[key][0] == self.all_shtick[value][0] or
                 self.all_shtick[key][0] == self.all_shtick[value][2] or
                 self.all_shtick[key][2] == self.all_shtick[value][0] or
                 self.all_shtick[key][2] == self.all_shtick[value][2]) and
                    (self.all_shtick[key] != self.all_shtick[value])):
                tmp_lst.append(key)
        return tmp_lst

    def examination_number_shtics(self, values, player):
        """Фишка была выбрана и теперь мы пытаемся ее ставить"""

        options_on_the_left = self.options(self.board[0])
        options_on_the_right = self.options(self.board[-1])

        ## Здесь можно поставить фишку и справа, и слева, поэтому надо предлагать игроку какой-то выбор и выводить
        ##доску на экран чтобы он понимал куда можно поставить

        if player.shticks[values] in options_on_the_left:
            print('Ставим фишку слева')
            self.board.insert(0, values)
            player.shticks.pop(values)
            player.count_shticks -= 1
            return True
        elif values in options_on_the_right:
            print('Ставим фишку справа')
            self.board.append(0, values)
            player.shticks.pop(values)
            player.count_shticks -= 1
            return True
        else:
            return False

    def dont_end_round(self):
        """ Проверяем кончился ли раунд?"""

        for player in self.players:
            if player.count_shticks == 0:
                self.end_round = False
                return False

        ## Проверяем рыбу через возможные варианты
        var_of_fish = [list([i for i in range(1, 8)]), list([2, 8, 9, 10, 11, 12, 13]),
                       list([3, 9, 14, 15, 16, 17, 18]), list([4, 10, 15, 19, 20, 21, 22]),
                       list([5, 11, 16, 20, 23, 24, 25]), list([6, 12, 17, 21, 24, 26, 27]),
                       list([6, 13, 18, 22, 25, 27, 28])]
        for number_of_fish in var_of_fish:
            count = 0
            for elem in number_of_fish:
                if elem in self.board:
                    count += 1
            if count == 7:
                self.end_round = False
                return False

    def possible_chips_that_can_be_placed(self, player):
        """ Выбираем номер фишки и проверяем куда ее можно поставить"""
        print('Ваши фишки')
        for elem in player.shticks:
            print(self.all_shtick[elem])
        print('Введите номер фишки')
        number_shtics = player.input_number()

        if self.examination_number_shtics(number_shtics, player) is True:
            return True
        else:
            return self.possible_chips_that_can_be_placed(player)

    def put_a_chip(self, number_of_player):
        """ Выбор фишки, которую можно поставить"""

        if self.count_round == 1 and 8 not in self.board:
            self.board.append(8)
            self.players[number_of_player - 1].shticks.remove(8)
            self.players[number_of_player - 1].count_shticks -= 1
        else:
            self.possible_chips_that_can_be_placed(self.players[number_of_player])

    def return_coordinate_point_one(self, number, X, Y):
        # Возвращаем координату точки
        if int(self.all_shtick[number][0]) == 1:
            return list([[X + 15, Y + 15, 5, 4]])
        elif int(self.all_shtick[number][0]) == 2:
            return list([[X + 8, Y + 10, 5, 4],
                         [X + 22, Y + 20, 5, 4]])
        elif int(self.all_shtick[number][0]) == 3:
            return list([[X + 7, Y + 7, 5, 4],
                         [X + 14, Y + 14, 5, 4],
                         [X + 21, Y + 22, 5, 4]])
        elif int(self.all_shtick[number][0]) == 4:
            return list([[X + 8, Y + 10, 5, 4],
                         [X + 8, Y + 20, 5, 4],
                         [X + 22, Y + 10, 5, 4],
                         [X + 22, Y + 20, 5, 4]])
        elif int(self.all_shtick[number][0]) == 5:
            return list([[X + 7, Y + 7, 5, 4],
                         [X + 7, Y + 22, 5, 4],
                         [X + 14, Y + 14, 5, 4],
                         [X + 21, Y + 7, 5, 4],
                         [X + 21, Y + 22, 5, 4]])
        elif int(self.all_shtick[number][0]) == 6:
            return list([[X + 8, Y + 7, 5, 4],
                         [X + 8, Y + 14, 5, 4],
                         [X + 8, Y + 21, 5, 4],
                         [X + 22, Y + 7, 5, 4],
                         [X + 22, Y + 14, 5, 4],
                         [X + 22, Y + 21, 5, 4]])

    def return_coordinate_point_two(self, number, X, Y):
        # Возвращаем координату точки
        if int(self.all_shtick[number][2]) == 1:
            return list([[X + 15, Y + 45, 5, 4]])
        elif int(self.all_shtick[number][2]) == 2:
            return list([[X + 8, Y + 40, 5, 4],
                         [X + 22, Y + 50, 5, 4]])
        elif int(self.all_shtick[number][2]) == 3:
            return list([[X + 7, Y + 37, 5, 4],
                         [X + 14, Y + 44, 5, 4],
                         [X + 21, Y + 52, 5, 4]])
        elif int(self.all_shtick[number][2]) == 4:
            return list([[X + 8, Y + 40, 5, 4],
                         [X + 8, Y + 50, 5, 4],
                         [X + 22, Y + 40, 5, 4],
                         [X + 22, Y + 50, 5, 4]])
        elif int(self.all_shtick[number][2]) == 5:
            return list([[X + 7, Y + 37, 5, 4],
                         [X + 7, Y + 52, 5, 4],
                         [X + 14, Y + 44, 5, 4],
                         [X + 21, Y + 37, 5, 4],
                         [X + 21, Y + 52, 5, 4]])
        elif int(self.all_shtick[number][2]) == 6:
            return list([[X + 8, Y + 37, 5, 4],
                         [X + 8, Y + 44, 5, 4],
                         [X + 8, Y + 51, 5, 4],
                         [X + 22, Y + 37, 5, 4],
                         [X + 22, Y + 44, 5, 4],
                         [X + 22, Y + 51, 5, 4]])

    def start_game(self):
        """ Непосредственно игра """

        pygame.init()
        dis = pygame.display.set_mode((1500, 750))
        dis.fill(THECOLORS['lightskyblue3'])
        pygame.display.update()
        pygame.display.set_caption('Dominoes by SanyaCentner')
        clock = pygame.time.Clock()
        time_on_move = 0.08
        time_to_clear_text = 0.5
        while self.end_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end_game = False

            while self.end_round:
                ## Отписываем номер раунда
                font = pygame.font.Font(None, 25)
                text_round = font.render(f"Начинается {self.count_round}-й раунд", True, THECOLORS['black'])
                place_text_round = text_round.get_rect(center=(750, 50))
                dis.blit(text_round, place_text_round)

                ## Тут должна быть основная логика раунда: раздать фишки и чтобы каждый видел свои
                self.chip_distribution()
                print('Раздача окончена')
                ## Раздаем фишки каждому и начинаем проходить по каждому человеку и отрисовывать фишки
                for number in self.order():
                    print(self.players[number - 1].shticks)
                    # Отрисовываем кто делает ход
                    text_name = font.render(f"Ход делает {self.players[number - 1].name}", True, THECOLORS['black'])
                    place_text_name = text_name.get_rect(center=(100, 50))
                    dis.blit(text_name, place_text_name)
                    # Отрисовываем все фишки данного игрока
                    text_shticks = font.render("Ваши фишки:", True, THECOLORS['black'])
                    place_text_shticks = text_shticks.get_rect(center=(750, 670))
                    dis.blit(text_shticks, place_text_shticks)
                    # Отрисовываем сами фишки
                    X_player_shticks_start = 645
                    Y_player_shticks_start = 690
                    # Отрисовываем закрашенную часть
                    pygame.draw.polygon(dis, THECOLORS['white'],
                                        [[X_player_shticks_start, Y_player_shticks_start],
                                         [X_player_shticks_start + 210, Y_player_shticks_start],
                                         [X_player_shticks_start + 210, Y_player_shticks_start + 60],
                                         [X_player_shticks_start, Y_player_shticks_start + 60]])
                    for dominoes in self.players[number - 1].shticks:
                        print(dominoes)
                        print(self.return_coordinate_point_one(dominoes, X_player_shticks_start,
                                                               Y_player_shticks_start))
                        # Отрисовываем точки, если там нуль, то отрисовываем только нижнее
                        if dominoes not in [1, 2, 3, 4, 5, 6, 7]:
                            for lst_one in self.return_coordinate_point_one(dominoes, X_player_shticks_start,
                                                                            Y_player_shticks_start):
                                pygame.draw.rect(dis, THECOLORS['black'], lst_one)
                        if dominoes != 1:
                            for lst_two in self.return_coordinate_point_two(dominoes, X_player_shticks_start,
                                                                            Y_player_shticks_start):
                                pygame.draw.rect(dis, THECOLORS['black'], lst_two)
                        # Переходим к следущей координате
                        X_player_shticks_start = X_player_shticks_start + 30
                        pygame.draw.line(dis, THECOLORS['black'], [X_player_shticks_start, 690],
                                         [X_player_shticks_start, 750])

                        pygame.draw.line(dis, THECOLORS['black'], [645, 720], [855, 720])
                        pygame.display.update()
                        clock.tick(time_to_clear_text)
                    clock.tick(time_on_move)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.end_round = False

                    #                     if event.type ==

                    #                     self.put_a_chip(number)

                    clock.tick(time_on_move)

                    self.count_round += 1

                self.end_round = True

            self.end_game = False
        pygame.quit()
        quit()
        # self.start_round()


if __name__ == '__main__':
    # game = Game(input("Введите имя первого игрока"), input("Введите имя второго игрока"),
    #             input("Введите имя третьего игрока"), input("Введите имя четвертого игрока"))
    game = Game('Sasha', 'Vanya', 'Seva', 'Vova')
    game.start_game()
    print('c')






