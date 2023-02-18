import turtle
from TurtleBlueprint import TurtleObject
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = turtle.textinput("Turtle Race!", "Which turtle do you want to win? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y = [-70, -50, -30, -10, 10, 30]

turtle_list = []
for turtle in range(0, 6):
    new_turtle = Turtle(shape="arrow")
    new_turtle.penup()
    new_turtle.color(colours[turtle])
    new_turtle.goto(x=-230, y=y[turtle])
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle won!")
            else:
                print(f"You lost! The {winning_color} turtle won!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)





screen.exitonclick()
