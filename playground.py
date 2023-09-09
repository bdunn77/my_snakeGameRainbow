# from turtle import Turtle, Screen
# import time
# screen = Screen()
# screen.tracer(0)
#
# block_start_positions = [(0, 0), (-20, 0), (-40, 0)]
#
# class Snake:
#     def __init__(self):
#         self.blocks_positions = []
#
#     def start(self):
#         for position in block_start_positions:
#             snake = Turtle("square", 200)
#             snake.penup()
#             snake.color("white")
#             snake.goto(position)
#             screen.update()
#             self.position.append(position)
#
#
#     # def move(self, which_way):
#         #if up, move up, etc. block in position 0 changes first
#         screen.onkey(fun, "up")
#         blocks[0].forward(20)
#
#     for block_num in range(len(blocks) - 1, 0, -1):
#         """1 goes to position 0, 2 goes to 1, etc"""
#         new_x = blocks[block_num - 1].xcor()
#         new_y = blocks[block_num - 1].ycor()
#         blocks[block_num].goto(new_x, new_y)
#
#
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(.1)
#
#
# snake = Snake()
#
#
#
# screen.exitonclick()
