#קריאה למחלקה הגרפית
import turtle       
=
# מסך עבור צב
wn = turtle.Screen()  

# player יוצר צב ושמו 
player = turtle.Turtle()    

#                        התקדמות קדימה steps צעדים 
player.forward(steps)   

#                         התקדמות אחורה steps צעדים 
player.backward(steps) 

#                           סיבוב ימין/שמאל num מעלות 
player.right(num)     player.left(num)    

#קפיצה למיקום על המסך
player.goto(x, y)           

# קבלת ערכי מיקום הצב למשתנים
x = player.pos()[0]
y = player.pos()[1]   

# שינוי מיקום של הצב
player.setx(x)    player.sety(y)           

#עט מטה – הצב יצייר מסלול כשיבצע הוראות
player.pendown()

#עט מעלה – הצב לא יצייר מסלול כשיבצע הוראות
player.penup()

# שינוי עובי העט שאיתו מציירים
player.pensize(num)

# שינוי צבע העט שאיתו מציירים
player.pencolor('red')


#שינוי צורת הצב
player.shape("turtle")  

