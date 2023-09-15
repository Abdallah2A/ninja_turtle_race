from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=650, height=300)

turtles_color = ["blue3", "purple3", "red3", "orange3"]
turtles = []

y_cor = 75
for color in turtles_color:
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(color)
    timmy.goto(x=-300, y=y_cor)
    y_cor -= 50
    turtles.append(timmy)

ninj_turtles = ["leonardo", "donatello", "raphael", "michelangelo"]

choice = None
while choice not in ninj_turtles:
    choice = screen.textinput(title="Make your choice:", prompt=f"Who will win the race? {ninj_turtles}").lower()
    if choice is None:
        screen.bye()  # Close the window if user presses cancel

choice = ninj_turtles.index(choice)

winner = ""
race_finished = True
while race_finished:
    for turtle in range(len(turtles)):
        turtles[turtle].forward(random.randint(1, 10))
        if turtles[turtle].xcor() >= 280:  # Corrected the condition
            winner = turtle
            race_finished = False

if winner == choice:
    print("Winner")
else:
    print("Loser")

screen.exitonclick()