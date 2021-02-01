import turtle
import pandas
import random
import time
df = pandas.read_csv("state_info.csv")

display = turtle.Screen()
display.setup(width=750, height=730)
image = "final.gif"
display.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
display.colormode(255)


def color_selector():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

states = df["states"].tolist()
def check_response():
    if user_response in states:
        global availability
        availability = True
    else:
        pass
def writer(x,y,name):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    color = color_selector()
    pen.color(color)
    pen.write(name)
status = True
score = 1
states_answered = []
start_time = time.perf_counter()
while status:
    availability = False
    title = f"{score}/29 guess state"
    user_response = display.textinput(title, "what's the name of the state?").title()
    check_response()
    if availability:
        x = df[df["states"] == user_response].x
        x = x.tolist()
        x = x[0]
        y = df[df["states"] == user_response].y
        y = y.tolist()
        y = y[0]
        score += 1
        time.sleep(1)
        writer(x,y,user_response)
        states_answered.append(user_response)
    if user_response == "Quit":
        status = False

states_unanswered = []

for i in states:
    if i in states_answered:
        pass
    else:
        states_unanswered.append(i)
print(states_unanswered)
end_time = time.perf_counter()


turtle.mainloop()
