# Simple pong in python3 for the training.
# By @blynd

#building the app inside of turtle for a visual aid.  bult in python3
import turtle

##  Classes will be added later.
# Controls the visual screen
win = turtle.Screen()
win.title('Pong by @blynd')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape('square')
paddle_1.color('blue')
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)


# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape('square')
paddle_2.color('red')
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(+350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)


# Function
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

# Function
def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


# Keyboard binding
win.listen()
win.onkeypress(paddle_1_up, 'w')
win.onkeypress(paddle_1_down, 's')
win.onkeypress(paddle_2_up, 'Up')
win.onkeypress(paddle_2_down, 'Down')


#Main game loop
while True:
    win.update()