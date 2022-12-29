import socket
import pygame
from pygame.color import THECOLORS

# class Client ():


if __name__ == "__main__":
    WIDTH_WINDOW, HEIGHT_WINDOW = 1500, 750
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Отключаем алгоритм Нейгла
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    sock.connect(('localhost', 10000))
    # Отрисовываем
    pygame.init()
    dis = pygame.display.set_mode((1500, 750))
    dis.fill(THECOLORS['lightskyblue3'])
    pygame.display.update()
    pygame.display.set_caption('Dominoes by SanyaCentner')
    clock = pygame.time.Clock()
    time_on_move = 1
    time_to_clear_text = 1.5
    running = True
    message = ''
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Считаем какие кнопки игрок нажал
        #     if event.type == pygame.KEYDOWN:
        #         # Чел выбирает фишку и проводим проверку можно ли ее ставить
        #         if event.key == pygame.K_LEFT:
        #             message += 'l,'
        #         elif event.key == pygame.K_RIGHT:
        #             message += 'r,'
        #         elif event.key == pygame.K_1:
        #             message += '0'
        #         elif event.key == pygame.K_2:
        #             message += '1'
        #         elif event.key == pygame.K_3:
        #             message += '2'
        #         elif event.key == pygame.K_4:
        #             message += '3'
        #         elif event.key == pygame.K_5:
        #             message += '4'
        #         elif event.key == pygame.K_6:
        #             message += '5'
        #         elif event.key == pygame.K_7:
        #             message += '6'

        #считываем команды игрока

        # Отправляем полученную команду на сервер
        sock.send('message'.encode())

        # Получаем от сервера новое состояние игрового поля, клиент полностью зависит от сервера
        data = sock.recv(1024)
        data = data.decode()

        # Рисуем новое состояние игрового поля
        print(data)