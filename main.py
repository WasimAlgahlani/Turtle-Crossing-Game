from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.go_forward, "Up")

car_manager = CarManager()

score = ScoreBoard()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_on = False
    if player.finish_line():
        score.move_to_another_level()
        car_manager.increase_speed()


screen.exitonclick()
