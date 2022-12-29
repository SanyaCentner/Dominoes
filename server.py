"""Server for Dominoes"""

import socket
import time

class Server:

    def __init__(self):
        self.main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Клиент нам будет отправлять не один большой пакет за долгое время, а несколько маленьких паетов
        self.main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.players_sockets = list([])

    def master(self):
        # Привязываем наш сокет через порт компьютера
        self.main_socket.bind(('localhost', 10000))
        # Настраиваем сокет, чтобы сервер работал непрерывно и программа не останавливалась и ждала сообщения
        self.main_socket.setblocking(0)
        # Режим прослушки может, одновременно подключиться 4 человека
        self.main_socket.listen(4)
        print('Server is work')
        while True:
            # Проверим есть ли желающие войти в игру, и переводим подключившегося на новый сокет (порт)
            try:
                new_socket, addr = self.main_socket.accept()
                print(f"Подключился {addr}")
                # Настраиваем новый сокет
                new_socket.setblocking(0)
                self.players_sockets.append(new_socket)
            except:
                print('Нет желающих')
                pass
            time.sleep(1)
            # Считываем команды игроков
            for sock in self.players_sockets:
                try:
                    data = sock.recv(1024)
                    print('получил', data.decode())
                except:
                    continue
            # Отправляем новое состояние игрового поля
            for sock in self.players_sockets:
                try:
                    sock.send('Новое состояние игры'.encode())
                except:
                    print(f"Отключился игрок {sock}")
                    self.players_sockets.remove(sock)
                    sock.close()

if __name__ == "__main__":
    server = Server()
    server.master()
