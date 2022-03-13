import turtle
import pandas as pd

data = pd.read_csv('50_states.csv')

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("U.S. states game")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50 states correct", prompt="Input another state").title()
    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for state in all_states:
        if answer == state:
            guessed_state.append(state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer)

screen.exitonclick()
