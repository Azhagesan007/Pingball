from turtle import Turtle

PLAYER1 = ((-380, 20), (-380, 0), (-380, -20))
PLAYER2 = ((390, 20), (390, 0), (390, -20))
MOVE_DISTANCE = 20


class Paddle:
    """It manages the paddle of the game"""
    def __init__(self):
        self.location1 = []
        self.location2 = []
        self.create_paddle()
        self.head1 = self.location1[0]
        self.head2 = self.location2[0]

    def create_paddle(self):
        for item1 in PLAYER1:
            t = Turtle()
            t.shape("square")
            t.color("white")
            t.penup()
            t.setheading(90)
            t.goto(item1)
            self.location1.append(t)

        for item2 in PLAYER2:
            t = Turtle()
            t.shape("square")
            t.color("white")
            t.penup()
            t.setheading(90)
            t.goto(item2)
            self.location2.append(t)

    def center_line(self):
        self.head1.goto(0, 250)
        self.head1.pendown()
        self.head1.goto(0, -250)
        self.head1.penup()
        self.head1.goto(-380, 20)

    def interchange1(self):
        x1 = self.location1[1].xcor()
        y1 = self.location1[1].ycor()
        x2 = self.location1[2].xcor()
        y2 = self.location1[2].ycor()
        self.location1[1].goto(x2, y2)
        self.location1[2].goto(x1, y1)

    def interchange2(self):
        x1 = self.location2[1].xcor()
        y1 = self.location2[1].ycor()
        x2 = self.location2[2].xcor()
        y2 = self.location2[2].ycor()
        self.location2[1].goto(x2, y2)
        self.location2[2].goto(x1, y1)

    def move2(self):
        self.head2.forward(MOVE_DISTANCE)
        self.head2.forward(MOVE_DISTANCE)
        self.head2.forward(MOVE_DISTANCE)

    def move1(self):
        self.head1.forward(MOVE_DISTANCE)
        self.head1.forward(MOVE_DISTANCE)
        self.head1.forward(MOVE_DISTANCE)

    def forward1(self):
        y = self.head1.ycor()
        if y < 250:
            if self.head1.heading() == 270:
                self.head1.setheading(90)
                self.move1()
                self.interchange1()
            for item in range(len(self.location1)-1, 0, -1):
                self.location1[item].goto(self.location1[item-1].xcor(), self.location1[item-1].ycor())
            self.head1.forward(MOVE_DISTANCE)

    def forward2(self):
        y = self.head2.ycor()
        if y < 250:
            if self.head2.heading() == 270:
                self.head2.setheading(90)
                self.move2()
                self.interchange2()
            # self.head2.setheading(90)
            else:
                for item in range(len(self.location2)-1, 0, -1):
                    self.location2[item].goto(self.location2[item-1].xcor(), self.location2[item-1].ycor())
                self.head2.forward(MOVE_DISTANCE)

    def backward1(self):
        y = self.head1.ycor()
        if y > -250:
            if self.head1.heading() == 90:
                self.head1.setheading(270)
                self.move1()
                self.interchange1()

            else:
                for item in range(len(self.location1)-1, 0, -1):
                    self.location1[item].goto(self.location1[item-1].xcor(), self.location1[item-1].ycor())
                self.head1.forward(MOVE_DISTANCE)

    def backward2(self):
        y = self.head2.ycor()
        if y > -250:
            if self.head2.heading() == 90:
                self.head2.setheading(270)
                self.move2()
                self.interchange2()

            else:
                for item in range(len(self.location2)-1, 0, -1):
                    self.location2[item].goto(self.location2[item-1].xcor(), self.location2[item-1].ycor())
                self.head2.forward(MOVE_DISTANCE)
