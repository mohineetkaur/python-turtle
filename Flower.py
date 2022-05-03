import turtle

t=turtle.Turtle()
turtle.bgcolor("white")
turtle.color("blue")
turtle.pensize(2)
turtle.speed(0)

for i in range(150):
    turtle.circle(190-i,90)
    turtle.lt(90)
    turtle.circle(190-i,90)
    turtle.lt(18) 

turtle.hideturtle()
turtle.mainloop()            