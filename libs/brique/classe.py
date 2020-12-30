from os import listdir
from os.path import isfile, join
import json


class Brick:

    def __init__(self, Game):
        self.x = 50
        self.y = 50
        self.number_max = 56
        self.width = None
        self.height = None
        self.colors = None
        self.bricks = []
        self.Game = Game
        self.levels = []
        self.counter = 1

        # self.create_all_bricks()
        # self.open_level()
        self.get_files()
        self.open_level_up()

    def create_all_bricks(self):
        for x in range(self.number_max):
            self.brick = self.Game.canevas.create_rectangle(self.x, self.y, self.x + 45, self.y + 25, fill='yellow')
            self.x += 50

            if x == 12 + 1:
                self.x = 50
                self.y = 100

            if x == 25 + 2:
                self.x = 50
                self.y = 150

            if x == 38 + 3:
                self.x = 50
                self.y = 200

    def display_console(self):
        try:
            with open('data/level.txt', "r") as file:
                list_ball = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                list_of_lists = []

                # Main display
                for line in file:
                    stripped_line = line.strip()
                    line_list = stripped_line.split()
                    list_of_lists.append(line_list)

                end = False
                while end is not True:

                    # Place the ball at the index indicated by the user
                    response = input("Quelle position attribuez vous à la balle ?  ")
                    # Checks if the user enters a number between 1 and 13
                    if 13 >= int(response) > 0:
                        end = False
                        touch = False
                        list_ball[int(response) - 1] = "*"
                        index_ball = list_ball.index("*")
                        while not end:
                            if str(list_of_lists[3][index_ball]) == "x":
                                list_of_lists[3][index_ball] = "-"
                                touch = True

                            if str(list_of_lists[2][index_ball]) == "x":
                                if not touch:
                                    list_of_lists[2][index_ball] = "-"
                                    touch = True

                            if str(list_of_lists[1][index_ball]) == "x":
                                if not touch:
                                    list_of_lists[1][index_ball] = "-"
                                    touch = True

                            if str(list_of_lists[0][index_ball]) == "x":
                                if not touch:
                                    list_of_lists[0][index_ball] = "-"
                                    touch = True
                            end = True

                        print(' '.join(map(str, list_of_lists[0])))
                        print(' '.join(map(str, list_of_lists[1])))
                        print(' '.join(map(str, list_of_lists[2])))
                        print(' '.join(map(str, list_of_lists[3])))

                        print(' '.join(map(str, list_ball)))
                        list_ball[int(response) - 1] = ' '
                        print("\n")

                        for elem in list_of_lists:
                            if 'x' in elem:
                                end = False
                            else:
                                end = True
                        if end:
                            print("END")
                    else:
                        print("Please enter a number between 1 and 13 inclusive!")
                        break
        except FileNotFoundError:
            print('File not found !')
        except IOError:
            print('Error IO.')

    def get_files(self):
        list_files = list()
        files = [f for f in listdir("data") if isfile(join("data", f))]
        for i in files:
            if i[:6] == "level_":
                list_files.append(i)

        with open("data/save.txt", "r") as file:
            res = json.load(file)
            for elem in list_files:
                if elem == "level_" + str(self.counter) + ".txt":
                    res["Actual Level"] = str(elem)

            with open("data/save.txt", "w") as file_write:
                json.dump(res, file_write, indent=3, sort_keys=True)

    def open_level_up(self):
        with open("data/save.txt", "r") as file:
            dictionary = json.load(file)
        try:
            with open('data/' + str(dictionary["Actual Level"]), "r") as file:
                res = {}
                line_number = 0

                for line in file:
                    dt = line.rstrip()
                    dt_splitted = dt.split(
                        " ")  # ['-', '-', '-', '1', '2', '3', '3', '3', '2', '1', '-', '-', '-']

                    name_line = str('line_' + str(line_number))

                    if name_line not in res:
                        res[name_line] = dt_splitted
                    line_number += 1
                res_keys = list(res.keys())  # ['line_0', 'line_1', 'line_2', 'line_3']
                for cle in res_keys:
                    for y in range(len(res[cle])):
                        if res[cle][y] == '1':
                            self.bricks.append(
                                self.Game.canevas.create_rectangle(self.x, self.y, self.x + 45, self.y + 25,
                                                                   fill='white', tag='white'))
                            self.x += 50
                        elif res[cle][y] == '2':
                            self.bricks.append(
                                self.Game.canevas.create_rectangle(self.x, self.y, self.x + 45, self.y + 25,
                                                                   fill='yellow', tag='yellow'))
                            self.x += 50
                        elif res[cle][y] == '3':
                            self.bricks.append(
                                self.Game.canevas.create_rectangle(self.x, self.y, self.x + 45, self.y + 25,
                                                                   fill='orange', tag='orange'))
                            self.x += 50
                        elif res[cle][y] == '4':
                            self.bricks.append(
                                self.Game.canevas.create_rectangle(self.x, self.y, self.x + 45, self.y + 25,
                                                                   fill='red', tag='red'))
                            self.x += 50
                        elif res[cle][y] == '5':
                            self.bricks.append(
                                self.Game.canevas.create_rectangle(self.x, self.y, self.x + 45, self.y + 25,
                                                                   fill='#8757D5', tag='#8757D5'))
                            self.x += 50
                        elif res[cle][y] == '6':
                            self.bricks.append(
                                self.Game.canevas.create_rectangle(self.x, self.y, self.x + 45, self.y + 25,
                                                                   fill='blue', tag='blue'))
                            self.x += 50
                        elif res[cle][y] == '7':
                            self.bricks.append(
                                self.Game.canevas.create_rectangle(self.x, self.y, self.x + 45, self.y + 25,
                                                                   fill='green', tag='green'))
                            self.x += 50
                        elif res[cle][y] == '8':
                            self.bricks.append(
                                self.Game.canevas.create_rectangle(self.x, self.y, self.x + 45, self.y + 25,
                                                                   fill='grey', tag='grey'))
                            self.x += 50
                        elif res[cle][y] == 'v':
                            self.bricks.append(
                                self.Game.canevas.create_rectangle(self.x, self.y, self.x + 45, self.y + 25,
                                                                   fill='pink', tag='pink'))
                            self.x += 50
                        else:
                            self.x += 50
                            continue

                    self.y += 50
                    self.x = 50

        except FileNotFoundError:
            print('Fichier introuvable.')

    def open_level(self):
        try:
            with open('data/level.txt', "r") as file:
                res = {}
                line_number = 0

                for line in file:
                    dt = line.rstrip()
                    dt_splitted = dt.split(" ")  # ['-', '-', '-', '1', '2', '3', '3', '3', '2', '1', '-', '-', '-']

                    name_line = str('line_' + str(line_number))

                    if name_line not in res:
                        res[name_line] = dt_splitted
                    line_number += 1

                res_keys = list(res.keys())  # ['line_0', 'line_1', 'line_2', 'line_3']
                for cle in res_keys:
                    for y in range(len(res[cle])):
                        if res[cle][y] == 'x':
                            self.bricks.append(
                                self.Game.canevas.create_rectangle(self.x, self.y, self.x + 45, self.y + 25,
                                                                   fill='yellow'))
                            self.x += 50
                        else:
                            self.x += 50
                            continue
                    self.y += 50
                    self.x = 50

        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

    def next_level(self):
        self.counter += 1
        self.x = 50
        self.y = 50
        self.get_files()
        self.open_level_up()
