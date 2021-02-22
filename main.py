from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
turtle_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

tim = Turtle(shape='turtle')
tim.color('red')
tim.penup()
tim.goto(-230, 60)

tom = Turtle(shape='turtle')
tom.color('orange')
tom.penup()
tom.goto(-230, 40)

ted = Turtle(shape='turtle')
ted.color('yellow')
ted.penup()
ted.goto(-230, 20)

tucker = Turtle(shape='turtle')
tucker.color('green')
tucker.penup()
tucker.goto(-230, 0)

teddy = Turtle(shape='turtle')
teddy.color('blue')
teddy.penup()
teddy.goto(-230, -20)

timmy = Turtle(shape='turtle')
timmy.color('purple')
timmy.penup()
timmy.goto(-230, -40)

screen.exitonclick()