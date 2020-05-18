import turtle as trtl
import math as m
import time as t

# set up screen
wn = trtl.Screen()
wn.setup(width = 1.0, height = 1.0)
wn.bgcolor("gray")
wn.bgpic("frogger.gif")

# create custom shapes
frogShape = "frog.gif"
frogLeftShape = "frogLeft.gif"
frogRightShape = "frogRight.gif"
frogBackShape = "frogBack.gif"
car1Shape = "car.gif"
car2Shape = "car2.gif"
car3Shape = "car3.gif"
car4Shape = "car4.gif"
car5Shape = "car5.gif"
splatShape = "splat.gif"
timerBarShape = "timerBar.gif"

wn.addshape(frogShape)
wn.addshape(frogLeftShape)
wn.addshape(frogRightShape)
wn.addshape(frogBackShape)
wn.addshape(car1Shape)
wn.addshape(car2Shape)
wn.addshape(car3Shape)
wn.addshape(car4Shape)
wn.addshape(car5Shape)
wn.addshape(splatShape)
wn.addshape(timerBarShape)

# initialize turtles
scribe = trtl.Turtle(visible = False) # writes everything
scribe._delay(0)
scribe.pencolor("red")
scribe.pu()

frog = trtl.Turtle(shape = frogShape) # player
frog._delay(0)
frog.pu()
frog.seth(90)
frog.sety(-260)

splat = trtl.Turtle(shape = splatShape) # splat that appears on death
splat.pu()
splat._delay(0)
splat.goto(10000, 10000)

timerBar = trtl.Turtle(shape = timerBarShape) # black bar that goes over the green bar
timerBar._delay(0)
timerBar.pu()
timerBar.goto(67, -299)

# lists for the cars
# first digit (listcar>4<1) tells the row from bottom to top
# second digit (listcar4>1<) tells top or bottom, 1 = bottom, 2 = top
listcar11 = []
listcar21 = []
listcar31 = []
listcar41 = []
listcar51 = []
listcar12 = []
listcar22 = []
listcar32 = []
listcar42 = []
listcar52 = []

# create cars
xc = -400 # xc is for initializing the cars at different x coords

for i in range(3):
    car11 = trtl.Turtle(shape = car1Shape)
    car11.pu()
    car11.speed(0)
    car11.goto(xc, -220)
    xc += 285
    listcar11.append(car11)

xc = 400

for i in range(3):
    car21 = trtl.Turtle(shape = car2Shape)
    car21.pu()
    car21.speed(0)
    car21.seth(180)
    car21.goto(xc, -180)
    xc -= 285
    listcar21.append(car21)

xc = -360

for i in range(3):
    car31 = trtl.Turtle(shape = car3Shape)
    car31.pu()
    car31.speed(0)
    car31.goto(xc, -140)
    xc += 285
    listcar31.append(car31)

xc = 400

for i in range(2):
    car41 = trtl.Turtle(shape = car4Shape)
    car41.pu()
    car41.speed(0)
    car41.seth(180)
    car41.goto(xc, -100)
    xc -= 427
    listcar41.append(car41)

xc = -320

for i in range(2):
    car51 = trtl.Turtle(shape = car5Shape)
    car51.pu()
    car51.speed(0)
    car51.goto(xc, -60)
    xc += 427
    listcar51.append(car51)

xc = -400

for i in range(3):
    car12 = trtl.Turtle(shape = car1Shape)
    car12.pu()
    car12.speed(0)
    car12.goto(xc, 20)
    xc += 285
    listcar12.append(car12)

xc = 400

for i in range(3):
    car22 = trtl.Turtle(shape = car2Shape)
    car22.pu()
    car22.speed(0)
    car22.seth(180)
    car22.goto(xc, 60)
    xc -= 285
    listcar22.append(car22)

xc = -360

for i in range(3):
    car32 = trtl.Turtle(shape = car3Shape)
    car32.pu()
    car32.speed(0)
    car32.goto(xc, 100)
    xc += 285
    listcar32.append(car32)

xc = 400

for i in range(2):
    car42 = trtl.Turtle(shape = car4Shape)
    car42.pu()
    car42.speed(0)
    car42.seth(180)
    car42.goto(xc, 140)
    xc -= 427
    listcar42.append(car42)

xc = -320

for i in range(2):
    car52 = trtl.Turtle(shape = car5Shape)
    car52.pu()
    car52.speed(0)
    car52.goto(xc, 180)
    xc += 427
    listcar52.append(car52)

# define functions
def frogForward():
    if frog.ycor() < 260: # player cannot leave game area
        frog.shape(frogShape)
        frog.speed(0)
        frog.seth(90)
        frog.speed(1)
        frog.fd(40)
def frogLeft():
    if frog.xcor() > -400:
        frog.shape(frogLeftShape)
        frog.speed(0)
        frog.seth(180)
        frog.speed(1)
        frog.fd(40)
def frogRight():
    if frog.xcor() < 400:
        frog.shape(frogRightShape)
        frog.speed(0)
        frog.seth(0)
        frog.speed(1)
        frog.fd(40)
def frogBack():
    if frog.ycor() > -260:
        frog.shape(frogBackShape)
        frog.speed(0)
        frog.seth(270)
        frog.speed(1)
        frog.fd(40)
def distance(t1, t2): # checks distance between two turtles
    global timer
    distance = m.sqrt(m.pow(t1.xcor()-t2.xcor(),2) + m.pow(t1.ycor()-t2.ycor(),2))
    if distance < 25:
        timer = 101
        splat.goto(frog.xcor(), frog.ycor())
        frog.ht()
        frog.goto(10000, -10000)
        scribe.goto(-220, -80)
        scribe.write("GAME OVER", font = ("impact", 80, "normal"))

# define keypresses
wn.listen()
wn.onkeypress(frogForward, "w")
wn.onkeypress(frogForward, "W")
wn.onkeypress(frogForward, "Up")
wn.onkeypress(frogLeft, "a")
wn.onkeypress(frogLeft, "A")
wn.onkeypress(frogLeft, "Left")
wn.onkeypress(frogRight, "d")
wn.onkeypress(frogRight, "D")
wn.onkeypress(frogRight, "Right")
wn.onkeypress(frogBack, "s")
wn.onkeypress(frogBack, "s")
wn.onkeypress(frogBack, "Down")

# variables for the timer
timer = 0
seconds = 1

timeStart = t.time()
while True:
    timer += 1 
    if timer == 100: # about a second
        timerBar.fd(14) # move the black bar 1/15th of the green bar
        timer = 0 # reset
        seconds += 1
        if seconds == 16: # when timer ends
            timer = 101 # stop the timer
            splat.goto(frog.xcor(), frog.ycor()) # kill player
            frog.ht()
            frog.goto(10000, -10000)
            scribe.goto(-220, -80)
            scribe.write("GAME OVER", font = ("impact", 80, "normal"))
    for car in listcar11:
        distance(frog, car) # check distance to frog
        if car.xcor() > 410: #check if car is out of bounds
            car.setx(-410) # move car to opposite side
        car.fd(0.8)
    for car in listcar21:
        distance(frog, car)
        if car.xcor() < -410:
            car.setx(410)
        car.fd(0.8)
    for car in listcar31:
        distance(frog, car)
        if car.xcor() > 410:
            car.setx(-410)
        car.fd(0.8)
    for car in listcar41:
        distance(frog, car)
        if car.xcor() < -410:
            car.setx(410)
        car.fd(1.2)
    for car in listcar51:
        distance(frog, car)
        if car.xcor() > 410:
            car.setx(-410)
        car.fd(1.2)
    for car in listcar12:
        distance(frog, car)
        if car.xcor() > 410:
            car.setx(-410)
        car.fd(1.6)
    for car in listcar22:
        distance(frog, car)
        if car.xcor() < -410:
            car.setx(410)
        car.fd(1.6)
    for car in listcar32:
        distance(frog, car)
        if car.xcor() > 410:
            car.setx(-410)
        car.fd(1.6)
    for car in listcar42:
        distance(frog, car)
        if car.xcor() < -410:
            car.setx(410)
        car.fd(2.4)
    for car in listcar52:
        distance(frog, car)
        if car.xcor() > 410:
            car.setx(-410)
        car.fd(2.4)
    if frog.ycor() >= 200:
        frogForward()
        frog.goto(0, -260)
        break # break to enter stage 2

timer = 0
seconds = 0
timerBar.setx(67) # reset black bar

while True:
    timer += 1
    if timer == 100:
        timerBar.fd(14)
        timer = 0
        seconds += 1
        if seconds == 15:
            timer = 101
            splat.goto(frog.xcor(), frog.ycor())
            frog.ht()
            frog.goto(10000, -10000)
            scribe.goto(-220, -80)
            scribe.write("GAME OVER", font = ("impact", 80, "normal"))
    for car in listcar11:
        distance(frog, car)
        if car.xcor() > 410:
            car.setx(-410)
        car.fd(1.6)
    for car in listcar21:
        distance(frog, car)
        if car.xcor() < -410:
            car.setx(410)
        car.fd(1.6)
    for car in listcar31:
        distance(frog, car)
        if car.xcor() > 410:
            car.setx(-410)
        car.fd(1.6)
    for car in listcar41:
        distance(frog, car)
        if car.xcor() < -410:
            car.setx(410)
        car.fd(2.4)
    for car in listcar51:
        distance(frog, car)
        if car.xcor() > 410:
            car.setx(-410)
        car.fd(2.4)
    for car in listcar12:
        distance(frog, car)
        if car.xcor() > 410:
            car.setx(-410)
        car.fd(3.2)
    for car in listcar22:
        distance(frog, car)
        if car.xcor() < -410:
            car.setx(410)
        car.fd(3.2)
    for car in listcar32:
        distance(frog, car)
        if car.xcor() > 410:
            car.setx(-410)
        car.fd(3.2)
    for car in listcar42:
        distance(frog, car)
        if car.xcor() < -410:
            car.setx(410)
        car.fd(4.8)
    for car in listcar52:
        distance(frog, car)
        if car.xcor() > 410:
            car.setx(-410)
        car.fd(4.8)
    if frog.ycor() >= 200:
        timeEnd = t.time()
        timeTotal = int(timeEnd - timeStart)
        break # break to end game
scribe.goto(-190, -80)
scribe.write("YOU WIN!", font = ("impact", 80, "normal"))
scribe.pencolor("orange")
scribe.goto(-80, -110)
scribe.write(str(timeTotal) + " seconds", font = ("impact", 30, "normal"))

wn.mainloop()
