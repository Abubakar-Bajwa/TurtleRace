from turtle import Turtle, Screen
import random

isRaceOn = False

screen = Screen()
guess = screen.textinput(title="Make your guess", prompt="Which turtle will win the race?").lower()

screen.listen()

colours = ["red", "blue", "green", "orange", "purple"]


y_position = [-100, -50, 0, 50, 100]
turtles_list = []

for i in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colours[i])
    tim.goto(-475, y_position[i])
    turtles_list.append(tim)

if guess:
    isRaceOn = True

while isRaceOn:
    for turtle in turtles_list:
        if turtle.xcor() > 475:
            isRaceOn = False
            winning_colour = turtle.pencolor()
            if guess == winning_colour:
                print(f"You won. The {winning_colour} turtle is the winner")
            else:
                print(f"You lost. The {winning_colour} turtle is the winner")

        distance = random.randint(0, 10)
        turtle.forward(distance)









screen.exitonclick()