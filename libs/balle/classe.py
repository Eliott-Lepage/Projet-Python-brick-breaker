from tkinter import *
import json


class Ball:
    def __init__(self, Game):
        self.dx = 2
        self.dy = -6
        self.Game = Game
        self.static = True
        self.Game.root.bind("<Button-1>", self.lancer_balle)

        self.create_label()
        self.create_ball()
        self.score = 0
        self.vies = 3
        self.create_score()

        # empaquetage
        self.label.grid(row=1, column=1, pady=245)

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
            self.label.config(text="")
            self.animation()
            self.static = False
            self.Game.canevas.pack()


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
        self.score_label = Label(self.Game.canevas, text="Score : " + str(self.score),
                                 font=("Arial", 15),
                                 bg=None, fg="black")

        # Create label best score
        self.best_score_label = Label(self.Game.canevas, text="Best Score : " + str(max_number),
                                      font=("Arial", 15),
                                      bg=None, fg="black")

        # Create label user
        self.user_name = Label(self.Game.canevas, text="Username : " + user,
                                      font=("Arial", 15),
                                      bg=None, fg="black")

        # Create label lives
        self.lives_label = Label(self.Game.canevas, text="Lives : " + str(self.vies),
                                 font=("Arial", 15),
                                 bg=None, fg="black")

    def update_json_file(self):
        with open("data/save.txt", "r+") as file:
            dictionary = json.load(file)
            user = dictionary["Actual Username"]
            dictionary[user].append(self.score)

        with open("data/save.txt", "w") as file:
            json.dump(dictionary, file)

    def animation(self):
        if self.Game.canevas.coords(self.ball)[1] < 0:
            self.dy = -1 * self.dy
        if self.Game.canevas.coords(self.ball)[3] > 600:
            self.update_json_file()
            self.static = True
            self.vies -= 1
            self.lives_label.config(text="Lives : " + str(self.vies))
            if self.vies == 0:
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

                # Score
                self.score += 100
                self.score_label.config(text="Score : " + str(self.score))

                # Change the color and solidity of the brick
                color = self.Game.canevas.gettags(i)
                if color == ('blue',):
                    self.Game.brick.bricks.remove(i)
                    self.Game.canevas.delete(i)
                elif color == ('pink',):
                    self.vies += 1
                    self.lives_label.config(text="Lives : " + str(self.vies))
                    self.Game.brick.bricks.remove(i)
                    self.Game.canevas.delete(i)
                elif color == ('green',):
                    self.Game.canevas.itemconfig(i, fill='blue', tag='blue')
                elif color == ('yellow',):
                    self.Game.canevas.itemconfig(i, fill='green', tag='green')
                elif color == ('red',):
                    self.Game.canevas.itemconfig(i, fill='yellow', tag='yellow')

                if len(self.Game.brick.bricks) == 0:
                    self.update_json_file()

    def continue_game(self):
        self.Game.leave_win_game()

# Destroy the ball first !
