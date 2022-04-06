import turtle
import pandas 
import os

# setup
screen = turtle.Screen()
screen.title('U.S states game')
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

file = 'missing states.csv'
if(os.path.exists(file) and os.path.isfile(file)):
  os.remove(file)

correct_guesses = []


data = pandas.read_csv('50_states.csv')
states_list = data.state.to_list()

while len(correct_guesses) < 50:
    ans_state = screen.textinput(title=f"{len(correct_guesses)}/50 states", prompt="Enter state:").title()

    if ans_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)

        new_data.to_csv('missing states.csv')
        break
    if ans_state in states_list:
        state = data[data.state == ans_state]
        if not state.state.item() in correct_guesses:
            correct_guesses.append(state.state.item())
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(x=int(state.x), y=int(state.y))
            t.write(state.state.item())


t = turtle.Turtle()
t.hideturtle()
t.penup()
t.color("red")

if len(correct_guesses) < 50:
    t.goto(x=-330, y=0)
    t.write("see states you've missed as csv file", font=("Verdana", 28, "normal"))
else:
    t.goto(x=-200, y=0)
    t.write("You made it !", font=("Verdana", 35, "normal"))

screen.exitonclick()
