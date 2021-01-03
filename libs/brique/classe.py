from os import listdir
from os.path import isfile, join
import json


class Brick:

    def __init__(self, game):
        self.x = 50
        self.y = 50
        self.number_max = 56
        self.width = None
        self.height = None
        self.colors = None
        self.bricks = []
        self.Game = game
        self.levels = []
        self.counter = 1

        # self.create_all_bricks()
        self.get_files()
        self.open_level_up()

    def create_all_bricks(self):
        for x in range(self.number_max):
            self.Game.canevas.create_rectangle(self.x, self.y, self.x + 45, self.y + 25, fill='yellow')
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
        self.Game.canevas.itemconfigure(self.Game.actual_level, text="Level " + str(self.counter))
        self.x = 50
        self.y = 50
        self.get_files()
        self.open_level_up()
