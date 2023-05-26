import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)
# screen.delay(1000)
step = 20
is_game_over = False

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.update()

screen.listen()
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")

while not is_game_over:
    time.sleep(0.1)
    # screen.l
    snake.move()
    screen.update()

    # Detect collision with food
    if snake.head().distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.add_head()
        screen.update()

    if snake.is_collided((600, 600)):
        is_game_over = True
        scoreboard.game_over()

print("Game Over")
screen.exitonclick()
