import turtle    

wn = turtle.Screen()
pen = turtle.Turtle()   

def move():
  pen.forward(10)
  
def func_on_up_key():
  move()


def func_on_down_key():
  move()
 

def func_on_left_key():
  move()


def func_on_right_key():
  move()


# כאן התכנית שלכם תתבצע
  

wn.onkey(func_on_up_key, "up")
wn.onkey(func_on_down_key, "down")
wn.onkey(func_on_left_key, "left")
wn.onkey(func_on_right_key, "right")


pen.shape('square')

# לא לשנות את הקוד מנקודה זו ומטה
wn.listen()

