"""Server for Dominoes"""

import socket
import time
from Game import Game, Gamer


class Server:

    def __init__(self):
        self.main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Клиент нам будет отправлять не один большой пакет за долгое время, а несколько маленьких пакетов
        self.main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.players = list([])
        self.server_works = True
        self.end_game = True
        self.end_round = True
        self.board = list([])
        self.game = Game()

    def send_shticks_player(self, distribution):
        self.players[0].shticks = sorted(distribution[: 7])
        self.players[1].shticks = sorted(distribution[7: 14])
        self.players[2].shticks = sorted(distribution[14: 21])
        self.players[3].shticks = sorted(distribution[21: 28])

    def get_params(self, count, pos, count_round, board, ):
        lst = []
        for i in range(len(self.players)):
            if count == i:
                dct = {'pos': pos,
                       'name': self.players[count].name,
                       'count_of_round': count_round,
                       'board': board,
                       'shticks': self.players[count].shticks}
                lst.append(dct)
            else:
                dct = {'pos': list([[], None, None]),
                       'name': self.players[count].name,
                       'count_of_round': count_round,
                       'board': board,
                       'shticks': self.players[i].shticks}
                lst.append(dct)
        return lst

    def master(self):
        # Привязываем наш сокет через порт компьютера
        self.main_socket.bind(('localhost', 10000))
        # Настраиваем сокет, чтобы сервер работал непрерывно и программа не останавливалась и ждала сообщения
        self.main_socket.setblocking(0)
        # Режим прослушивания может, одновременно подключиться 4 человека
        self.main_socket.listen(4)
        print('Server is work')
        while self.server_works:
            # Проверим есть ли желающие войти в игру, и переводим подключившегося на новый сокет (порт)
            try:
                new_socket, addr = self.main_socket.accept()
                print(f"Подключился {addr}")
                # Настраиваем новый сокет
                new_socket.setblocking(0)
                # Создаем нового игрока и добавляем в массив игроков
                new_player = Gamer(new_socket, addr)
                self.players.append(new_player)
            except:
                print('Нет желающих')
                pass
            time.sleep(1)
            print(len(self.players))
            # Считываем команды игроков
            for player in self.players:
                try:
                    data = player.conn.recv(1024)
                    data = data.decode()
                    print(f"получил {data}, {type(data)}")
                    if data.startswith('name_'):
                        player.name = data[5:]
                except:
                    continue
            if len(self.players) == 4:
                print('внутри')
                while self.game.end_game:
                    list_shticks = self.game.chip_distribution()
                    self.send_shticks_player(list_shticks)
                    print('Раздача окончена')
                    order = self.game.order(self.players)
                    print(order)
                    print(f"Имя первого чела {self.players[order[0] - 1].name} "
                          f"и его фишки {self.players[order[0] - 1].shticks}")
                    # Раунд начался.
                    # Пишем номер раунда.
                    self.game.end_round = True
                    number_of_passes = 0
                    self.game.board = list([])
                    print(f"Начало {self.game.count_round}-го раунда")

                    while self.game.end_round:
                        for number in order:
                            print('Количество пропусков', number_of_passes)
                            print(f"ходит игрок {self.players[number - 1].name, self.players[number - 1].shticks}")
                            pos_var = self.game.put_a_chip(number - 1, self.players)
                            print(f"Возможные варианты")
                            params = self.get_params(number - 1, pos_var, self.game.count_round, self.game.board)
                            print(params)
                            if pos_var != list([[], None, None]):
                                # Отправляем человеку возможные варианты как можно сходить и доску для отрисовки
                                try:
                                    for i in range(4):
                                        if i == number - 1:
                                            param = str({'pos': pos_var,
                                                         'name': self.players[number - 1].name,
                                                         'count_of_round': self.game.count_round,
                                                         'board': self.game.board,
                                                         'shticks': self.players[number - 1].shticks})
                                            self.players[i].conn.send(param.encode())
                                        else:
                                            param = str({'pos': list([[], None, None]),
                                                         'name': self.players[number - 1].name,
                                                         'count_of_round': self.game.count_round,
                                                         'board': self.game.board,
                                                         'shticks': self.players[i].shticks})
                                            self.players[i].conn.send(param.encode())
                                except:
                                    print(f"Не получилось отправить")

                                answer = True
                                while answer:
                                # Принимаю от клиента фишку и куда ее ставить
                                    try:
                                        data = self.players[number - 1].conn.recv(1024)
                                        data = data.decode()
                                        print('Получили от игрока:', data)
                                        number_of_passes = 0
                                        data = eval(data)
                                        print(f"Что пришло от игрока {self.players[number - 1].name}, {data}")
                                        print(f"Какие фишки у игрока {self.players[number - 1].shticks}")
                                        if data['side'] == 'left':
                                            self.game.board.insert(0, data['key'])
                                            self.players[number - 1].shticks.remove(
                                                self.players[number - 1].shticks[data['count_of_position']])
                                        elif data['side'] == 'right':
                                            self.game.board.append(data['key'])
                                            self.players[number - 1].shticks.remove(
                                                self.players[number - 1].shticks[data['count_of_position']])
                                        answer = False
                                # Вот тут возможно надо считать рыбу
                                    except:
                                        continue
                            else:
                                number_of_passes += 1
                                print('У игрока нет вариантов')
                            print('Мы по идее переходим к следующему игроку')
                            if number_of_passes >= 4:
                                print('у нас тут типа рыба, но скорей конец раунда')
                                time.sleep(5)
                            if self.game.dont_end_round(number_of_passes,
                                                        number - 1, self.players)\
                                    and len(self.game.board) >= 12:
                                    self.game.end_round = False
                                    print('Раунд должен быть закончен')
                                    break
                    if self.game.dont_end_game() == 'one':
                        print('Победила первая команда')
                    elif self.game.dont_end_game() == 'two':
                        print('Победила вторая команда')
                    break


if __name__ == "__main__":
    server = Server()
    server.master()
