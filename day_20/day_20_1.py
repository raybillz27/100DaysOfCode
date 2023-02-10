import time
from turtle import Screen
from day_20_3 import Player
from day_20_2 import CarManager
from day_20_4 import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            score.game_over()

    if turtle.ycor() > 280:
        turtle.start_again()
        car_manager.level_up()
        score.new_level()


screen.exitonclick()

