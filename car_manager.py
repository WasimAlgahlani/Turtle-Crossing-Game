from turtle import Turtle
import random

COLORS = ["red", "yellow", "green", "purple", "orange", "blue"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
WIDTH = 1
HEIGHT = 2


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle(shape="square")
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

