import turtle

wn = turtle.Screen()
pen = turtle.Turtle()



pen.penup()

def my_click(x,y):

  pen.goto(x,y)
  pen.pendown()
  for i in range(4):
    pen.forward(20)
    pen.left(90)
  pen.penup()



wn.onclick(my_click)

turtle.mainloop()