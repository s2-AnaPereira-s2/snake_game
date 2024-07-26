from turtle import Turtle
import random



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.food_position()
        
    def food_position(self):
        X = random.randint(-280, 280)
        Y = random.randint(-280, 280)
        self.goto(X, Y)