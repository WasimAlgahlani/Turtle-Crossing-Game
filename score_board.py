from turtle import Turtle

FONT = ("Courier", 18, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.update_levels()

    def update_levels(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-235, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def move_to_another_level(self):
        self.level += 1
        self.update_levels()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 80, "bold"))

