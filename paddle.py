from turtle import Turtle

WIDTH = 5
HEIGHT = 1
X_POSITION = 350
Y_POSITION = 0


class Paddle(Turtle):

    def __init__(self, side):
        """Argument: side: as string "left" or "right" for paddle's side"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.penup()
        self.choose_side(side)

    def go_up(self):
        """Move a paddle up"""
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Move a paddle down"""
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)

    def choose_side(self, side):
        if side == "right":
            self.goto(X_POSITION, Y_POSITION)
        elif side == "left":
            self.goto(-X_POSITION, Y_POSITION)
