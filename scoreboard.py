from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__();
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.setpos(0, 270)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"Game Over. Your score is {self.score}", align=ALIGNMENT, font=FONT)
