import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

tim.speed("fastest")
tim.dot(20, random.choice(random_color()))