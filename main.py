import turtle
turtle.bgcolor('blueviolet')
from random import *
window = turtle.Screen()
window.setup(700, 700)
border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.pensize(5)
border.color('red')
border.up()
border.goto(300, 300)
border.down()
border.goto(300, -300)
border.goto(-300, -300)
border.goto(-300, 300)
border.goto(300, 300)
boll = turtle.Turtle()
boll.hideturtle()
boll.shape('circle')
boll.up()
randx = randint(-229, 290)
randy = randint(-229, 290)

boll.goto(randx, randy)

boll.showturtle()
dx = 4
dy = 5
while True:
    x, y = boll.position()
    if x + dx >= 300 or x + dx <= -300:
        dx = -dx
    if y + dy >= 300 or y + dy <= -300:
        dy = -dy
    boll.goto(x+dx, y+dy)      
window.mainloop()
