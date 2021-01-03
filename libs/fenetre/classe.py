from tkinter import *
from libs.balle.classe import Ball
from libs.paddle.classe import Paddle
from libs.brique.classe import Brick
import json
import time


class Window:
    """Class representing a menu for the Game

       Author : Mathis Dory, Eliott Lepage
       Date : November 2020
       This class is used to create a GUI and start the Game
    """

    def __init__(self):
        """This builds a GUI menu

                        PRE :
                            -
                        POST :
                            call
                                self.create_title()
                                self.create_subtitle()
                                self.create_play_button()
                                self.create_quit_button()
        """
        self.window = Tk()
        self.window.title("Brick Breaker")
        self.window.attributes("-fullscreen", True)
        self.window.iconbitmap("data/wall.ico")
        self.window.config(background="light blue")

        # initialization des composants
        self.frame = Frame(self.window, bg='light blue')
        self.littleFrame = Frame(self.frame, bg='light blue')
        self.littleFrame_bis = LabelFrame(self.frame, bg='light blue', text="USER NAME")

        # creation des composants
        self.create_title()
        self.create_subtitle()
        self.create_play_button()
        self.create_quit_button()

        # empaquetage
        self.littleFrame_bis.pack(expand=YES, pady=30)
        self.littleFrame.pack(expand=YES, pady=50)
        self.frame.pack(expand=YES, fill=BOTH, pady=200)

    def create_title(self):
        """This builds a title label

                        PRE :
                            -
                        POST :
                            pack the title label
        """
        label_title = Label(self.frame, text="Brick Breaker", font=("Arial", 40), bg='light blue',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        """This builds a subtitle label

                                PRE :
                                    -
                                POST :
                                    pack the subtitle label
                """
        label_subtitle = Label(self.frame, text="Projet Python 2020", font=("Arial", 25), bg='light blue',
                               fg='white')
        label_subtitle.pack()

    def create_play_button(self):
        """This builds button to launch the Game or leave it
                                PRE :
                                    -
                                POST :
                                    call function my_click if user click on "Jouer" button
                                RAISES :
                                    -
                """

        def my_click():
            """This builds button to launch the Game or leave it
                            PRE : -

                            POST :
                                save.txt exists in data folder
                                Actual Username is a key in save.txt
                                name.isalnum() == True
                            RAISES :
                                ValueError if not name.isalnum()
                                FileNotFoundError not save.txt in data
                                IOError if not save.txt in data
            """
            name = user_name.get(1.0, END).strip()
            self.res = {}
            try:
                with open("data/save.txt", "r") as file:
                    self.res = json.load(file)
                    self.res["Actual Username"] = str(name)
                    if not name.isalnum():
                        raise ValueError
                    if '' in self.res:
                        del self.res['']

                    if name not in self.res:
                        self.res[str(name)] = [0]
            except FileNotFoundError:
                print('File not found !')
            except IOError:
                print('Error IO.')
            try:
                with open("data/save.txt", "w") as file_write:
                    json.dump(self.res, file_write)

            except FileNotFoundError:
                print('File not found !')
            except IOError:
                print('Error IO.')

        user_name = Text(self.littleFrame_bis, width=30, height=1, font=("Helvetica", 16))
        user_name.pack(pady=30, padx=30)

        play_button = Button(self.littleFrame, text="Jouer", font=("Arial", 25), bg='white', relief='groove',
                             fg='light blue',
                             command=lambda: [my_click(), self.play_game()], width=8, activebackground='green',
                             activeforeground='black')
        play_button.grid(column=0, row=0)
        invisible_widget = Label(self.littleFrame, text=" ", bg="light blue")
        invisible_widget.grid(column=1, row=0)

    def create_quit_button(self):
        """This create a button to quit the game

                        PRE :
                            -
                        POST :
                           create the leave button in a grid
        """
        quit_button = Button(self.littleFrame, text="Quitter", font=("Arial", 25), bg='white', relief='groove',
                             fg='light blue',
                             command=self.leave_page, width=8, activebackground='red',
                             activeforeground='black')
        quit_button.grid(column=2, row=0)

    def leave_page(self):
        """This destroy the menu window if player leaves the game

                        PRE :
                            -
                        POST :
                           destroy window
        """
        self.window.destroy()

    def play_game(self):
        """This destroy the menu window if player plays the game and create a new window with the loaded level

                        PRE :
                            -
                        POST :
                           destroy window
                           call Game() class
        """
        self.window.destroy()
        Game()


class Game:
    """Class representing the main window for the game.

       Author : Mathis Dory, Eliott Lepage
       Date : November 2020
       This class is used to create a GUI with all needed elements
    """

    def __init__(self):
        """This builds a level interface

                        PRE :
                            -
                        POST :
                            create canvas to insert all elements in
                            create ball, paddle and brick class
                            call create_score() method
        """
        self.root = Tk()
        self.root.title("Brick Breaker")
        self.root.geometry("800x600")
        self.root.maxsize(800, 600)
        self.root.minsize(800, 600)
        self.root.iconbitmap("data/wall.ico")
        self.root.config(background="#000000")
        self.score = 0
        self.life = 3
        self.canevas = Canvas(self.root, bg='light blue', highlightthickness=0)
        self.paddle = Paddle(self)
        self.ball = Ball(self)
        self.brick = Brick(self)
        self.create_score()
        self.window = Window
        self.end = False
        self.canevas.pack(fill=BOTH, expand=YES)

    def leave_loose_game(self):
        """This destroy the window if user has no more lives

                                PRE :
                                    -
                                POST :
                                    call update_json_file() method
                                    destroy root windows
                                    call GameOver() class
        """
        self.update_json_file()
        self.end = True
        self.root.destroy()
        GameOver()

    def leave_win_game(self):
        """This update objects of the canvas if the player destroyed all the bricks in its current level

                                PRE :
                                    -
                                POST :
                                    sleep the program for 2 seconds
                                    update canvas to create black screen
                                    call self.brick.next_level method
        """
        self.end = True
        self.canevas.config(bg='black')
        self.canevas.itemconfig(self.ball.ball, fill='black')
        self.canevas.itemconfig(self.paddle.paddle, fill='black')
        self.canevas.update()
        time.sleep(2)
        self.canevas.config(bg='light blue')
        self.canevas.itemconfig(self.ball.ball, fill='red')
        self.canevas.itemconfig(self.paddle.paddle, fill='grey')
        self.brick.next_level()

    def create_score(self):
        """This create text widgets with username, current level, lives, current score and best score

                                PRE :
                                    -
                                POST :
                                    save.txt exists in data folder
                                    Actual Username is a key in save.txt

                                RAISES :
                                    KeyError if not "Actual Username" in dictionary
                                    FileNotFoundError not save.txt in data
                                    IOError if not save.txt in data
        """
        try:
            with open("data/save.txt", "r") as file:

                dictionary = json.load(file)
                if not "Actual Username" in dictionary:
                    raise KeyError("The Actual Username key is missing !")
                else:
                    # Get the name of the actual user
                    user = dictionary["Actual Username"]
                    # Get the higher score of the user

                max_number = 0
                for elem in dictionary[user]:
                    if elem > max_number:
                        max_number = elem
                    else:
                        continue
        except FileNotFoundError:
            print('File not found !')
        except IOError:
            print('Error IO.')

        # Create the score in game
        self.score_label = self.canevas.create_text(0, 0, text="Score : " + str(self.score), font=("Arial", 15),
                                                    anchor=NW)

        # Create the actual level in game
        self.actual_level = self.canevas.create_text(400, 0, text="Level " + str(self.brick.counter),
                                                     font=("Arial", 15), anchor=N)

        # Create label best score
        self.best_score_label = self.canevas.create_text(800, 0, text="Best Score : " + str(max_number),
                                                         font=("Arial", 15), anchor=NE)

        # Create label user
        self.user_name = self.canevas.create_text(0, 600, text="Username : " + user, font=("Arial", 15), anchor=SW)

        # Create label lives
        self.lives_label = self.canevas.create_text(800, 600, text="Lives : " + str(self.life), font=("Arial", 15),
                                                    anchor=SE)

    def update_json_file(self):
        """This update the save.txt file with score when user has no more lives

                                PRE :
                                    -
                                POST :
                                    save.txt exists in data folder
                                    Actual Username is a key in save.txt

                                RAISES :
                                    KeyError if not "Actual Username" in dictionary
                                    FileNotFoundError not save.txt in data
                                    IOError if not save.txt in data
        """
        with open("data/save.txt", "r+") as file:
            dictionary = json.load(file)
            user = dictionary["Actual Username"]
            dictionary[user].append(self.score)

        with open("data/save.txt", "w") as file:
            json.dump(dictionary, file, indent=3, sort_keys=True)


class GameOver:
    """Class representing a menu if the user has no more lives

       Author : Mathis Dory, Eliott Lepage
       Date : November 2020
       This class is used to create a GUI with 2 buttons
    """

    def __init__(self):
        """This builds a GUI menu

                        PRE :
                            -
                        POST :
                            call
                                self.create_title()
                                self.create_play_button()
                                self.create_quit_button()
        """
        self.master = Tk()
        self.master.title("Brick Breaker")
        self.master.geometry("800x600")
        self.master.minsize(800, 600)
        self.master.iconbitmap("data/wall.ico")
        self.master.config(background="lightblue")
        self.frame = Frame(self.master, bg='lightblue')
        self.littleFrame = Frame(self.frame, bg='lightblue')

        # creation des composants
        self.create_title()
        self.create_play_button()
        self.create_quit_button()

        # empaquetage
        self.littleFrame.pack(expand=YES, pady=100)
        self.frame.pack(expand=YES)

    def create_title(self):
        """This builds a title label

                        PRE :
                            -
                        POST :
                            pack the title label
        """
        label_title = Label(self.frame, text="Game Over", font=("Arial", 40), bg='lightblue',
                            fg='white')
        label_title.pack()

    def create_play_button(self):
        """This create a button to restart the game

                        PRE :
                            -
                        POST :
                           create the restart button in a grid
        """
        play_button = Button(self.littleFrame, text="Rejouer", font=("Arial", 25), bg='white', relief='groove',
                             fg='lightblue',
                             command=self.start_game, width=8, activebackground='white',
                             activeforeground='lightblue')
        play_button.grid(column=0, row=0)
        invisible_widget = Label(self.littleFrame, text=" ", bg="lightblue")
        invisible_widget.grid(column=1, row=0)

    def create_quit_button(self):
        """This create a button to quit the game

                        PRE :
                            -
                        POST :
                           create the leave button in a grid
        """
        quit_button = Button(self.littleFrame, text="Quitter", font=("Arial", 25), bg='white', relief='groove',
                             fg='lightblue',
                             command=self.leave_page, width=8, activebackground='white',
                             activeforeground='lightblue')
        quit_button.grid(column=2, row=0)

    def leave_page(self):
        """destroy the master window

                        PRE :
                            -
                        POST :
                           destroy the master window
        """
        self.master.destroy()

    def start_game(self):
        """destroy the master window and restart the game

                        PRE :
                            -
                        POST :
                           destroy the master window
                           call Game() class
        """
        self.master.destroy()
        Game()
