import turtle as t
t.bgcolor("black")
t.color("aqua")
t.speed(0)
t.hideturtle()
a=["pink","cyan","white"]
for i in range(200):
    t.pencolor(a[i%3])
    t.forward(i*4)
    t.right(121)
t.done()