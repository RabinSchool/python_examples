import turtle    

wn = turtle.Screen()
pen = turtle.Turtle()   



# pen.forward(100)      # ציור קו באורך 100
# pen.right(90)         #  פנה ימינה במעלות המצוינות
# pen.left(angle)       #  פנה שמאלה במעלות המצוינות
# pen.heading()         # החזר את כיוון העט
# pen.setheading(90)    # פנה לכיוון 
# pen.setpos(50,50)     #  העבר את העט לנקודה 50 , 50
# pen.goto(0,0)         #  הזז את העט למרכז המסך
# pen.setx(80)          #  שנה את המיקום בציר איקס להיות 80   
# pen.sety(50)          # 50 שנה את המיקום בציר איקס להיות         
# pen.color("blue")     # שנה את צבע העט לצבע כחול       
# pen.pensize(3)        #  שנה את עובי העט לשלוש נקודות
# pen.pendown()         # הנח את העט הל המסך והתחל לצייר
# pen.down()            #  הנח את העט הל המסך והתחל לצייר
# pen.penup()           #  הרם את העט מהמסך והפסק לצייר
# pen.fillcolor('pink') #  הגדר צבע מילוי
# pen.begin_fill()      #  הגדר טווח מילוי
# pen.end_fill()        #  סיים טווח מילוי צורה
# pen.circle(70)        #  צייר עיגול ברדיוס 70
# pen.back(100)         #  זוז לאחור 100 צעדים











#---------------------------------------------------------
# פעולה לציור ריבוע בצבעים שונים
import turtle

wn=turtle.Screen()
pen=turtle.Turtle()

pen.pendown()
def draw_square():
  colors = ['red', 'orange', 'yellow', 'green']
  for i in range(4):
    pen.pencolor(colors[i])
    pen.forward(100)
    pen.left(90)

draw_square()


