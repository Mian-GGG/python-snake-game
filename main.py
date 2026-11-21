import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = t.Screen()
screen.setup(600 + 4, 600 + 4)
screen.screensize(600, 600, bg="black")
screen.title("My snake Game")
snake_start_point = 0

is_on = True
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.ycor() > 300 or snake.head.xcor() > 300 or snake.head.ycor() < -300 or snake.head.xcor() < -300:
        snake.reset_snake()
        scoreboard.reset_game()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            snake.reset_snake()
            scoreboard.reset_game()

screen.exitonclick()
