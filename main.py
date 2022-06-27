import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

game_is_on = True
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG: The Game")
screen.tracer(0)

l_paddle = Paddle((-365, 0))
r_paddle = Paddle((365, 0))
score = ScoreBoard()
ball = Ball()

screen.listen()
screen.onkeypress(l_paddle.move_up, "Up")
screen.onkeypress(l_paddle.move_down, "Down")
screen.onkeypress(r_paddle.move_up, "w")
screen.onkeypress(r_paddle.move_down, "s")

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddles
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 or ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect ball out of bounds - r_paddle
    if ball.xcor() > 415:
        ball.reset_position()
        score.l_point()

    # Detect ball out of bounds - l_paddle
    if ball.xcor() < -415:
        ball.reset_position()
        score.r_point()






screen.exitonclick()
