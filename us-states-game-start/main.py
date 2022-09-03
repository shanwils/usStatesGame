import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.tracer(0)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
answer_list = []

while len(answer_list) < 50:
    answer_state = screen.textinput(title=f"{len(answer_list)}/ 50 guessed",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        states_remaining = [state for state in states if state not in answer_list]
        new_data = pandas.DataFrame(states_remaining)
        new_data.to_csv("states_to_learn.csv")

        break

    if answer_state in states:
        answer_row = data[data.state == answer_state]
        x_coor = int(answer_row.x)
        y_coor = int(answer_row.y)
        turtle.goto(x_coor, y_coor)
        turtle.write(answer_state, align=ALIGNMENT, font=FONT)
        answer_list.append(answer_state)


