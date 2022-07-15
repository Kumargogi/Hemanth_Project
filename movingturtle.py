from turtle import Turtle

class Man(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(0,-280)

    def go_up(self):
        new_y=self.ycor()+10
        self.goto(self.xcor(),new_y)

    def collision_y(self):
        self.goto(0,-280)


