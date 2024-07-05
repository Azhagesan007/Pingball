from turtle import Turtle
import random
COLOR = 'red'
SHAPE = 'circle'


class Ball(Turtle):
    """Controls the ball unit of the game"""
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()

    def move(self):
        self.forward(10)

    def random_angle(self, x, y):
        a = random.randint(x, y)
        c = True
        while c:
            if -20 < a < 20:
                a *= 2
            elif -20 > a > 20:
                c = False
            else:
                c = False
            if 160 < a < 200:
                a *= 2
            elif 160 > a > 200:
                c = False
            else:
                c = False
        self.setheading(a)

    def hit_wall(self):
        x = self.heading()
        y = 360 - x
        self.setheading(y)

    def hit_paddle(self):
        x = self.heading()
        y = 180 - x
        self.setheading(y)

    def refresh(self, x, y):
        """Receives the angle range to set"""
        self.goto(0, 0)
        self.random_angle(x, y)

