from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")
GAME_OVER_FONT = ("Courier", 100, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 250)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", False, ALIGNMENT, GAME_OVER_FONT)