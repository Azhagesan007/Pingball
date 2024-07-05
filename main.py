from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

score = Scoreboard()
s = Screen()
s.setup(width=800, height=500)
s.bgcolor("black")
s.tracer(0)
paddle = Paddle()
paddle.center_line()
ball = Ball()
ball.create_ball()
s.listen()
s.onkeypress(key="Up", fun=paddle.forward2)
s.onkeypress(key="Down", fun=paddle.backward2)
s.onkeypress(key="w", fun=paddle.forward1)
s.onkeypress(key="s", fun=paddle.backward1)
start = True
game_refresh = True
while start:
    s.update()
    time.sleep(0.04)
    if game_refresh:
        time.sleep(2)
        ball.refresh(-45, 45)
        game_refresh = False
    ball.move()

    if ball.ycor() >= 250 or ball.ycor() <= -250:
        ball.hit_wall()

    for item1 in paddle.location1:
        x = item1.xcor()
        y = item1.ycor()
        if ball.distance(x, y) < 15:
            ball.hit_paddle()

    for item2 in paddle.location2:
        x = item2.xcor()
        y = item2.ycor()
        if ball.distance(x, y) < 15:
            ball.hit_paddle()

    if ball.xcor() < -400 or ball.xcor() > 400:
        if ball.xcor() < -400:
            ball.refresh(135, 225)
            score.update_score2()

        if ball.xcor() > 400:
            ball.refresh(-45, 45)
            score.update_score1()
    if score.score1 == 10 or score.score2 == 10:
        score.game_over()
        start = False
s.exitonclick()
