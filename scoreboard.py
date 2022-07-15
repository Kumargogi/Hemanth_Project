from turtle import Turtle

FONT=("courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-380,260)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def level_update(self):
        self.level += 1
        self.score_update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=FONT)