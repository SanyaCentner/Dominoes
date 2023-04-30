import socket
import pygame
from pygame.color import THECOLORS

# class Client ():
from Board import Board

class client_Vova:

    def __init__(self):
        self.board = Board()
        self.X_right = 0
        self.X_left = 0
        self.Y_doubles = 345
        self.Y_not_doubles = 360
        # self.board_client = list([])
        # self.position_of_the_first_сhip = 0

    def exam(self, number_in_deck, side_in_deck, var_of_position):
        """Проверяем можно ли поставить нужную фишку"""
        print('Зашли в функцию проверки выбранной фишки')
        for elem in var_of_position:
            print(f"какие варианты {elem}, какую фишку {number_in_deck}, с какой стороны {side_in_deck}")
            if number_in_deck == elem[0][0] and side_in_deck == elem[0][1]:
                return True
        return False

    def examination_number_shtics(self, number, key, side, variable):
        """Фишка была выбрана и теперь мы пытаемся ее ставить"""

        # Здесь можно поставить фишку и справа, и слева, поэтому надо предлагать игроку какой-то выбор и выводить
        # доску на экран чтобы он понимал куда можно поставить
        print('мы зашли в функцию')
        print(f"Какой номер из player берем {number}, какая фишка передается {key}, {type(variable)},"
              f"на какую сторону ставим {side}")
        for var in variable:
            print(var)
            if var[0][0] == number and var[0][1] == side and var[1] == True and var[2] == True:
                return (1, key + 28)
            if var[0][0] == number and var[0][1] == side and var[1] == True and var[2] == False:
                return (1, key)
            if var[0][0] == number and var[0][1] == side and var[1] == False and var[2] == True:
                return (2, key + 28)
            if var[0][0] == number and var[0][1] == side and var[1] == False and var[2] == False:
                return (2, key)

    def exam_point(self, key, number):
        """Передаем фишку и проверяем нули"""
        if number == 1:
            if self.board.all_shtick[key][0] == '0':
                return False
            else:
                return True
        if number == 2:
            if self.board.all_shtick[key][2] == '0':
                return False
            else:
                return True

    def start_client(self):
        WIDTH_WINDOW, HEIGHT_WINDOW = 1500, 750
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Отключаем алгоритм Нейгла
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        sock.connect(('localhost', 10000))
        sock.send('name_Vova'.encode())
        # Отрисовываем
        pygame.init()
        dis = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))
        dis.fill(THECOLORS['lightskyblue3'])
        pygame.display.update()
        pygame.display.set_caption('Dominoes by SanyaCentner')
        clock = pygame.time.Clock()
        running = True
        font = pygame.font.Font(None, 25)
        # Отписываем что за игрок в целом
        text_name = font.render('Я игрок Вова', True, THECOLORS['black'])
        place_text_name = text_name.get_rect(center=(100, 25))
        dis.blit(text_name, place_text_name)
        pygame.display.update()
        while running:
            # Получаем от сервера какие фишки куда можно поставить
            data1 = sock.recv(1024)
            data1 = data1.decode()
            print(f"что получили {data1}, {type(data1)}")
            try:
                data = eval(data1)
            except:
                data = data1[0: data1.find('}') + 1]
                print('Сработал try', data)
                data = eval(data)
            # Очистим все поле
            pygame.draw.polygon(dis, THECOLORS['lightskyblue3'],
                                [[0, 0], [WIDTH_WINDOW, 0], [WIDTH_WINDOW, HEIGHT_WINDOW], [0, HEIGHT_WINDOW]])
            # Отписываем что за игрок в целом
            text_name = font.render('Я игрок Вова', True, THECOLORS['black'])
            place_text_name = text_name.get_rect(center=(100, 25))
            dis.blit(text_name, place_text_name)
            # Отрисовываем кто делает ход
            text_name = font.render(f"Ход делает {data['name']}", True, THECOLORS['black'])
            place_text_name = text_name.get_rect(center=(100, 50))
            dis.blit(text_name, place_text_name)
            # Отписываем какой счет между командами
            text_name = font.render(f"CC {data['point_team_one']} : ВВ {data['point_team_two']}", True,
                                    THECOLORS['black'])
            place_text_name = text_name.get_rect(center=(1000, 50))
            dis.blit(text_name, place_text_name)
            # Отрисовываем какой раунд
            text_round = font.render(f"Начинается {data['count_of_round']}-й раунд", True, THECOLORS['black'])
            place_text_round = text_round.get_rect(center=(750, 50))
            dis.blit(text_round, place_text_round)
            # Отрисовываем все фишки данного игрока
            text_shticks = font.render("Ваши фишки:", True, THECOLORS['black'])
            place_text_shticks = text_shticks.get_rect(center=(750, 670))
            dis.blit(text_shticks, place_text_shticks)
            # Отрисовываем сами фишки
            X_player_shticks_start = 645
            Y_player_shticks_start = 690
            for dominoes in data['shticks']:
                pygame.draw.polygon(dis, THECOLORS['white'],
                                    [[X_player_shticks_start, Y_player_shticks_start],
                                     [X_player_shticks_start + 30, Y_player_shticks_start],
                                     [X_player_shticks_start + 30, Y_player_shticks_start + 60],
                                     [X_player_shticks_start, Y_player_shticks_start + 60]])
                # Отрисовываем точки, если там нуль, то отрисовываем только нижнее
                if dominoes not in [1, 2, 3, 4, 5, 6, 7]:
                    for lst_one in self.board.return_coordinate_point_one(dominoes, X_player_shticks_start,
                                                                    Y_player_shticks_start):
                        pygame.draw.rect(dis, THECOLORS['black'], lst_one)
                if dominoes != 1:
                    for lst_two in self.board.return_coordinate_point_two(dominoes, X_player_shticks_start,
                                                                    Y_player_shticks_start):
                        pygame.draw.rect(dis, THECOLORS['black'], lst_two)

                pygame.draw.line(dis, THECOLORS['black'], [X_player_shticks_start, 720],
                                 [X_player_shticks_start + 30, 720])
                pygame.draw.line(dis, THECOLORS['black'], [X_player_shticks_start, 690],
                                 [X_player_shticks_start, 750])
                # Переходим к следущей координате
                X_player_shticks_start += 30
                pygame.display.update()
                clock.tick(20)
            # Отрисовываем фишки на доске
            self.X_right = 0
            for elem in data['board']:
                if elem in [1, 8, 14, 19, 23, 26, 28]:
                    pygame.draw.polygon(dis, THECOLORS['white'],
                                        [[self.X_right, self.Y_doubles],
                                         [self.X_right + 30, self.Y_doubles],
                                         [self.X_right + 30, self.Y_doubles + 60],
                                         [self.X_right, self.Y_doubles + 60]])
                    pygame.draw.line(dis, THECOLORS['black'],
                                     [self.X_right, self.Y_doubles + 30],
                                     [self.X_right + 30, self.Y_doubles + 30])
                    # Отрисовывание точек
                    if self.exam_point(elem, 1):
                        for lst_one in self.board.return_coordinate_point_one(elem,
                                                                              self.X_right,
                                                                              self.Y_doubles):
                            pygame.draw.rect(dis, THECOLORS['black'], lst_one)
                    if self.exam_point(elem, 2):
                        for lst_two in self.board.return_coordinate_point_two(elem,
                                                                              self.X_right,
                                                                              self.Y_doubles):
                            pygame.draw.rect(dis, THECOLORS['black'], lst_two)
                    self.X_right += 30
                    pygame.display.update()
                    clock.tick(20)
                else:
                    pygame.draw.polygon(dis, THECOLORS['white'],
                                        [[self.X_right, self.Y_not_doubles],
                                         [self.X_right + 60, self.Y_not_doubles],
                                         [self.X_right + 60, self.Y_not_doubles + 30],
                                         [self.X_right, self.Y_not_doubles + 30]])
                    pygame.draw.line(dis, THECOLORS['black'],
                                     [self.X_right + 30, self.Y_not_doubles],
                                     [self.X_right + 30, self.Y_not_doubles + 30])
                    if self.exam_point(elem, 1):
                        for lst_one in self.board.return_coordinate_point_one(elem,
                                                                              self.X_right,
                                                                              self.Y_not_doubles):
                            pygame.draw.rect(dis, THECOLORS['black'], lst_one)
                    if self.exam_point(elem, 2):
                        for lst_two in self.board.return_coordinate_point_two(elem,
                                                                              self.X_right + 30,
                                                                              self.Y_not_doubles - 30):
                            pygame.draw.rect(dis, THECOLORS['black'], lst_two)
                    self.X_right += 60
                    pygame.display.update()
                    clock.tick(20)
            # Теперь выбираем фишку и должны ее поставить
            if data['pos'] != list([[], None, None]):
                tmp = True
                tmp_num = 10
                tmp_side = ''
                while tmp:
                    for event in pygame.event.get():
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
                                tmp_side = 'left'
                            elif event.key == pygame.K_RIGHT:
                                tmp_side = 'right'
                            if self.exam(tmp_num, tmp_side, data['pos']):
                                text_name = font.render('Ты че даун?) Попробуй еще раз',
                                                        True, THECOLORS['lightskyblue3'])
                                place_text_name = text_name.get_rect(center=(750, 200))
                                dis.blit(text_name, place_text_name)
                                pygame.display.update()
                                print('Проверка прошла успешно, можно отправлять серверу')
                                # Если возвращается 1, то это дубль, если 2, то обычная фишка
                                tmp = False
                                doubles_, key = self.examination_number_shtics(tmp_num, data['shticks'][tmp_num],
                                                                               tmp_side, data['pos'])
                                message = {'side': tmp_side,
                                           'key': key,
                                           'count_of_position': tmp_num}
                                print(message)
                                message = str(message)
                                print('Что пытаемся отправить?', message, type(message))
                                sock.send(message.encode())
                                break
                            elif not self.exam(tmp_num, tmp_side, data['pos']) \
                                    and (tmp_side != '' and tmp != 10):
                                # Отписываем что за игрок в целом
                                text_name = font.render('Ты че даун?) Попробуй еще раз',
                                                        True, THECOLORS['black'])
                                place_text_name = text_name.get_rect(center=(750, 200))
                                dis.blit(text_name, place_text_name)
                                pygame.display.update()

if __name__ == "__main__":
    client = client_Vova()
    client.start_client()