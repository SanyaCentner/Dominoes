import pygame
import time
from pygame.color import THECOLORS
import random
from Gamers import Gamer

# class Game:
#     """Основная часть игры"""
#
#     min_of_end_point = 101
#
#     def __init__(self, name_one, name_two, name_three, name_four):
#         self.gamer_one = Gamer(name_one)
#         self.gamer_two = Gamer(name_two)
#         self.gamer_three = Gamer(name_three)
#         self.gamer_four = Gamer(name_four)
#         self.board = list([])
#         self.players = list([self.gamer_one, self.gamer_two, self.gamer_three, self.gamer_four])
#         self.count_round = 1
#         self.number_first_move = 0
#         self.point_team_one = 0
#         self.point_team_two = 0
#         self.end_round = True
#         self.end_game = True
#         self.all_shtick = {1: "0-0", 2: "0-1", 3: "0-2", 4: "0-3", 5: "0-4", 6: "0-5", 7: "0-6",
#                            8: "1-1", 9: "1-2", 10: "1-3", 11: "1-4", 12: "1-5", 13: "1-6",
#                            14: "2-2", 15: "2-3", 16: "2-4", 17: "2-5", 18: "2-6",
#                            19: "3-3", 20: "3-4", 21: "3-5", 22: "3-6",
#                            23: "4-4", 24: "4-5", 25: "4-6",
#                            26: "5-5", 27: "5-6",
#                            28: "6-6",
#                            29: "0-0", 30: "1-0", 31: "2-0", 32: "3-0", 33: "4-0", 34: "5-0", 35: "6-0",
#                            36: "1-1", 37: "2-1", 38: "3-1", 39: "4-1", 40: "5-1", 41: "6-1",
#                            42: "2-2", 43: "3-2", 44: "4-2", 45: "5-2", 46: "6-2",
#                            47: "3-3", 48: "4-3", 49: "5-3", 50: "6-3",
#                            51: "4-4", 52: "5-4", 53: "6-4",
#                            54: "5-5", 55: "6-5",
#                            56: "6-6"}
#         self.doubles = [1, 8, 14, 19, 23, 26, 28]
#         self.X_right = 750
#         self.X_left = 750
#         self.Y_doubles = 345
#         self.Y_not_doubles = 360
#
#     def examination_distribution(self, list_of_shtick):
#         """ Проверка разданных фишек на наличие 5 и больше дублей """
#         for i in range(0, 4):
#             count_doubles = 0
#             for number in self.doubles:
#                 if number in list_of_shtick[i * 7: i * 7 + 7]:
#                     count_doubles += 1
#             if count_doubles >= 5:
#                 return False
#         return True
#
#     def match_list(self, count):
#         """ Функция выбора порядка ходов """
#         match count:
#             case 1:
#                 return list([1, 2, 3, 4])
#             case 2:
#                 return list([2, 3, 4, 1])
#             case 3:
#                 return list([3, 4, 1, 2])
#             case 4:
#                 return list([4, 1, 2, 3])
#
#     def find_first_move(self):
#         """ Выбор игрока, у которого 1-1 """
#         tmp = 1
#         for player in self.players:
#             for elem in player.shticks:
#                 if elem == 8:
#                     return self.match_list(tmp)
#             tmp += 1
#
#     def order(self):
#         """Возвращаем порядок"""
#         if self.count_round == 1:
#             return self.find_first_move()
#         else:
#             return self.match_list(self.number_first_move)
#
#     def chip_distribution(self):
#         """ Раздача фишек и возврат """
#         tmp = list(range(1, 29))
#         random.shuffle(tmp)
#
#         if (self.examination_distribution(tmp) == True):
#             self.gamer_one.shticks = sorted(tmp[:7])
#             self.gamer_one.count_shticks = 7
#             self.gamer_two.shticks = sorted(tmp[7:14])
#             self.gamer_two.count_shticks = 7
#             self.gamer_three.shticks = sorted(tmp[14:21])
#             self.gamer_three.count_shticks = 7
#             self.gamer_four.shticks = sorted(tmp[21:28])
#             self.gamer_four.count_shticks = 7
#         else:
#             tmp = list(range(1, 29))
#             random.shuffle(tmp)
#             self.chip_distribution(tmp)
#
#     def options(self, value, side):
#         """Возможные варианты которые можно поставить"""
#         tmp_lst = list([])
#         if len(self.board) != 0:
#             if side == 'left':
#                 for key in self.all_shtick:
#                     if ((self.all_shtick[key][2] == self.all_shtick[self.board[0]][0]) and
#                             (self.all_shtick[key] != self.all_shtick[self.board[0]])):
#                         tmp_lst.append(key)
#             elif side == 'right':
#                 for key in self.all_shtick:
#                     if ((self.all_shtick[key][0] == self.all_shtick[self.board[-1]][2]) and
#                             (self.all_shtick[key] != self.all_shtick[self.board[-1]])):
#                         tmp_lst.append(key)
#         return tmp_lst
#
#     def examination_number_shtics(self, number, key, side, variable):
#         """Фишка была выбрана и теперь мы пытаемся ее ставить"""
#
#         ## Здесь можно поставить фишку и справа, и слева, поэтому надо предлагать игроку какой-то выбор и выводить
#         ##доску на экран чтобы он понимал куда можно поставить
#         print('мы зашли в функцию')
#         print(f"Какой номер из player берем {number}, какая фишка передается {key}, {variable}")
#         for var in variable:
#             if var[0][0] == number and var[0][1] == side and var[1] == True and var[2] == True:
#                 return (1, key + 28)
#             if var[0][0] == number and var[0][1] == side and var[1] == True and var[2] == False:
#                 return (1, key)
#             if var[0][0] == number and var[0][1] == side and var[1] == False and var[2] == True:
#                 return (2, key + 28)
#             if var[0][0] == number and var[0][1] == side and var[1] == False and var[2] == False:
#                 return (2, key)
#
#     def summ_points(self, player_first, player_second):
#         """ Считаем количество очков"""
#         count = 0
#         for shtick in player_first.shticks:
#             count += int(self.all_shtick[shtick][0]) + int(self.all_shtick[shtick][2])
#             print(f"Какая фишка {self.all_shtick[shtick]}, Сумма очков {count}")
#         for shtick in player_second.shticks:
#             count += int(self.all_shtick[shtick][0]) + int(self.all_shtick[shtick][2])
#             print(f"Какая фишка {self.all_shtick[shtick]}, Сумма очков {count}")
#
#         return count
#
#     def dont_end_round(self, passes, number_of_player):
#         """ Проверяем кончился ли раунд?"""
#         ## Проверяем рыбу
#         print("Проверяем конец раунда")
#         if passes == 4:
#             self.number_first_move = number_of_player
#             self.count_round += 1
#             team_one = self.summ_points(self.gamer_one, self.gamer_three)
#             team_two = self.summ_points(self.gamer_two, self.gamer_four)
#             if team_one == team_two:
#                 self.point_team_one += team_one
#                 self.point_team_two += team_two
#             elif team_one > team_two:
#                 self.point_team_one += team_one
#             elif team_one < team_two:
#                 self.point_team_two += team_two
#             return True
#
#         ## Проверяем конец раунда в целом
#         for count in range(0, 4):
#             print('ну что же, мы внутри')
#             if len(self.players[count].shticks) == 0:
#                 print(f"номер игрока {count}, сам игрок {self.players[count].name}")
#                 self.number_first_move = count + 1
#                 self.count_round += 1
#                 if count == 1 or count == 3:
#                     self.point_team_one += self.summ_points(self.gamer_one, self.gamer_three)
#                 elif count == 2 or count == 4:
#                     self.point_team_two += self.summ_points(self.gamer_two, self.gamer_four)
#                 return True
#
#         return False
#
#     def possible_chips_that_can_be_placed(self, player):
#         """ Отслеживаем номер фишки и куда ее поставить"""
#
#         ## Здесь можно поставить фишку и справа, и слева, поэтому надо предлагать игроку какой-то выбор и выводить
#         ##доску на экран чтобы он понимал куда можно поставить
#         lst_possible = list([])
#         lst_tmp = list([])
#         # Это условие для нового раунда и чел может поставить что хочет
#         if len(self.board) == 0:
#             for elem in player.shticks:
#                 if elem in self.doubles:
#                     lst_possible.append([[player.shticks.index(elem), 'left'], True, False])
#                     lst_possible.append([[player.shticks.index(elem), 'right'], True, False])
#                 else:
#                     lst_possible.append([[player.shticks.index(elem), 'left'], False, False])
#                     lst_possible.append([[player.shticks.index(elem), 'right'], False, False])
#             return lst_possible
#
#         options_on_the_left = self.options(self.board[0], 'left')
#         options_on_the_right = self.options(self.board[-1], 'right')
#         #         print('Номера, которые можно поставить слева', options_on_the_left)
#         #         print('Номера, которые можно поставить справа', options_on_the_right)
#
#         for elem in player.shticks:
#             if elem in options_on_the_left and elem in options_on_the_right:
#                 if elem in self.doubles:
#                     lst_possible.append([[player.shticks.index(elem), 'left'], True, False])
#                     lst_possible.append([[player.shticks.index(elem), 'right'], True, False])
#                 else:
#                     lst_possible.append([[player.shticks.index(elem), 'left'], False, False])
#                     lst_possible.append([[player.shticks.index(elem), 'right'], False, False])
#             elif elem in options_on_the_left:
#                 if elem in self.doubles:
#                     lst_possible.append([[player.shticks.index(elem), 'left'], True, False])
#                 else:
#                     lst_possible.append([[player.shticks.index(elem), 'left'], False, False])
#             elif elem in options_on_the_right:
#                 if elem in self.doubles:
#                     lst_possible.append([[player.shticks.index(elem), 'right'], True, False])
#                 else:
#                     lst_possible.append([[player.shticks.index(elem), 'right'], False, False])
#
#         for elem in player.shticks:
#             if elem + 28 in options_on_the_left and elem + 28 in options_on_the_right:
#                 if elem in self.doubles:
#                     lst_possible.append([[player.shticks.index(elem), 'left'], True, True])
#                     lst_possible.append([[player.shticks.index(elem), 'right'], True, True])
#                 else:
#                     lst_possible.append([[player.shticks.index(elem), 'left'], False, True])
#                     lst_possible.append([[player.shticks.index(elem), 'right'], False, True])
#             elif elem + 28 in options_on_the_left:
#                 if elem in self.doubles:
#                     lst_possible.append([[player.shticks.index(elem), 'left'], True, True])
#                 else:
#                     lst_possible.append([[player.shticks.index(elem), 'left'], False, True])
#             elif elem + 28 in options_on_the_right:
#                 if elem in self.doubles:
#                     lst_possible.append([[player.shticks.index(elem), 'right'], True, True])
#                 else:
#                     lst_possible.append([[player.shticks.index(elem), 'right'], False, True])
#         #         print('возможные варианты:', lst_possible)
#         if len(lst_possible) == 0:
#             return ([[], None, None])
#         return lst_possible
#
#     def put_a_chip(self, number_of_player):
#         """ Выбор фишки, которую можно поставить"""
#
#         if self.count_round == 1 and 8 not in self.board:
#             n = self.players[number_of_player].shticks.index(8)
#             return [[[n, 'right'], True, False], [
#                 [n, 'left'], True, False]]
#         else:
#             return self.possible_chips_that_can_be_placed(self.players[number_of_player])
#
#     def return_coordinate_point_one(self, number, X, Y):
#         # Возвращаем координату точки
#         if int(self.all_shtick[number][0]) == 1:
#             return list([[X + 15, Y + 15, 5, 4]])
#         elif int(self.all_shtick[number][0]) == 2:
#             return list([[X + 8, Y + 10, 5, 4],
#                          [X + 22, Y + 20, 5, 4]])
#         elif int(self.all_shtick[number][0]) == 3:
#             return list([[X + 7, Y + 7, 5, 4],
#                          [X + 14, Y + 14, 5, 4],
#                          [X + 21, Y + 22, 5, 4]])
#         elif int(self.all_shtick[number][0]) == 4:
#             return list([[X + 8, Y + 10, 5, 4],
#                          [X + 8, Y + 20, 5, 4],
#                          [X + 22, Y + 10, 5, 4],
#                          [X + 22, Y + 20, 5, 4]])
#         elif int(self.all_shtick[number][0]) == 5:
#             return list([[X + 7, Y + 7, 5, 4],
#                          [X + 7, Y + 22, 5, 4],
#                          [X + 14, Y + 14, 5, 4],
#                          [X + 21, Y + 7, 5, 4],
#                          [X + 21, Y + 22, 5, 4]])
#         elif int(self.all_shtick[number][0]) == 6:
#             return list([[X + 8, Y + 7, 5, 4],
#                          [X + 8, Y + 14, 5, 4],
#                          [X + 8, Y + 21, 5, 4],
#                          [X + 22, Y + 7, 5, 4],
#                          [X + 22, Y + 14, 5, 4],
#                          [X + 22, Y + 21, 5, 4]])
#
#     def return_coordinate_point_two(self, number, X, Y):
#         # Возвращаем координату точки
#         if int(self.all_shtick[number][2]) == 1:
#             return list([[X + 15, Y + 45, 5, 4]])
#         elif int(self.all_shtick[number][2]) == 2:
#             return list([[X + 8, Y + 40, 5, 4],
#                          [X + 22, Y + 50, 5, 4]])
#         elif int(self.all_shtick[number][2]) == 3:
#             return list([[X + 7, Y + 37, 5, 4],
#                          [X + 14, Y + 44, 5, 4],
#                          [X + 21, Y + 52, 5, 4]])
#         elif int(self.all_shtick[number][2]) == 4:
#             return list([[X + 8, Y + 40, 5, 4],
#                          [X + 8, Y + 50, 5, 4],
#                          [X + 22, Y + 40, 5, 4],
#                          [X + 22, Y + 50, 5, 4]])
#         elif int(self.all_shtick[number][2]) == 5:
#             return list([[X + 7, Y + 37, 5, 4],
#                          [X + 7, Y + 52, 5, 4],
#                          [X + 14, Y + 44, 5, 4],
#                          [X + 21, Y + 37, 5, 4],
#                          [X + 21, Y + 52, 5, 4]])
#         elif int(self.all_shtick[number][2]) == 6:
#             return list([[X + 8, Y + 37, 5, 4],
#                          [X + 8, Y + 44, 5, 4],
#                          [X + 8, Y + 51, 5, 4],
#                          [X + 22, Y + 37, 5, 4],
#                          [X + 22, Y + 44, 5, 4],
#                          [X + 22, Y + 51, 5, 4]])
#
#     def dont_end_game(self):
#         if self.point_team_one >= min_of_end_point:
#             return 'one'
#         elif self.point_team_two >= min_of_end_point:
#             return 'two'
#         else:
#             return 'equality'
#
#     def exam_point(self, key, number):
#         if number == 1:
#             if self.all_shtick[key][0] == '0':
#                 return False
#             else:
#                 return True
#         if number == 2:
#             if self.all_shtick[key][2] == '0':
#                 return False
#             else:
#                 return True
#
#     def start_game(self):
#         """ Непосредственно игра """
#         pygame.init()
#         dis = pygame.display.set_mode((1500, 750))
#         dis.fill(THECOLORS['lightskyblue3'])
#         pygame.display.update()
#         pygame.display.set_caption('Dominoes by SanyaCentner')
#         clock = pygame.time.Clock()
#         time_on_move = 1
#         time_to_clear_text = 1.5
#         while self.end_game:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.end_game = False
#             # Пока не конец раунда такой порядок
#             self.chip_distribution()
#             print('Раздача окончена')
#             order = self.order()
#             #             print(order)
#             # Раунд начался
#             ## Отписываем номер раунда
#             font = pygame.font.Font(None, 25)
#             text_round = font.render(f"Начинается {self.count_round}-й раунд", True, THECOLORS['black'])
#             place_text_round = text_round.get_rect(center=(750, 50))
#             dis.blit(text_round, place_text_round)
#             self.end_round = True
#             number_of_passes = 0
#             self.board = list([])
#
#             while self.end_round:
#                 ## Тут должна быть основная логика раунда: раздать фишки и чтобы каждый видел свои
#                 ## Раздаем фишки каждому и начинаем проходить по каждому человеку и отрисовывать фишки
#                 for number in order:
#                     # Отрисовываем кто делает ход
#                     text_name = font.render(f"Ход делает {self.players[number - 1].name}", True, THECOLORS['black'])
#                     place_text_name = text_name.get_rect(center=(100, 50))
#                     dis.blit(text_name, place_text_name)
#                     # Отрисовываем все фишки данного игрока
#                     text_shticks = font.render("Ваши фишки:", True, THECOLORS['black'])
#                     place_text_shticks = text_shticks.get_rect(center=(750, 670))
#                     dis.blit(text_shticks, place_text_shticks)
#                     # Отрисовываем сами фишки
#                     X_player_shticks_start = 645
#                     Y_player_shticks_start = 690
#                     # Отрисовываем закрашенную часть
#                     pygame.draw.polygon(dis, THECOLORS['white'],
#                                         [[X_player_shticks_start, Y_player_shticks_start],
#                                          [X_player_shticks_start + 210, Y_player_shticks_start],
#                                          [X_player_shticks_start + 210, Y_player_shticks_start + 60],
#                                          [X_player_shticks_start, Y_player_shticks_start + 60]])
#                     for dominoes in self.players[number - 1].shticks:
#                         # Отрисовываем точки, если там нуль, то отрисовываем только нижнее
#                         if dominoes not in [1, 2, 3, 4, 5, 6, 7]:
#                             for lst_one in self.return_coordinate_point_one(dominoes, X_player_shticks_start,
#                                                                             Y_player_shticks_start):
#                                 pygame.draw.rect(dis, THECOLORS['black'], lst_one)
#                         if dominoes != 1:
#                             for lst_two in self.return_coordinate_point_two(dominoes, X_player_shticks_start,
#                                                                             Y_player_shticks_start):
#                                 pygame.draw.rect(dis, THECOLORS['black'], lst_two)
#                         # Переходим к следущей координате
#                         X_player_shticks_start = X_player_shticks_start + 30
#                         pygame.draw.line(dis, THECOLORS['black'], [X_player_shticks_start, 690],
#                                          [X_player_shticks_start, 750])
#
#                         pygame.draw.line(dis, THECOLORS['black'], [645, 720], [855, 720])
#                         pygame.display.update()
#                         clock.tick(time_to_clear_text)
#
#                     # Закрашиваем верхнюю часть с именем человека
#                     pos_var = self.put_a_chip(number - 1)
#
#                     print(f"Какие фишки возможно поставить {pos_var}")
#                     print(f"Какие элементы на столе {self.board}")
#                     if pos_var != list([[], None, None]):
#                         number_of_passes = 0
#                         tmp = True
#                         while tmp:
#                             for event in pygame.event.get():
#                                 if event.type == pygame.QUIT:
#                                     self.end_round = False
#                                 #                                 print('мы внутри')
#                                 # Теперь человек выбирает фишку и мы ее отрисуем
#                                 if event.type == pygame.KEYDOWN:
#                                     # Чел выбирает фишку и проводим проверку можно ли ее ставить
#                                     if event.key == pygame.K_1:
#                                         tmp_num = 0
#                                     elif event.key == pygame.K_2:
#                                         tmp_num = 1
#                                     elif event.key == pygame.K_3:
#                                         tmp_num = 2
#                                     elif event.key == pygame.K_4:
#                                         tmp_num = 3
#                                     elif event.key == pygame.K_5:
#                                         tmp_num = 4
#                                     elif event.key == pygame.K_6:
#                                         tmp_num = 5
#                                     elif event.key == pygame.K_7:
#                                         tmp_num = 6
#
#                                     if event.key == pygame.K_LEFT:
#                                         # Если возвращается 1, то это дубль, если 2, то обычная фишка
#                                         doubles_, key = self.examination_number_shtics(tmp_num,
#                                                                                        self.players[number - 1].shticks[
#                                                                                            tmp_num],
#                                                                                        'left', pos_var)
#                                         if doubles_ == 1:
#                                             print('мы внутри номера', tmp_num)
#                                             pygame.draw.polygon(dis, THECOLORS['white'],
#                                                                 [[self.X_left - 30, self.Y_doubles],
#                                                                  [self.X_left, self.Y_doubles],
#                                                                  [self.X_left, self.Y_doubles + 60],
#                                                                  [self.X_left - 30, self.Y_doubles + 60]])
#                                             pygame.draw.line(dis, THECOLORS['black'],
#                                                              [self.X_left - 30, self.Y_doubles + 30],
#                                                              [self.X_left, self.Y_doubles + 30])
#
#                                             self.board.insert(0, key)
#                                             self.players[number - 1].shticks.remove(
#                                                 self.players[number - 1].shticks[tmp_num])
#                                             self.players[number - 1].count_shticks -= 1
#                                             # Отрисовывание точек
#                                             if self.exam_point(key, 1):
#                                                 for lst_one in self.return_coordinate_point_one(key,
#                                                                                                 self.X_left - 30,
#                                                                                                 self.Y_doubles):
#                                                     pygame.draw.rect(dis, THECOLORS['black'], lst_one)
#                                             if self.exam_point(key, 2):
#                                                 for lst_two in self.return_coordinate_point_two(key,
#                                                                                                 self.X_left - 30,
#                                                                                                 self.Y_doubles):
#                                                     pygame.draw.rect(dis, THECOLORS['black'], lst_two)
#                                             self.X_left -= 30
#                                             pygame.display.update()
#                                             clock.tick(time_to_clear_text)
#                                             tmp = False
#                                             break
#
#                                         elif doubles_ == 2:
#                                             pygame.draw.polygon(dis, THECOLORS['white'],
#                                                                 [[self.X_left - 60, self.Y_not_doubles],
#                                                                  [self.X_left, self.Y_not_doubles],
#                                                                  [self.X_left, self.Y_not_doubles + 30],
#                                                                  [self.X_left - 60, self.Y_not_doubles + 30]])
#                                             pygame.draw.line(dis, THECOLORS['black'],
#                                                              [self.X_left - 30, self.Y_not_doubles],
#                                                              [self.X_left - 30, self.Y_not_doubles + 30])
#                                             self.board.insert(0, key)
#                                             self.players[number - 1].shticks.remove(
#                                                 self.players[number - 1].shticks[tmp_num])
#                                             self.players[number - 1].count_shticks -= 1
#                                             if self.exam_point(key, 1):
#                                                 for lst_one in self.return_coordinate_point_one(key,
#                                                                                                 self.X_left - 60,
#                                                                                                 self.Y_not_doubles):
#                                                     pygame.draw.rect(dis, THECOLORS['black'], lst_one)
#                                             if self.exam_point(key, 2):
#                                                 for lst_two in self.return_coordinate_point_two(key,
#                                                                                                 self.X_left - 30,
#                                                                                                 self.Y_not_doubles - 30):
#                                                     pygame.draw.rect(dis, THECOLORS['black'], lst_two)
#                                             self.X_left -= 60
#                                             pygame.display.update()
#                                             clock.tick(time_to_clear_text)
#                                             tmp = False
#                                             break
#
#                                     elif event.key == pygame.K_RIGHT:
#                                         doubles_, key = self.examination_number_shtics(tmp_num,
#                                                                                        self.players[number - 1].shticks[
#                                                                                            tmp_num],
#                                                                                        'right', pos_var)
#                                         # Если возвращается 1, то это дубль, если 2, то обычная фишка
#                                         if doubles_ == 1:
#                                             pygame.draw.polygon(dis, THECOLORS['white'],
#                                                                 [[self.X_right, self.Y_doubles],
#                                                                  [self.X_right + 30, self.Y_doubles],
#                                                                  [self.X_right + 30, self.Y_doubles + 60],
#                                                                  [self.X_right, self.Y_doubles + 60]])
#                                             pygame.draw.line(dis, THECOLORS['black'],
#                                                              [self.X_right, self.Y_doubles + 30],
#                                                              [self.X_right + 30, self.Y_doubles + 30])
#                                             self.board.append(key)
#                                             self.players[number - 1].shticks.remove(
#                                                 self.players[number - 1].shticks[tmp_num])
#                                             self.players[number - 1].count_shticks -= 1
#                                             if self.exam_point(key, 1):
#                                                 for lst_one in self.return_coordinate_point_one(key,
#                                                                                                 self.X_right,
#                                                                                                 self.Y_doubles):
#                                                     pygame.draw.rect(dis, THECOLORS['black'], lst_one)
#                                             if self.exam_point(key, 2):
#                                                 for lst_two in self.return_coordinate_point_two(key,
#                                                                                                 self.X_right,
#                                                                                                 self.Y_doubles):
#                                                     pygame.draw.rect(dis, THECOLORS['black'], lst_two)
#                                             self.X_right += 30
#                                             pygame.display.update()
#                                             clock.tick(time_to_clear_text)
#                                             tmp = False
#                                             break
#
#                                         elif doubles_ == 2:
#                                             pygame.draw.polygon(dis, THECOLORS['white'],
#                                                                 [[self.X_right, self.Y_not_doubles],
#                                                                  [self.X_right + 60, self.Y_not_doubles],
#                                                                  [self.X_right + 60, self.Y_not_doubles + 30],
#                                                                  [self.X_right, self.Y_not_doubles + 30]])
#                                             pygame.draw.line(dis, THECOLORS['black'],
#                                                              [self.X_right + 30, self.Y_not_doubles],
#                                                              [self.X_right + 30, self.Y_not_doubles + 30])
#                                             self.board.append(key)
#                                             self.players[number - 1].shticks.remove(
#                                                 self.players[number - 1].shticks[tmp_num])
#                                             self.players[number - 1].count_shticks -= 1
#                                             if self.exam_point(key, 1):
#                                                 for lst_one in self.return_coordinate_point_one(key,
#                                                                                                 self.X_right,
#                                                                                                 self.Y_not_doubles):
#                                                     pygame.draw.rect(dis, THECOLORS['black'], lst_one)
#                                             if self.exam_point(key, 2):
#                                                 for lst_two in self.return_coordinate_point_two(key,
#                                                                                                 self.X_right + 30,
#                                                                                                 self.Y_not_doubles - 30):
#                                                     pygame.draw.rect(dis, THECOLORS['black'], lst_two)
#                                             self.X_right += 60
#                                             pygame.display.update()
#                                             clock.tick(time_to_clear_text)
#                                             tmp = False
#
#                     else:
#                         number_of_passes += 1
#
#                     clock.tick(time_on_move)
#                     pygame.draw.polygon(dis, THECOLORS['lightskyblue3'],
#                                         [[0, 0], [200, 0],
#                                          [200, 75], [0, 75]])
#                     pygame.display.update()
#
#                     if self.dont_end_round(number_of_passes, number - 1) == True and len(self.board) > 10:
#                         pygame.draw.polygon(dis, THECOLORS['lightskyblue3'],
#                                             [[0, 0], [1500, 0], [1500, 750], [0, 750]])
#                         print(f"Количество очков у команд {self.point_team_one} и {self.point_team_two}")
#                         print(
#                             f"Какие фишки у кого остались {self.gamer_one.shticks, self.gamer_two.shticks, self.gamer_three.shticks, self.gamer_four.shticks}")
#                         self.X_right = 750
#                         self.X_left = 750
#                         self.end_round = False
#                         break
#                 print('раунд закончился')
#                 print(self.end_round)
#
#             if self.dont_end_game() == 'one':
#                 pygame.draw.polygon(dis, THECOLORS['lightskyblue3'],
#                                     [[0, 0], [1500, 0], [1500, 750], [0, 750]])
#                 text_round = font.render("Выиграла первая команда", True, THECOLORS['black'])
#                 place_text_round = text_round.get_rect(center=(750, 50))
#                 dis.blit(text_round, place_text_round)
#             elif self.dont_end_game() == 'two':
#                 pygame.draw.polygon(dis, THECOLORS['lightskyblue3'],
#                                     [[0, 0], [1500, 0], [1500, 750], [0, 750]])
#                 text_round = font.render("Выиграла вторая команда", True, THECOLORS['black'])
#                 place_text_round = text_round.get_rect(center=(750, 50))
#                 dis.blit(text_round, place_text_round)
#
#         pygame.quit()
#         quit()
        # self.start_round()

class Game:
    """Основная часть игры"""

    min_of_end_point = 101

    def __init__(self):
        self.board = list([])
        self.count_round = 1
        self.number_first_move = 0
        self.point_team_one = 100
        self.point_team_two = 100
        self.end_round = True
        self.end_game = True
        self.all_shtick = {1: "0-0", 2: "0-1", 3: "0-2", 4: "0-3", 5: "0-4", 6: "0-5", 7: "0-6",
                           8: "1-1", 9: "1-2", 10: "1-3", 11: "1-4", 12: "1-5", 13: "1-6",
                           14: "2-2", 15: "2-3", 16: "2-4", 17: "2-5", 18: "2-6",
                           19: "3-3", 20: "3-4", 21: "3-5", 22: "3-6",
                           23: "4-4", 24: "4-5", 25: "4-6",
                           26: "5-5", 27: "5-6",
                           28: "6-6",
                           29: "0-0", 30: "1-0", 31: "2-0", 32: "3-0", 33: "4-0", 34: "5-0", 35: "6-0",
                           36: "1-1", 37: "2-1", 38: "3-1", 39: "4-1", 40: "5-1", 41: "6-1",
                           42: "2-2", 43: "3-2", 44: "4-2", 45: "5-2", 46: "6-2",
                           47: "3-3", 48: "4-3", 49: "5-3", 50: "6-3",
                           51: "4-4", 52: "5-4", 53: "6-4",
                           54: "5-5", 55: "6-5",
                           56: "6-6"}
        self.doubles = [1, 8, 14, 19, 23, 26, 28]
        # self.X_right = 750
        # self.X_left = 750
        # self.Y_doubles = 345
        # self.Y_not_doubles = 360

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

    def find_first_move(self, players):
        """ Выбор игрока, у которого 1-1 """
        tmp = 1
        for player in players:
            for elem in player.shticks:
                if elem == 8:
                    return self.match_list(tmp)
            tmp += 1

    def order(self, players):
        """Возвращаем порядок"""
        if self.count_round == 1:
            return self.find_first_move(players)
        else:
            return self.match_list(self.number_first_move)

    def chip_distribution(self):
        """ Раздача фишек и возврат """
        tmp = list(range(1, 29))
        random.shuffle(tmp)

        if (self.examination_distribution(tmp) == True):
            return tmp
        else:
            return self.chip_distribution()

    def options(self, value, side):
        """Возможные варианты которые можно поставить"""
        tmp_lst = list([])
        if len(self.board) != 0:
            if side == 'left':
                for key in self.all_shtick:
                    if ((self.all_shtick[key][2] == self.all_shtick[self.board[0]][0]) and
                            (self.all_shtick[key] != self.all_shtick[self.board[0]])):
                        tmp_lst.append(key)
            elif side == 'right':
                for key in self.all_shtick:
                    if ((self.all_shtick[key][0] == self.all_shtick[self.board[-1]][2]) and
                            (self.all_shtick[key] != self.all_shtick[self.board[-1]])):
                        tmp_lst.append(key)
        return tmp_lst
    #
    def examination_number_shtics(self, number, key, side, variable):
        """Фишка была выбрана и теперь мы пытаемся ее ставить"""

        ## Здесь можно поставить фишку и справа, и слева, поэтому надо предлагать игроку какой-то выбор и выводить
        ##доску на экран чтобы он понимал куда можно поставить
        print('мы зашли в функцию')
        print(f"Какой номер из player берем {number}, какая фишка передается {key}, {variable}")
        for var in variable:
            if var[0][0] == number and var[0][1] == side and var[1] == True and var[2] == True:
                return (1, key + 28)
            if var[0][0] == number and var[0][1] == side and var[1] == True and var[2] == False:
                return (1, key)
            if var[0][0] == number and var[0][1] == side and var[1] == False and var[2] == True:
                return (2, key + 28)
            if var[0][0] == number and var[0][1] == side and var[1] == False and var[2] == False:
                return (2, key)

    def summ_points(self, player_first, player_second):
        """ Считаем количество очков"""
        count = 0
        for shtick in player_first.shticks:
            count += int(self.all_shtick[shtick][0]) + int(self.all_shtick[shtick][2])
            print(f"Какая фишка {self.all_shtick[shtick]}, Сумма очков {count}")
        for shtick in player_second.shticks:
            count += int(self.all_shtick[shtick][0]) + int(self.all_shtick[shtick][2])
            print(f"Какая фишка {self.all_shtick[shtick]}, Сумма очков {count}")
        return count

    def dont_end_round(self, passes, number_of_player, players):
        """ Проверяем кончился ли раунд?"""
        ## Проверяем рыбу
        # print("Проверяем конец раунда")
        # if passes == 4:
        #     self.number_first_move = number_of_player
        #     self.count_round += 1
        #     team_one = self.summ_points(players[0], players[2])
        #     team_two = self.summ_points(players[1], players[3])
        #     if team_one == team_two:
        #         self.point_team_one += team_one
        #         self.point_team_two += team_two
        #     elif team_one > team_two:
        #         self.point_team_one += team_one
        #     elif team_one < team_two:
        #         self.point_team_two += team_two
        #     return True

        ## Проверяем конец раунда в целом
        for count in range(0, 4):
            print('ну что же, мы внутри')
            if len(players[count].shticks) == 0:
                print(f"номер игрока {count}, сам игрок {players[count].name}")
                self.number_first_move = count + 1
                self.count_round += 1
                if count == 2 or count == 4:
                    self.point_team_one += self.summ_points(players[0], players[2])
                elif count == 1 or count == 3:
                    self.point_team_two += self.summ_points(players[1], players[3])
                return True

        return False

    def possible_chips_that_can_be_placed(self, player):
        """ Отслеживаем номер фишки и куда ее поставить"""

        ## Здесь можно поставить фишку и справа, и слева, поэтому надо предлагать игроку какой-то выбор и выводить
        ##доску на экран чтобы он понимал куда можно поставить
        lst_possible = list([])
        # lst_tmp = list([])
        # Это условие для нового раунда и чел может поставить что хочет
        if len(self.board) == 0:
            for elem in player.shticks:
                if elem in self.doubles:
                    lst_possible.append([[player.shticks.index(elem), 'left'], True, False])
                    lst_possible.append([[player.shticks.index(elem), 'right'], True, False])
                else:
                    lst_possible.append([[player.shticks.index(elem), 'left'], False, False])
                    lst_possible.append([[player.shticks.index(elem), 'right'], False, False])
            return lst_possible

        options_on_the_left = self.options(self.board[0], 'left')
        options_on_the_right = self.options(self.board[-1], 'right')
        #         print('Номера, которые можно поставить слева', options_on_the_left)
        #         print('Номера, которые можно поставить справа', options_on_the_right)

        for elem in player.shticks:
            if elem in options_on_the_left and elem in options_on_the_right:
                if elem in self.doubles:
                    lst_possible.append([[player.shticks.index(elem), 'left'], True, False])
                    lst_possible.append([[player.shticks.index(elem), 'right'], True, False])
                else:
                    lst_possible.append([[player.shticks.index(elem), 'left'], False, False])
                    lst_possible.append([[player.shticks.index(elem), 'right'], False, False])
            elif elem in options_on_the_left:
                if elem in self.doubles:
                    lst_possible.append([[player.shticks.index(elem), 'left'], True, False])
                else:
                    lst_possible.append([[player.shticks.index(elem), 'left'], False, False])
            elif elem in options_on_the_right:
                if elem in self.doubles:
                    lst_possible.append([[player.shticks.index(elem), 'right'], True, False])
                else:
                    lst_possible.append([[player.shticks.index(elem), 'right'], False, False])

        for elem in player.shticks:
            if elem + 28 in options_on_the_left and elem + 28 in options_on_the_right:
                if elem in self.doubles:
                    lst_possible.append([[player.shticks.index(elem), 'left'], True, True])
                    lst_possible.append([[player.shticks.index(elem), 'right'], True, True])
                else:
                    lst_possible.append([[player.shticks.index(elem), 'left'], False, True])
                    lst_possible.append([[player.shticks.index(elem), 'right'], False, True])
            elif elem + 28 in options_on_the_left:
                if elem in self.doubles:
                    lst_possible.append([[player.shticks.index(elem), 'left'], True, True])
                else:
                    lst_possible.append([[player.shticks.index(elem), 'left'], False, True])
            elif elem + 28 in options_on_the_right:
                if elem in self.doubles:
                    lst_possible.append([[player.shticks.index(elem), 'right'], True, True])
                else:
                    lst_possible.append([[player.shticks.index(elem), 'right'], False, True])
        if len(lst_possible) == 0:
            return ([[], None, None])
        return lst_possible

    def put_a_chip(self, number_of_player, players):
        """ Выбор фишки, которую можно поставить"""
        if self.count_round == 1 and 8 not in self.board:
            n = players[number_of_player].shticks.index(8)
            return [[[n, 'right'], True, False], [[n, 'left'], True, False]]
        else:
            return self.possible_chips_that_can_be_placed(players[number_of_player])

    def dont_end_game(self):
        if self.point_team_one >= Game.min_of_end_point:
            return 'two'
        elif self.point_team_two >= Game.min_of_end_point:
            return 'one'

    def exam_point(self, key, number):
        if number == 1:
            if self.all_shtick[key][0] == '0':
                return False
            else:
                return True
        if number == 2:
            if self.all_shtick[key][2] == '0':
                return False
            else:
                return True

    def start_game(self):
        """ Непосредственно игра """
        pygame.init()
        dis = pygame.display.set_mode((1500, 750))
        dis.fill(THECOLORS['lightskyblue3'])
        pygame.display.update()
        pygame.display.set_caption('Dominoes by SanyaCentner')
        clock = pygame.time.Clock()
        time_on_move = 1
        time_to_clear_text = 1.5
        while self.end_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end_game = False
            # Пока не конец раунда такой порядок
            self.chip_distribution()
            print('Раздача окончена')
            order = self.order()
            #             print(order)
            # Раунд начался
            ## Отписываем номер раунда
            font = pygame.font.Font(None, 25)
            text_round = font.render(f"Начинается {self.count_round}-й раунд", True, THECOLORS['black'])
            place_text_round = text_round.get_rect(center=(750, 50))
            dis.blit(text_round, place_text_round)
            self.end_round = True
            number_of_passes = 0
            self.board = list([])

            while self.end_round:
                ## Тут должна быть основная логика раунда: раздать фишки и чтобы каждый видел свои
                ## Раздаем фишки каждому и начинаем проходить по каждому человеку и отрисовывать фишки
                for number in order:
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

                    # Закрашиваем верхнюю часть с именем человека
                    pos_var = self.put_a_chip(number - 1)

                    print(f"Какие фишки возможно поставить {pos_var}")
                    print(f"Какие элементы на столе {self.board}")
                    if pos_var != list([[], None, None]):
                        number_of_passes = 0
                        tmp = True
                        while tmp:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    self.end_round = False
                                #                                 print('мы внутри')
                                # Теперь человек выбирает фишку и мы ее отрисуем
                                if event.type == pygame.KEYDOWN:
                                    # Чел выбирает фишку и проводим проверку можно ли ее ставить
                                    if event.key == pygame.K_1:
                                        tmp_num = 0
                                    elif event.key == pygame.K_2:
                                        tmp_num = 1
                                    elif event.key == pygame.K_3:
                                        tmp_num = 2
                                    elif event.key == pygame.K_4:
                                        tmp_num = 3
                                    elif event.key == pygame.K_5:
                                        tmp_num = 4
                                    elif event.key == pygame.K_6:
                                        tmp_num = 5
                                    elif event.key == pygame.K_7:
                                        tmp_num = 6

                                    if event.key == pygame.K_LEFT:
                                        # Если возвращается 1, то это дубль, если 2, то обычная фишка
                                        doubles_, key = self.examination_number_shtics(tmp_num,
                                                                                       self.players[number - 1].shticks[
                                                                                           tmp_num],
                                                                                       'left', pos_var)
                                        if doubles_ == 1:
                                            print('мы внутри номера', tmp_num)
                                            pygame.draw.polygon(dis, THECOLORS['white'],
                                                                [[self.X_left - 30, self.Y_doubles],
                                                                 [self.X_left, self.Y_doubles],
                                                                 [self.X_left, self.Y_doubles + 60],
                                                                 [self.X_left - 30, self.Y_doubles + 60]])
                                            pygame.draw.line(dis, THECOLORS['black'],
                                                             [self.X_left - 30, self.Y_doubles + 30],
                                                             [self.X_left, self.Y_doubles + 30])

                                            self.board.insert(0, key)
                                            self.players[number - 1].shticks.remove(
                                                self.players[number - 1].shticks[tmp_num])
                                            self.players[number - 1].count_shticks -= 1
                                            # Отрисовывание точек
                                            if self.exam_point(key, 1):
                                                for lst_one in self.return_coordinate_point_one(key,
                                                                                                self.X_left - 30,
                                                                                                self.Y_doubles):
                                                    pygame.draw.rect(dis, THECOLORS['black'], lst_one)
                                            if self.exam_point(key, 2):
                                                for lst_two in self.return_coordinate_point_two(key,
                                                                                                self.X_left - 30,
                                                                                                self.Y_doubles):
                                                    pygame.draw.rect(dis, THECOLORS['black'], lst_two)
                                            self.X_left -= 30
                                            pygame.display.update()
                                            clock.tick(time_to_clear_text)
                                            tmp = False
                                            break

                                        elif doubles_ == 2:
                                            pygame.draw.polygon(dis, THECOLORS['white'],
                                                                [[self.X_left - 60, self.Y_not_doubles],
                                                                 [self.X_left, self.Y_not_doubles],
                                                                 [self.X_left, self.Y_not_doubles + 30],
                                                                 [self.X_left - 60, self.Y_not_doubles + 30]])
                                            pygame.draw.line(dis, THECOLORS['black'],
                                                             [self.X_left - 30, self.Y_not_doubles],
                                                             [self.X_left - 30, self.Y_not_doubles + 30])
                                            self.board.insert(0, key)
                                            self.players[number - 1].shticks.remove(
                                                self.players[number - 1].shticks[tmp_num])
                                            self.players[number - 1].count_shticks -= 1
                                            if self.exam_point(key, 1):
                                                for lst_one in self.return_coordinate_point_one(key,
                                                                                                self.X_left - 60,
                                                                                                self.Y_not_doubles):
                                                    pygame.draw.rect(dis, THECOLORS['black'], lst_one)
                                            if self.exam_point(key, 2):
                                                for lst_two in self.return_coordinate_point_two(key,
                                                                                                self.X_left - 30,
                                                                                                self.Y_not_doubles - 30):
                                                    pygame.draw.rect(dis, THECOLORS['black'], lst_two)
                                            self.X_left -= 60
                                            pygame.display.update()
                                            clock.tick(time_to_clear_text)
                                            tmp = False
                                            break

                                    elif event.key == pygame.K_RIGHT:
                                        doubles_, key = self.examination_number_shtics(tmp_num,
                                                                                       self.players[number - 1].shticks[
                                                                                           tmp_num],
                                                                                       'right', pos_var)
                                        # Если возвращается 1, то это дубль, если 2, то обычная фишка
                                        if doubles_ == 1:
                                            pygame.draw.polygon(dis, THECOLORS['white'],
                                                                [[self.X_right, self.Y_doubles],
                                                                 [self.X_right + 30, self.Y_doubles],
                                                                 [self.X_right + 30, self.Y_doubles + 60],
                                                                 [self.X_right, self.Y_doubles + 60]])
                                            pygame.draw.line(dis, THECOLORS['black'],
                                                             [self.X_right, self.Y_doubles + 30],
                                                             [self.X_right + 30, self.Y_doubles + 30])
                                            self.board.append(key)
                                            self.players[number - 1].shticks.remove(
                                                self.players[number - 1].shticks[tmp_num])
                                            self.players[number - 1].count_shticks -= 1
                                            if self.exam_point(key, 1):
                                                for lst_one in self.return_coordinate_point_one(key,
                                                                                                self.X_right,
                                                                                                self.Y_doubles):
                                                    pygame.draw.rect(dis, THECOLORS['black'], lst_one)
                                            if self.exam_point(key, 2):
                                                for lst_two in self.return_coordinate_point_two(key,
                                                                                                self.X_right,
                                                                                                self.Y_doubles):
                                                    pygame.draw.rect(dis, THECOLORS['black'], lst_two)
                                            self.X_right += 30
                                            pygame.display.update()
                                            clock.tick(time_to_clear_text)
                                            tmp = False
                                            break

                                        elif doubles_ == 2:
                                            pygame.draw.polygon(dis, THECOLORS['white'],
                                                                [[self.X_right, self.Y_not_doubles],
                                                                 [self.X_right + 60, self.Y_not_doubles],
                                                                 [self.X_right + 60, self.Y_not_doubles + 30],
                                                                 [self.X_right, self.Y_not_doubles + 30]])
                                            pygame.draw.line(dis, THECOLORS['black'],
                                                             [self.X_right + 30, self.Y_not_doubles],
                                                             [self.X_right + 30, self.Y_not_doubles + 30])
                                            self.board.append(key)
                                            self.players[number - 1].shticks.remove(
                                                self.players[number - 1].shticks[tmp_num])
                                            self.players[number - 1].count_shticks -= 1
                                            if self.exam_point(key, 1):
                                                for lst_one in self.return_coordinate_point_one(key,
                                                                                                self.X_right,
                                                                                                self.Y_not_doubles):
                                                    pygame.draw.rect(dis, THECOLORS['black'], lst_one)
                                            if self.exam_point(key, 2):
                                                for lst_two in self.return_coordinate_point_two(key,
                                                                                                self.X_right + 30,
                                                                                                self.Y_not_doubles - 30):
                                                    pygame.draw.rect(dis, THECOLORS['black'], lst_two)
                                            self.X_right += 60
                                            pygame.display.update()
                                            clock.tick(time_to_clear_text)
                                            tmp = False

                    else:
                        number_of_passes += 1

                    clock.tick(time_on_move)
                    pygame.draw.polygon(dis, THECOLORS['lightskyblue3'],
                                        [[0, 0], [200, 0],
                                         [200, 75], [0, 75]])
                    pygame.display.update()

                    if self.dont_end_round(number_of_passes, number - 1) == True and len(self.board) > 10:
                        pygame.draw.polygon(dis, THECOLORS['lightskyblue3'],
                                            [[0, 0], [1500, 0], [1500, 750], [0, 750]])
                        print(f"Количество очков у команд {self.point_team_one} и {self.point_team_two}")
                        print(
                            f"Какие фишки у кого остались {self.gamer_one.shticks, self.gamer_two.shticks, self.gamer_three.shticks, self.gamer_four.shticks}")
                        self.X_right = 750
                        self.X_left = 750
                        self.end_round = False
                        break
                print('раунд закончился')
                print(self.end_round)

            if self.dont_end_game() == 'one':
                pygame.draw.polygon(dis, THECOLORS['lightskyblue3'],
                                    [[0, 0], [1500, 0], [1500, 750], [0, 750]])
                text_round = font.render("Выиграла первая команда", True, THECOLORS['black'])
                place_text_round = text_round.get_rect(center=(750, 50))
                dis.blit(text_round, place_text_round)
            elif self.dont_end_game() == 'two':
                pygame.draw.polygon(dis, THECOLORS['lightskyblue3'],
                                    [[0, 0], [1500, 0], [1500, 750], [0, 750]])
                text_round = font.render("Выиграла вторая команда", True, THECOLORS['black'])
                place_text_round = text_round.get_rect(center=(750, 50))
                dis.blit(text_round, place_text_round)

        pygame.quit()
        quit()





