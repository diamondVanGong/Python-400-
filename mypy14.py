import turtle
t=turtle.Pen()
my_colors=("red","green","yellow","black")
t.width(4)
t.speed(1)
for i in range(100):#0 1 2 3 4
    t.penup()
    t.goto(0,-i*10)   #0 -100 -200 -300 -400
    t.pendown()
    t.color(my_colors[i%len(my_colors)])
    t.circle(100+i*10)
turtle.done()#程序执行完以后，窗口依旧还在

