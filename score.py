import turtle


class Score:
    def __init__(self, score=0):
        self.score = score
        self.screen = turtle.Screen()
        self.t = turtle.Turtle()
        self.t.hideturtle()

    def set_score(self, score):
        self.score = score

    def run(self):
        self.t.clear()
        self.t.pencolor('mediumvioletred')
        self.t.penup()
        self.t.goto(330, 240)
        self.t.pendown()
        self.t.write(f"{self.score}", font=("Verdana", 32, "normal"))

    def update(self, new_score):
        self.score = self.score + new_score
        self.run()

    def __str__(self):
        return f"Score: {self.score}"
