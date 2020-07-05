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
paddle_1.color('red')
paddle_1.penup()
paddle_1.goto(-350, 0)


# Paddle 2



# Ball



#Main game loop
while True:
    win.update()