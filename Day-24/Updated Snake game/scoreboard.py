from turtle import Turtle

FONT = ("courier", 24, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())

        self.hideturtle()
        self.goto(0, 260)
        self.penup()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} Highscore:{self.highscore}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over.", align=ALIGNMENT, font=FONT)

    def increase_scoreboard(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w+") as data_score:
                data_score.write(str(self.highscore))
        self.score = 0



        self.update_scoreboard()
