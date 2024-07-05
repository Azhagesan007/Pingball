from turtle import Turtle
FONT = ("Arial", 24, "normal")
ALIGN = "left"


class Scoreboard:
    """Controls the score unit of the game"""
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.score_turtle = []
        for item in range(0, 2):
            t = Turtle()
            t.color("white")
            t.penup()
            t.hideturtle()
            self.score_turtle.append(t)
        self.player1 = self.score_turtle[0]
        self.player2 = self.score_turtle[1]
        self.player1.goto(-300, 220)
        self.player2.goto(100, 220)

        self.update_score()

    def update_score(self):
        self.player1.write(arg=f"Score : {self.score1}", align=ALIGN, font=FONT)
        self.player2.write(arg=f"Score : {self.score2}", align=ALIGN, font=FONT)

    def update_score1(self):
        self.player1.clear()
        self.player2.clear()
        self.score1 += 1
        self.update_score()

    def update_score2(self):
        self.player1.clear()
        self.player2.clear()
        self.score2 += 1
        self.update_score()

    def game_over(self):
        self.player2.clear()
        self.player1.clear()
        self.player1.goto(0, 0)
        if self.score1 == 10:
            self.player1.write(arg=f"The winner is player 1.\n Player 1 score = {self.score1}\n Player 2 score = {self.score2},", font=FONT)
        else:
            self.player1.write(arg=f"The winner is player 2.\n Player 1 score = {self.score1}\n Player 2 score = {self.score2}", font=FONT)
