from tkinter import *


class Ball():
    def __init__(self, Game):
        self.dx = 2
        self.dy = -6
        self.Game = Game
        self.static = True
        self.Game.root.bind("<Button-1>", self.lancer_balle)

        self.create_label()
        self.create_ball()

        # empaquetage
        self.label.pack(expand=YES)

    def create_label(self):
        self.label = Label(self.Game.canevas, text="Clique gauche pour lancer la balle", font=("Arial", 25),
                           bg='lightblue',
                           fg="black")

    def create_ball(self):
        self.ball = self.Game.canevas.create_oval(390, 480,
                                                  390 + 20, 480 + 20,
                                                  fill='red')

    def lancer_balle(self, event):
        if self.static == False:
            return 0
        else:
            self.label.pack_forget()
            self.animation()
            self.static = False

    def animation(self):
        if self.Game.canevas.coords(self.ball)[1] < 0:
            self.dy = -1 * self.dy
        if self.Game.canevas.coords(self.ball)[3] > 600:
            self.Game.leave_loose_game()
            return 0
        if self.Game.canevas.coords(self.ball)[0] < 0:
            self.dx = -1 * self.dx
        if self.Game.canevas.coords(self.ball)[2] > 800:
            self.dx = -1 * self.dx
        self.Game.canevas.move(self.ball, self.dx, self.dy)
        self.Game.root.after(20, self.animation)
        # collision paddle
        if len(self.Game.canevas.find_overlapping(self.Game.canevas.coords(self.Game.paddle.paddle)[0],
                                                  self.Game.canevas.coords(self.Game.paddle.paddle)[1],
                                                  self.Game.canevas.coords(self.Game.paddle.paddle)[2],
                                                  self.Game.canevas.coords(self.Game.paddle.paddle)[3])) > 1:
            self.Game.ball.dy = -1 * self.Game.ball.dy
        # collision briques
        for i in self.Game.brick.bricks:
            if len(self.Game.canevas.find_overlapping(self.Game.canevas.coords(i)[0],
                                                      self.Game.canevas.coords(i)[1],
                                                      self.Game.canevas.coords(i)[2],
                                                      self.Game.canevas.coords(i)[3])) > 1:
                self.Game.ball.dy = -1 * self.Game.ball.dy
                # Change la couleur / solidité de la brique
                color = self.Game.canevas.gettags(i)
                if color == ('blue',):
                    self.Game.brick.bricks.remove(i)
                    self.Game.canevas.delete(i)
                elif color == ('green',):
                    self.Game.canevas.itemconfig(i, fill='blue', tag='blue')
                elif color == ('yellow',):
                    self.Game.canevas.itemconfig(i, fill='green', tag='green')
                elif color == ('red',):
                    self.Game.canevas.itemconfig(i, fill='yellow', tag='yellow')
                else:
                    print('Error')

                if len(self.Game.brick.bricks) == 0:
                    self.continue_game()

    def continue_game(self):
        counter = 0
        counter += 1
        self.Game.leave_win_game()
        return counter

# Destroy the ball first !
