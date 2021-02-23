from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
turtle_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_start_y = [75, 45, 15, -15, -45, -75]

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
while user_bet.lower() not in turtle_colors:
    user_bet = screen.textinput(title="Make your bet", prompt="Please enter a valid color (red, orange, yellow,"
                                                              " green, blue, purple)")

turtles = [Turtle(shape='turtle') for color in turtle_colors]
for i, turtle in enumerate(turtles):
    turtles[i].penup()
    turtles[i].color(turtle_colors[i])
    turtles[i].goto(-230, turtle_start_y[i])

if user_bet:
    is_race_on = True

winner = "no"
while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 230:
            winner = turtle
            is_race_on = False
            break

if user_bet.lower() == winner.color()[0]:
    print("You won!")
else:
    print("You lost.")
print(f"The {winner.color()[0]} turtle is the winner!")

screen.exitonclick()
