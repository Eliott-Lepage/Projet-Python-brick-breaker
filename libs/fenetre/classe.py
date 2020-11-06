from tkinter import *


class Window:

    def __init__(self):
        self.window = Tk()
        self.window.title("Brick Breaker")
        self.window.geometry("1920x1080")
        self.window.minsize(800, 600)
        self.window.iconbitmap("data/wall.ico")
        self.window.config(background="#000000")

        # initialization des composants
        self.frame = Frame(self.window, bg='#000000')
        self.petiteFrame = Frame(self.frame, bg='#000000')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.petiteFrame.pack(expand=YES, pady=100)
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create_play_button()
        self.create_quit_button()

    def create_title(self):
        label_title = Label(self.frame, text="Brick Breaker", font=("Arial", 40), bg='#000000',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="Projet Python 2020", font=("Arial", 25), bg='#000000',
                               fg='white')
        label_subtitle.pack()

    def create_play_button(self):
        play_button = Button(self.petiteFrame, text="Jouer", font=("Arial", 25), bg='white', relief='groove',
                             fg='#000000',
                             command=self.lancer_jeu, width=8, activebackground='green',
                             activeforeground='black')
        play_button.grid(column=0, row=0)
        invisible_widget = Label(self.petiteFrame, text=" ", bg="black")
        invisible_widget.grid(column=1, row=0)

    def create_quit_button(self):
        quit_button = Button(self.petiteFrame, text="Quitter", font=("Arial", 25), bg='white', relief='groove',
                             fg='#000000',
                             command=self.quitter_page, width=8, activebackground='red',
                             activeforeground='black')
        quit_button.grid(column=2, row=0)

    def quitter_page(self):
        self.window.destroy()

    def lancer_jeu(self):
        self.window.destroy()
        Jeu()


class Jeu:
    def __init__(self):
        self.window = Tk()
        self.window.title("Brick Breaker")
        self.window.geometry("1920x1080")
        self.window.minsize(800, 600)
        self.window.iconbitmap("data/wall.ico")
        self.window.config(background="#000000")
