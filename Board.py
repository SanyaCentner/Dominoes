import pygame


if __name__ == '__main__':
    pygame.init()
    dis = pygame.display.set_mode((400, 300))
    pygame.display.update()
    pygame.display.set_caption('Snake game by Pythonist')
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            print(event)  # выводит на экран все действия игры

    pygame.quit()
    quit()