from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
fin = open("scores.txt", "r")
HIGHSCORE = fin.read()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(HIGHSCORE)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setheading(90)
        self.forward(260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.highscore}" , align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
        fout = open("scores.txt", "w")
        fout.write(str(self.highscore))
        fout.close()
    """def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= ALIGNMENT, font=FONT)"""

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

