class Ball:
    """Class representing a ball

       Author : Mathis Dory, Eliott Lepage
       Date : November 2020
       This class is used to create an animate ball
    """
    def __init__(self, game):
        """This builds a ball and bind right click to launch the ball.

                PRE :
                    Game class is running
                POST :
                    call launch_ball() if user use Button-1
                RAISES :
                    -
        """
        self.dx = 2
        self.dy = -6
        self.Game = game
        self.static = True
        self.Game.root.bind("<Button-1>", self.launch_ball)
        self.label = self.Game.canevas.create_text(400, 300, text="Clique gauche pour lancer la balle",
                                                   font=("Arial", 25))
        self.ball = self.Game.canevas.create_oval(390, 480,
                                                  390 + 20, 480 + 20,
                                                  fill='red')

    def launch_ball(self, event):
        """Remove instruction text and start ball animation.

                PRE :
                    event is calling by right click
                POST :
                    return 0 is self.static is False
                    call self.animation() if self.static is True
                RAISES :
                    -
        """
        if not self.static:
            return 0
        else:
            self.Game.canevas.itemconfigure(self.label, text="")
            self.animation()
            self.static = False
            self.Game.canevas.pack()

    def animation(self):
        """Give movement to the ball and modify score, lifes and bricks.

                PRE :
                    -
                POST :
                    call self.Game.leave_loose_game() methods and return 0 if self.Game.life == 0
                    call self.Game.leave_win_game() methods if len(self.Game.brick.bricks) == 0
                RAISES :
                    -
        """
        if self.Game.canevas.coords(self.ball)[1] < 0:
            self.dy = -1 * self.dy
        if self.Game.canevas.coords(self.ball)[3] > 600:
            self.Game.life -= 1
            self.Game.canevas.itemconfigure(self.Game.lives_label, text="Lives : " + str(self.Game.life))
            self.Game.root.unbind("<Button-1>")  # empeche le spam click et donc de faire lag le programme
            self.static = True  # remet la balle en position initiale
            self.dy = -1 * self.dy  # Permet de relancer la balle vers le haut pour le nouveau lancer au lieu part
            # dans le paddle et lag

            if self.Game.life == 0:
                self.Game.leave_loose_game()
            return 0

        if self.Game.canevas.coords(self.ball)[0] < 0:
            self.dx = -1 * self.dx
        if self.Game.canevas.coords(self.ball)[2] > 800:
            self.dx = -1 * self.dx
        self.Game.canevas.move(self.ball, self.dx, self.dy)
        animate = self.Game.root.after(15,
                                       self.animation)  # le premier parametre indique la vitesse de la balle,
        # plus petit = plus rapide

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
                self.Game.score += 100
                self.Game.canevas.itemconfigure(self.Game.score_label, text="Score : " + str(self.Game.score))

                # Change the color and solidity of the brick
                color = self.Game.canevas.gettags(i)
                if color == ('white',):
                    self.Game.brick.bricks.remove(i)
                    self.Game.canevas.delete(i)
                elif color == ('pink',):
                    self.Game.life += 1
                    self.Game.canevas.itemconfigure(self.Game.lives_label,
                                                    text="Lives : " + str(self.Game.life))
                    self.Game.brick.bricks.remove(i)
                    self.Game.canevas.delete(i)
                elif color == ('yellow',):
                    self.Game.canevas.itemconfig(i, fill='white', tag='white')
                elif color == ('orange',):
                    self.Game.canevas.itemconfig(i, fill='yellow', tag='yellow')
                elif color == ('red',):
                    self.Game.canevas.itemconfig(i, fill='orange', tag='orange')
                elif color == ('#8757D5',):
                    self.Game.canevas.itemconfig(i, fill='red', tag='red')
                elif color == ('blue',):
                    self.Game.canevas.itemconfig(i, fill='#8757D5', tag='#8757D5')
                elif color == ('green',):
                    self.Game.canevas.itemconfig(i, fill='blue', tag='blue')
                elif color == ('grey',):
                    self.Game.canevas.itemconfig(i, fill='green', tag='green')

                if len(self.Game.brick.bricks) == 0:
                    self.Game.root.unbind("<Button-1>")  # empeche le spam click et donc de faire lag le programme
                    self.Game.root.after_cancel(animate)
                    self.Game.canevas.coords(self.Game.paddle.paddle, 370, 500, 370 + 60, 500 + 8)
                    self.Game.canevas.coords(self.ball, 390, 480,
                                             390 + 20, 480 + 20)
                    self.static = True
                    self.dy = -6
                    self.Game.leave_win_game()
