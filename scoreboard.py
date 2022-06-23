from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.update_score()

    def update_score(self):
        """update current score"""
        self.write(f"{self.left_score}  {self.right_score}", align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        """increase left score"""
        self.left_score += 1
        self.clear()
        self.update_score()

    def increase_right_score(self):
        """increase right score"""
        self.right_score += 1
        self.clear()
        self.update_score()
