# Simple pong in python3 for the training.
# By @blynd

#building the app inside of turtle for a visual aid.  bult in python3
import turtle

wn = turtle.Screen()
wn.title('Pong by @blynd')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)



#Main game loop
while True:
    wn.update()