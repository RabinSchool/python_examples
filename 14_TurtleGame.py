import turtle
import random

lst = []
wn = turtle.Screen()
wn.addshape('rock.gif')
wn.addshape('paper.gif')
wn.addshape('scissor.gif')
wn.addshape('start.gif')
wn.addshape('win.gif')


def select_picture(i):
    if i == 0:
        return 'rock.gif'
    elif i == 1:
        return 'paper.gif'
    else:
        return 'scissor.gif'


winner = turtle.Turtle()
winner.penup()
winner.goto(80, 80)

winner.shape('win.gif')


# for i in range(3):
#     lst.append(turtle.Turtle())
#     lst[i].goto(i*80,0)
#     lst[i].shape(select_picture(i))
#

def update_winner():
    if p1r == 0 and p2r == 2:
        # player 1 winner
        winner.goto(0, 80)
    elif p1r == 2 and p2r == 0:
        winner.goto(160, 80)
    elif p1r == p2r:
        winner.goto(80, 80)
    elif p1r > p2r:
        winner.goto(0, 80)
    elif p1r < p2r:
        winner.goto(160, 80)
    else:
        winner.goto(0, 80)


def runclick(x, y):
    global p1r, p2r
    p1r = random.randint(0, 3)
    p2r = random.randint(0, 3)
    player1.shape(select_picture(p1r))
    player2.shape(select_picture(p2r))
    update_winner()


player1 = turtle.Turtle()
player1.penup()
player1.goto(0, 0)

player2 = turtle.Turtle()
player2.penup()
player2.goto(160, 0)

start = turtle.Turtle()

start.shape('start.gif')
start.penup()
start.goto(80, 0)

start.onclick(runclick)

turtle.mainloop()