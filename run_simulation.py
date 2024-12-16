import turtle
import random
from ball import Ball
from score import Score
from player import Player


class Simulation:
    def __init__(self):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)
        self.ball_radius = 0.02 * self.canvas_width
        turtle.colormode(255)
        self.ball_list = []

        self.player = Player()
        self.score = Score(0)

        self.g_over = False
        self.screen = turtle.Screen()

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(5)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)

    def gen_ball(self):
        for i in range(5):
            color = random.choice(['salmon', 'cornflowerblue', 'gold'])
            x = random.uniform(-1 * self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius)
            y = random.uniform(-1 * self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius)
            vx = 10 * random.uniform(-1.0, 1.0)
            vy = 10 * random.uniform(-1.0, 1.0)
            self.ball_list.append(Ball(color, self.ball_radius, x, y, vx, vy))

        for j in range(2):
            x = random.uniform(-1 * self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius)
            y = random.uniform(-1 * self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius)
            vx = 10 * random.uniform(-1.0, 1.0)
            vy = 10 * random.uniform(-1.0, 1.0)
            self.ball_list.append(Ball('dimgray', self.ball_radius, x, y, vx, vy))

    def run(self):
        self.screen.listen()
        self.screen.onkey(self.player.move_up, "Up")
        self.screen.onkey(self.player.move_down, "Down")
        self.screen.onkey(self.player.move_left, "Left")
        self.screen.onkey(self.player.move_right, "Right")
        self.screen.onkey(self.player.move_up, "w")
        self.screen.onkey(self.player.move_down, "s")
        self.screen.onkey(self.player.move_left, "a")
        self.screen.onkey(self.player.move_right, "d")

        turtle.bgcolor('white')

        self.gen_ball()
        dt = 1.5

        old_ball = 0
        while True:
            turtle.clear()
            self.draw_border()
            for i in range(len(self.ball_list)):
                self.ball_list[i].draw()
                self.ball_list[i].move(dt)
                self.ball_list[i].update_velocity()

            self.score.run()
            turtle.update()

            for ball in self.ball_list:
                if ball.check_hit_player(self.player):
                    if ball.color == 'dimgray':
                        self.g_over = True
                        turtle.clear()
                        turtle.bgcolor('black')
                        turtle.penup()
                        turtle.goto(0, 0)
                        turtle.pencolor('palevioletred')
                        turtle.pendown()
                        turtle.write(f"Game Over", align="center", font=("Verdana", 32, "normal"))
                        turtle.penup()
                        turtle.goto(0, -30)
                        turtle.pendown()
                        turtle.write(self.score, align="center", font=("Verdana", 28, "normal"))
                        turtle.penup()
                        turtle.goto(0, -80)
                        turtle.pencolor('darkgray')
                        turtle.pendown()
                        turtle.write('Enter to play new game', align="center", font=("Verdana", 16, "normal"))
                        turtle.onkey(self.run, "Return")
                        self.score.set_score(0)
                        self.player.set_size(1)
                        self.player.set_position()
                        self.ball_list.clear()
                        turtle.done()
                    elif ball.color == 'salmon':
                        self.score.update(3)
                    elif ball.color == 'cornflowerblue':
                        self.score.update(2)
                    elif ball.color == 'gold':
                        self.score.update(1)

                    self.ball_list.remove(ball)

                    if len(self.ball_list) <= 2 + old_ball:
                        self.gen_ball()
                        self.player.increase_size()
                        old_ball = old_ball + 2
                turtle.update()


simulation = Simulation()
simulation.run()
turtle.done()
