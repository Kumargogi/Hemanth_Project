import time
from turtle import  Screen
from movingturtle import Man
from car_manager import Car
from scoreboard import Scoreboard

screen= Screen()
screen.setup(width=800,height=600)
screen.tracer(0)

man1=Man()
car=Car() #creating objects
score=Scoreboard()

screen.listen()
screen.onkey(man1.go_up,"Up")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if man1.ycor() > 290:
        man1.collision_y()
        car.level_up() #leveling up
        score.level_update()

    #screen.update()
    car.create_car()
    car.move_car()
    #collision with car
    for each_car in car.all_cars:
        if each_car.distance(man1) <20:
            score.game_over()
            game_is_on=False



screen.exitonclick()
