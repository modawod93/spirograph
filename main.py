import turtle as t
import random

tim = t.Turtle()
tod = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# speed = [0, 10, 6, 3, 1, 10, 0, 0]

# tim.speed(random.choice(speed))
# tod.speed(random.choice(speed))

tim.speed(0)
tod.speed(0)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tod.color(random_color())
        tod.circle(50)
        tod.setheading(tod.heading() + size_of_gap)

def not_draw_spirograph():
    for _ in range(100):    
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)

# This function will alternate between tim and tod to give the effect of simultaneous drawing
def alternate_drawing():
    draw_spirograph(5)
    not_draw_spirograph()

# Use ontimer to call the drawing functions without using threads
def draw_tim():
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + 10)
    t.ontimer(draw_tim, 100)  # Schedule the next call

def draw_tod():
    tod.color(random_color())
    tod.circle(50)
    tod.setheading(tod.heading() + 5)
    t.ontimer(draw_tod, 100)  # Schedule the next call

# Start the alternating drawing for both turtles
draw_tim()
draw_tod()

screen = t.Screen()
screen.exitonclick()
