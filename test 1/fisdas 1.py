import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("FISDAS")
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(150)
ball.goto(0, 100)
ball.dy = 3

gravity = 0.1

while True:

    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)

    #check for a bounce
    if ball.ycor() <-300:
         ball.dy *=-1

wn.mainloop()
