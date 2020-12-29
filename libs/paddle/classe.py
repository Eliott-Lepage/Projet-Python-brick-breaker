from tkinter import *


class Paddle():
    def __init__(self, Game):
        self.Game = Game
        self.dx = 1
        self.paddle = self.Game.canevas.create_rectangle(370, 500, 370 + 60, 500 + 8, fill='grey')
        self.Game.root.bind("<Motion>", self.motion)

    def motion(self, event):
        if event.x - 30 <= 0:
            self.Game.canevas.coords(self.paddle, 0, 500, 60, 500 + 8)
            if self.Game.ball.static:
                self.Game.root.bind("<Button-1>", self.Game.ball.launch_ball)
                self.Game.canevas.coords(self.Game.ball.ball, 20, 480,
                                         40, 480 + 20)

        elif event.x + 30 > 800:
            self.Game.canevas.coords(self.paddle, 740, 500, 800, 500 + 8)
            if self.Game.ball.static:
                self.Game.root.bind("<Button-1>", self.Game.ball.launch_ball)
                self.Game.canevas.coords(self.Game.ball.ball, 760, 480,
                                         780, 480 + 20)
        else:
            self.Game.canevas.coords(self.paddle, event.x - 30, 500, event.x + 30, 500 + 8)
            if self.Game.ball.static:
                self.Game.root.bind("<Button-1>", self.Game.ball.launch_ball)
                self.Game.canevas.coords(self.Game.ball.ball, event.x - 10, 480,
                                         event.x + 10, 480 + 20)
