from tkinter import *


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

        #self.create_all_bricks()
        #self.open_level()
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

                # Affichage principal
                for line in file:
                    stripped_line = line.strip()
                    line_list = stripped_line.split()
                    list_of_lists.append(line_list)

                end = False
                while end is not True:

                    # Place la balle à l'index indiqué par l'utilisateur
                    reponse = input("Quelle position attribuez vous à la balle ?  ")
                    # Vérifie si l'utilisateur introduit un nombre entre 1 et 13
                    if 13 >= int(reponse) > 0:
                        end = False
                        touch = False
                        list_ball[int(reponse) - 1] = "*"
                        index_ball = list_ball.index("*")
                        while end == False:
                            if str(list_of_lists[3][index_ball]) == "x":
                                list_of_lists[3][index_ball] = "-"
                                touch = True

                            if str(list_of_lists[2][index_ball]) == "x":
                                if touch == False:
                                    list_of_lists[2][index_ball] = "-"
                                    touch = True

                            if str(list_of_lists[1][index_ball]) == "x":
                                if touch == False:
                                    list_of_lists[1][index_ball] = "-"
                                    touch = True

                            if str(list_of_lists[0][index_ball]) == "x":
                                if touch == False:
                                    list_of_lists[0][index_ball] = "-"
                                    touch = True
                            end = True

                        print(' '.join(map(str, list_of_lists[0])))
                        print(' '.join(map(str, list_of_lists[1])))
                        print(' '.join(map(str, list_of_lists[2])))
                        print(' '.join(map(str, list_of_lists[3])))

                        print(' '.join(map(str, list_ball)))
                        list_ball[int(reponse) - 1] = ' '
                        print("\n")

                        for elem in list_of_lists:
                            if 'x' in elem:
                                end = False
                            else:
                                end = True
                        if end:
                            print("ENNDDDDD")

                    else:
                        print("Veuillez introduire un nombre entre 1 et 13 compris !")
                        break
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

    def open_level_up(self):
        try:
            with open('data/level_03.txt', "r") as file:
                res = {}
                ligne_number = 0

                for line in file:
                    dt = line.rstrip()
                    dt_splitted = dt.split(" ")  # ['-', '-', '-', '1', '2', '3', '3', '3', '2', '1', '-', '-', '-']

                    nom_ligne = str('line_' + str(ligne_number))

                    if not nom_ligne in res:
                        res[nom_ligne] = dt_splitted
                    ligne_number += 1
                res_keys = list(res.keys())  # ['line_0', 'line_1', 'line_2', 'line_3']
                for cle in res_keys:
                    for y in range(len(res[cle])):
                        if res[cle][y] == '1':
                            self.bricks.append(
                                self.Game.canevas.create_rectangle(self.x, self.y, self.x + 45, self.y + 25,
                                                                  fill='blue', tag='blue'))
                            self.x += 50
                        elif res[cle][y] == '2':
                            self.bricks.append(
                                self.Game.canevas.create_rectangle(self.x, self.y, self.x + 45, self.y + 25,
                                                                  fill='green', tag='green'))
                            self.x += 50
                        elif res[cle][y] == '3':
                            self.bricks.append(
                                self.Game.canevas.create_rectangle(self.x, self.y, self.x + 45, self.y + 25,
                                                                  fill='yellow', tag='yellow'))
                            self.x += 50
                        elif res[cle][y] == '4':
                            self.bricks.append(
                                self.Game.canevas.create_rectangle(self.x, self.y, self.x + 45, self.y + 25,
                                                                  fill='red', tag='red'))
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

                    if not name_line in res:
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
