import pygame

class Board():

    def __init__(self):
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