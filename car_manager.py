from turtle import Turtle
import random
car_colors=["red","blue","yellow","orange","purple"]
move_dist=5
moving_increase=10

class Car():
    def __init__(self):
        self.all_cars=[]
        self.car_speed=move_dist

    def create_car(self):
        ran_chance=random.randint(1,6)
        if ran_chance==1: #for every 6 times while loop it creates a car
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(car_colors))
            new_y=random.randint(-240,290)
            new_car.goto(400,new_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car1 in self.all_cars:
            car1.backward(self.car_speed)

    def level_up(self):
        self.car_speed += moving_increase




