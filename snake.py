from turtle import Turtle

START_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20


class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    
    def create_snake(self):
        for position in START_POSITIONS:
            self.create_parts(position)
    
    def create_parts(self, position):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.segments.append(snake_part)
        
    def grow_snake(self):
        self.create_parts(self.segments[-1].pos())      

    def move(self):
        for part_num in range(len(self.segments)-1, 0, -1):
            self.segments[part_num].goto(self.segments[part_num - 1].pos()) 
        self.head.forward(MOVE_DISTANCE)
    
    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)    
 
        
    
        
        

       
        
