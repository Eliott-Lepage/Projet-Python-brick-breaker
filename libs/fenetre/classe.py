from tkinter import *
from libs.balle.classe import Ball
from libs.paddle.classe import Paddle
from libs.brique.classe import Brick
import json
import time


class Window:
    def __init__(self):
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
        self.create_widgets()

        # empaquetage
        self.littleFrame_bis.pack(expand=YES, pady=30)
        self.littleFrame.pack(expand=YES, pady=50)
        self.frame.pack(expand=YES, fill=BOTH, pady=200)

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create_play_button()
        self.create_quit_button()

    def create_title(self):
        label_title = Label(self.frame, text="Brick Breaker", font=("Arial", 40), bg='light blue',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="Projet Python 2020", font=("Arial", 25), bg='light blue',
                               fg='white')
        label_subtitle.pack()

    def create_play_button(self):
        def my_click():
            name = user_name.get(1.0, END).strip()
            self.res = {}

            with open("data/save.txt", "r") as file:
                self.res = json.load(file)
                self.res["Actual Username"] = str(name)
                if not name.isalnum():  # Verifie si le nom de l'utilisateur n est pas vide ou si il contient des espaces
                    raise ValueError
                if '' in self.res:
                    del self.res['']

                if name not in self.res:
                    self.res[str(name)] = [0]

                with open("data/save.txt", "w") as file_write:
                    json.dump(self.res, file_write)

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
        quit_button = Button(self.littleFrame, text="Quitter", font=("Arial", 25), bg='white', relief='groove',
                             fg='light blue',
                             command=self.leave_page, width=8, activebackground='red',
                             activeforeground='black')
        quit_button.grid(column=2, row=0)

    def leave_page(self):
        self.window.destroy()

    def play_game(self):
        self.window.destroy()
        Game()


class Game:
    def __init__(self):
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
        self.update_json_file()
        self.end = True
        self.root.destroy()
        GameOver()

    def leave_win_game(self):
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
        with open("data/save.txt", "r") as file:
            dictionary = json.load(file)
            # Get the name of the actual user
            user = dictionary["Actual Username"]
            # Get the higher score of the user

            max_number = 0
            for elem in dictionary[user]:
                if elem > max_number:
                    max_number = elem
                else:
                    continue

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
        with open("data/save.txt", "r+") as file:
            dictionary = json.load(file)
            user = dictionary["Actual Username"]
            dictionary[user].append(self.score)

        with open("data/save.txt", "w") as file:
            json.dump(dictionary, file, indent=3, sort_keys=True)


class GameOver:
    def __init__(self):
        self.master = Tk()
        self.master.title("Brick Breaker")
        self.master.geometry("800x600")
        self.master.minsize(800, 600)
        self.master.iconbitmap("data/wall.ico")
        self.master.config(background="lightblue")
        self.frame = Frame(self.master, bg='lightblue')
        self.littleFrame = Frame(self.frame, bg='lightblue')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.littleFrame.pack(expand=YES, pady=100)
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()
        self.create_play_button()
        self.create_quit_button()

    def create_title(self):
        label_title = Label(self.frame, text="Game Over", font=("Arial", 40), bg='lightblue',
                            fg='white')
        label_title.pack()

    def create_play_button(self):
        play_button = Button(self.littleFrame, text="Rejouer", font=("Arial", 25), bg='white', relief='groove',
                             fg='lightblue',
                             command=self.start_game, width=8, activebackground='white',
                             activeforeground='lightblue')
        play_button.grid(column=0, row=0)
        invisible_widget = Label(self.littleFrame, text=" ", bg="lightblue")
        invisible_widget.grid(column=1, row=0)

    def create_quit_button(self):
        quit_button = Button(self.littleFrame, text="Quitter", font=("Arial", 25), bg='white', relief='groove',
                             fg='lightblue',
                             command=self.leave_page, width=8, activebackground='white',
                             activeforeground='lightblue')
        quit_button.grid(column=2, row=0)

    def leave_page(self):
        self.master.destroy()

    def start_game(self):
        self.master.destroy()
        Game()


class Victory:
    def __init__(self):
        self.master = Tk()
        self.master.title("Brick Breaker")
        self.master.geometry("800x600")
        self.master.minsize(800, 600)
        self.master.iconbitmap("data/wall.ico")
        self.master.config(background="lightblue")
        self.frame = Frame(self.master, bg='lightblue')
        self.littleFrame = Frame(self.frame, bg='lightblue')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.littleFrame.pack(expand=YES, pady=100)
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()
        self.create_play_button()
        self.create_quit_button()

    def create_title(self):
        label_title = Label(self.frame, text="Victoire !", font=("Arial", 40), bg='lightblue',
                            fg='white')
        label_title.pack()

    def create_play_button(self):
        play_button = Button(self.littleFrame, text="Rejouer", font=("Arial", 25), bg='white', relief='groove',
                             fg='lightblue',
                             command=self.start_game, width=8, activebackground='white',
                             activeforeground='lightblue')
        play_button.grid(column=0, row=0)
        invisible_widget = Label(self.littleFrame, text=" ", bg="lightblue")
        invisible_widget.grid(column=1, row=0)

    def create_quit_button(self):
        quit_button = Button(self.littleFrame, text="Quitter", font=("Arial", 25), bg='white', relief='groove',
                             fg='lightblue',
                             command=self.leave_game, width=8, activebackground='white',
                             activeforeground='lightblue')
        quit_button.grid(column=2, row=0)

    def leave_game(self):
        self.master.destroy()

    def start_game(self):
        self.master.destroy()
        Game()
