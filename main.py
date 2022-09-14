import turtle
import pandas
from write_and_locate import StateLabel
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# print(answer_state)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

state_labeler = StateLabel()
score = 0

game_on = True

data = pandas.read_csv("50_states.csv")

states = data["state"].to_list()

guessed_states = []


while score < len(states):

    answer_state = screen.textinput(title = f"{score}/{len(states)} States Correct", prompt = "What's another state's name?").title()

    if answer_state == "Exit":
        break


    if answer_state in states:

        guessed_states.append(answer_state)
        state_xcor = data[data.state == answer_state].x.to_list()
        state_ycor = data[data.state == answer_state].y.to_list()
        state_labeler.write_and_locate(state_xcor[0], state_ycor[0], answer_state)
        score += 1

states_text = states

for i in range(len(guessed_states)):

   if guessed_states[i] in states_text:
        states_text.remove(guessed_states[i])

states_dic = {
    "States to learn" : states_text
}


states_to_learn = pandas.DataFrame(states_dic)
states_to_learn.to_csv("states_to_learn.csv")


    

    


    

