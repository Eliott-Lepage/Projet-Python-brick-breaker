from os import listdir
from os.path import isfile, join
import json

from libs.brique.fonction import set_next_level


class Brick:
    """Class representing the bricks
           Author : Mathis Dory, Eliott Lepage
           Date : November 2020
           This class is used to create the bricks of the Graphical User Interface
    """
    def __init__(self, game):
        """
        Creation of all the features of a single brick (width, height, x and y components)
                PRE :
                    game class is running
                POST :
                    Call the functions self.get_files() and self.open_level_up()
        """
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

        # Component creation
        self.get_files()
        self.open_level_up()

    def get_files(self):
        """
        This function performs two different things
            - Creates a list of all the files in the directory data (only txt format/extension)
            - Writes the actual level in the file save.txt

            PRE: -
            POST:
                Writes/dumps a new '[key] : [value]' in save.txt like -> "Actual Level": "level_01.txt"
                - Key = The actual level
                - Value = txt file

            RAISES:
                FileNotFoundError not save.txt in data
        """
        list_files = list()
        files = [f for f in listdir("data") if isfile(join("data", f))]
        for i in files:
            if i[:6] == "level_":
                list_files.append(i)
        try:
            with open("data/save.txt", "r") as file:
                res = json.load(file)
                for elem in list_files:
                    if elem == "level_" + str(self.counter) + ".txt":
                        res["Actual Level"] = str(elem)
        except FileNotFoundError:
            return 'File not found !'
        except IOError:
            return 'Error IO.'

        try:
            with open("data/save.txt", "w") as file_write:
                json.dump(res, file_write, indent=3, sort_keys=True)
        except FileNotFoundError:
            return 'File not found !'
        except IOError:
            return 'Error IO.'

    def open_level_up(self):
        """
        Creates the physical part of the bricks in the Graphical User Interface in terms of the txt file (level_**.txt)
         - This includes the width, height and color

        PRE:
            -
        POST:
            - The file save.txt exists in data folder
            - Actual level is a key of dictionary
            - Bricks are created in the Graphical User Interface

        RAISES :
            FileNotFoundError not save.txt in data

        """
        try:
            with open("data/save.txt", "r") as file:
                dictionary = json.load(file)
        except FileNotFoundError:
            return 'File not found !'
        except IOError:
            return 'Error IO.'

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

            return 'File not found !'

        except IOError:

            return 'Error IO.'

    def next_level(self):
        """
        This function sets the next level (+1) when the user has finished the actual level
        Configure the text of the label in the Graphic User Interface

        PRE: -
        POST:
            - Increment self.counter (+1) to access to the next level of the game
            - Configure the level label
            - Call the functions self.get_files() and self.open_level_up()

        """
        temp_data = set_next_level(self.counter)
        self.counter = temp_data[0]
        self.Game.canevas.itemconfigure(self.Game.actual_level, text="Level " + str(self.counter))
        self.x = temp_data[1]
        self.y = temp_data[2]
        self.get_files()
        self.open_level_up()

