import turtle


class Player:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.speed(0)
        self.t.goto(0, 0)
        self.t.shape("turtle")
        self.t.shapesize(stretch_wid=1, stretch_len=1)
        self.t.color("seagreen")
        self.t.setheading(90)
        self.size = 1

        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]

    def move_up(self):
        if self.t.ycor() < self.canvas_height - self.size - 20:
            if self.t.heading() != 90:
                self.t.setheading(90)
                self.t.forward(15)
            self.t.forward(15)

    def move_down(self):
        if self.t.ycor() > -self.canvas_height + self.size + 20:
            if self.t.heading() != -90:
                self.t.setheading(-90)
                self.t.forward(15)
            self.t.forward(15)

    def move_left(self):
        if self.t.xcor() > -self.canvas_width + self.size + 20:
            if self.t.heading() != 180:
                self.t.setheading(180)
                self.t.forward(15)
            self.t.forward(15)

    def move_right(self):
        if self.t.xcor() < self.canvas_width - self.size - 20:
            if self.t.heading() != 0:
                self.t.setheading(0)
                self.t.forward(15)
            self.t.forward(15)

    def increase_size(self):
        self.size = self.size + 0.3
        self.t.shapesize(stretch_wid=self.size, stretch_len=self.size)

    def set_size(self, size):
        self.size = size
        self.t.shapesize(stretch_wid=size, stretch_len=size)

    def set_position(self):
        self.t.goto(0, 0)
        self.t.setheading(90)
