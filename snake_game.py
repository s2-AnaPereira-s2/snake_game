from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ana the Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()



screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.listen()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.13)
    snake.move()
    
    #DETECT FOOD 
    
    if food.distance(snake.head) < 15:
        food.food_position()
        score.score_count()
        snake.grow_snake()
    
    #DETECT WALL
     
    elif snake.head.xcor() > 295.0 or snake.head.xcor() < -300.0 or snake.head.ycor() > 300.0 or snake.head.ycor() < -295.0:
        game_on = False
        score.game_over()
    
    #DETECT SNAKE
    
    for snake_parts in snake.segments[1::]:
        if snake.head.pos() == snake_parts.pos():
            game_on = False
            score.game_over()
     
         
   
    
    








screen.exitonclick()




        
   
        












