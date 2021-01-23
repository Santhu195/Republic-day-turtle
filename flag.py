
import turtle
import winsound

# creating background screen
sc = turtle.Screen()
sc.setup(width=800,height=600)
sc.bgcolor('black')

# playing music
winsound.PlaySound('anthem.wav',winsound.SND_ASYNC)

def create_pole():

    # creating flag pole
    pole = turtle.Turtle()
    pole.color('white')
    pole.shape('square')
    pole.penup()
    pole.setposition(-300,-280)
    pole.pendown()
    pole.goto(-300,280)
    
create_pole()
flag = turtle.Turtle()
flag.color('white')
flag.penup()
flag.setposition(-300,270)
flag.pendown()

length = 400
width = 80

def rect(color):
    flag.fillcolor(color)
    flag.begin_fill()
    flag.forward(length)
    flag.right(90)
    flag.forward(width)
    flag.right(90)
    flag.forward(length)
    flag.right(180)
    flag.end_fill()

rect('orange')
rect('white')
rect('green')

flag.left(90)
flag.forward(width*3)
flag.hideturtle()

def create_flag():

    # drawing wheel
    wheel = turtle.Turtle()
    # Big blue Circle
    wheel.penup()
    wheel.goto(-100, 115)
    wheel.pendown()
    wheel.color("navy")
    wheel.begin_fill()
    wheel.circle(37)
    wheel.end_fill()

    # Big White Circle
    wheel.penup()
    wheel.goto(-100, 124)
    wheel.pendown()
    wheel.color("white")
    wheel.begin_fill()
    wheel.circle(29)
    wheel.end_fill()

    # Small Blue Circle
    wheel.penup()
    wheel.color("navy")
    wheel.goto(-100, 140)
    wheel.pendown()
    wheel.begin_fill()
    wheel.circle(10)
    wheel.end_fill()
    # Spokes
    wheel.penup()
    wheel.goto(-100,150)
    wheel.pendown()
    wheel.pensize(2)
    for i in range(24):
        wheel.forward(30)
        wheel.backward(30)
        wheel.left(15)

create_flag()
# writing text
text = turtle.Turtle()
text.hideturtle()
text.speed(2)

def write(message,pos,color):
    x,y = pos
    text.color(color)
    text.penup()
    text.goto(x,y)
    text.pendown()
    style = ('Courier',40,'italic')
    text.write(message,font=style)

write('Happy',(60,-80),'orange')
write('Rep',(10,-140),'white')
write('ub',(105,-140),'blue')
write('lic',(167,-140),'white')
write('Day',(70,-200),'green')
write('2021',(50,-270),'white')


turtle.done()