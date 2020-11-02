import random
import turtle
import time
# screen
wn = turtle.Screen()
wn.bgcolor("green")
#wn.window_height()
#wn.window_width()
wn.setup(width=1080, height=720)
wn.tracer(0)

#border
border = turtle.Turtle()
border.penup()
border.goto(300, 300)
border.pendown()
for _ in range(4):
    border.right(90)
    border.forward(600)
    border.ht()

# snake
snakehead = turtle.Turtle()
snakehead.speed(0)
snakehead.color("black")
snakehead.shape("square")
snakehead.penup()
snakehead.goto(0, 0)
snakehead.direction = "stop"

#food
food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0, 200)

#SCORE
points = turtle.Turtle()
points.color("white")
points.penup()
points.goto(0, 320)
points.ht()
points.speed(0)

points.write("Score:0 HighScore:0", align="center", font=("arial", 24, "normal"))


segments = []
score = 0
high_score = 0

def move():
    '''if snakehead.ycor() > wn.window_height()/2:
        pass
    if snakehead.xcor() > wn.window_width()/2:
        pass
    '''
    if snakehead.direction is "up":
        y = snakehead.ycor()
        snakehead.sety(y + 20)
    if snakehead.direction is "down":
        y = snakehead.ycor()
        snakehead.sety(y - 20)
    if snakehead.direction is "right":
        x = snakehead.xcor()
        snakehead.setx(x + 20)
    if snakehead.direction is "left":
        x = snakehead.xcor()
        snakehead.setx(x - 20)


def goup():
    if snakehead.direction != "down":
        snakehead.direction = "up"
def godown():
    if snakehead.direction != "up":
        snakehead.direction = "down"
def goright():
    if snakehead.direction != "left":
        snakehead.direction = "right"
def goleft():
    if snakehead.direction != "right":
        snakehead.direction = "left"

#keyboard
wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goright, "d")
wn.onkeypress(goleft, "a")


while True:
    wn.update()
    #border collision
    if snakehead.xcor() > 290 or snakehead.xcor() < -290 or snakehead.ycor() > 290 or snakehead.ycor() < -290:
        time.sleep(1)
        snakehead.goto(0, 0)
        snakehead.direction = "stop"
        for j in segments:
            j.goto(1000, 1000)
        segments.clear()
        score = 0
        points.clear()
        points.write("Score:{} HighScore:{}".format(score, high_score), align="center", font=("arial", 24, "normal"))

    if snakehead.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        #new segment
        segment = turtle.Turtle()
        segment.speed(0)
        segment.color("blue")
        segment.shape("square")
        segment.penup()
        segments.append(segment)

        score += 10
        if score > high_score:
            high_score = score
        points.clear()
        points.write("Score:{} HighScore:{}".format(score, high_score), align="center", font=("arial", 24, "normal"))

    #moving
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        x = snakehead.xcor()
        y = snakehead.ycor()
        segments[0].goto(x, y)
    move()
    #body collision
    for j in segments:
        if j.distance(snakehead) < 20:
            time.sleep(0.5)
            snakehead.goto(1000, 1000)
            snakehead.direction = "stop"

            for j in segments:
                j.goto(1000, 1000)
            segments.clear
            score = 0
            points.clear()
            points.write("Score:{} HighScore:{}".format(score, high_score), align="center",
                         font=("arial", 24, "normal"))

    time.sleep(0.1)

wn.mainloop()
