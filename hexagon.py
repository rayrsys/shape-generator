import turtle
t=turtle.Turtle()
i=turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("green")
i.pencolor("red")
a=0
b=0
c=0
d=0
while True:
    t.forward(a)
    t.right(b)
    i.forward(c)
    i.right(d)
    a+=3
    b+=1
    c+=2
    d+=1
    if b== 210 or d == 210:
       break
    i.hideturtle()
    t.hideturtle()
turtle.done()

