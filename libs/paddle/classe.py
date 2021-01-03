class Paddle:
    """
    Class representing a paddle
       Author : Mathis Dory, Eliott Lepage
       Date : November 2020
       This class is used to create an animate Paddle which moves from right to left
    """
    def __init__(self, game):
        """
        Creation of all the features of the paddle : width, height, movement speed
        Bind <motion> for the object paddle : it moves when the user moves the mouse

        PRE:
            Game class is running
        POST:
           - Creation of the paddle label which represents the paddle in the Graphic User Interface
           - Binding of the movement of the paddle
        RAISES :
            -
        """
        self.Game = game
        self.dx = 1
        self.paddle = self.Game.canevas.create_rectangle(370, 500, 370 + 60, 500 + 8, fill='grey')
        self.Game.root.bind("<Motion>", self.motion)

    def motion(self, event):
        """
        This function changes the coordinates of the paddle when the user moves the mouse and launch the ball

        PRE : event is the action of moving the paddle from right to left
        POST :
            - It modifies the coordinates of the paddle
            - Call self.Game.ball.launch_ball : the ball is launched from the paddle
        RAISES :
            -
        """
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
