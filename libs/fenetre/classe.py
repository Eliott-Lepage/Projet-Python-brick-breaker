from tkinter import *
from libs.balle.classe import Ball
from libs.paddle.classe import Paddle
from libs.brique.classe import Brick
import json


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
        self.canevas = Canvas(self.root, bg='light blue', highlightthickness=0)
        self.paddle = Paddle(self)
        self.ball = Ball(self)
        self.brick = Brick(self)
        self.window = Window
        self.end = False
        self.canevas.pack(fill=BOTH, expand=YES)
        self.ball.score_label.grid(row=0, column=0, sticky='w')
        self.ball.best_score_label.grid(row=2, column=0, sticky='e')
        self.ball.user_name.grid(row=0, column=2, sticky='w')
        self.ball.lives_label.grid(row=2, column=2, sticky='e')

    def leave_loose_game(self):
        self.end = True
        self.root.destroy()
        GameOver()

    def leave_win_game(self):
        self.end = True
        self.root.destroy()
        Victory()


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
