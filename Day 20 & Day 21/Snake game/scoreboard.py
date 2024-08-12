from turtle import Turtle
FONT = ("courier", 24, "normal")
ALIGNMENT = "center"
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 260)
        self.penup()
        self.color("white")
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)

    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
