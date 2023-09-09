from turtle import Turtle

from food import Food


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self, food):
        self.food = food
        self.block_positions = []
        self.create_snake()
        self.head = self.block_positions[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self, position):
        block = Turtle("square", 200)
        block.color(self.get_food_list())
        block.penup()
        block.goto(position)
        self.block_positions.append(block)
    def extend(self):
        self.add_segment(self.block_positions[-1].position())
    def get_food_list(self):
        return Food.food_colors[-2]






    def move(self):
        for block_num in range(len(self.block_positions) -1, 0, -1):
            new_x = self.block_positions[block_num - 1].xcor()
            new_y = self.block_positions[block_num - 1].ycor()
            self.block_positions[block_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
