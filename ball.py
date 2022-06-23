from turtle import Turtle

WIDTH = 1
HEIGHT = 1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Move the ball on the screen"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        """
        Change the movement of the ball about the x-axis (bounced with paddles)
        in the opposite direction and increase ball's speed after bounce
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        """
        Change the movement of the ball about the y-axis in the opposite direction
        """
        self.y_move *= -1

    def reset_position(self):
        """return ball to the start position and change ball's movement in the opposite direction"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
