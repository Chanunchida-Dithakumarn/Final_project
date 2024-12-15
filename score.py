import turtle


class Score:
    def __init__(self, score=0):
        self.score = score
        self.screen = turtle.Screen()
        self.t = turtle.Turtle()

    def display(self):
        self.t.clear()
        self.t.hideturtle()
        self.t.pencolor('mediumvioletred')
        self.t.penup()
        self.t.goto(200, 70)
        self.t.pendown()
        self.t.write(f"{self.score}", font=("Verdana", 32, "normal"))


s = Score(15)
s.display()

turtle.done()
