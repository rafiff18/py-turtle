import turtle as t
import random

rafif = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

rafif.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        rafif.color(random_color())
        rafif.circle(100)
        rafif.setheading(rafif.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()


