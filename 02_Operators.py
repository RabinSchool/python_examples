
# השמה של ערך למשתנה קובעת את הטיפוס שלו.
#-------------------------------------------
x = 110

# הפקודה הבאה מגדילה את המשתנה ב-10
# לאחר הפקודה הערך יהיה 120
x = x + 10

#  השמה של טקסט למשתנה 
name = 'tomer'


# השמה מרובה למספר משתנים בשורה אחת
# הפקודה שקולה לשלושת הפקודות הבאות
# n1 =  10 
# n2 =  10.0 
# n3 =  "10"

n1, n2, n3 = 10, 10.0, "10"



num1 = 32
num2 = 9

result = num1 / num2      #   פעולת חילוק 
result = num1 // num2     #  פעולת חלוקה ועיגול למטה 
result = num1 * num2      #   פעולת כפל
result = num1 - num2      #   פעולת חיסור
result = num1 + num2      #  פעולת חיבור
result = num1 % num2      #   פעולת שארית החלוקה




#   אופרטור שארית החלוקה %
#----------------------------------------------------

print (10 % 3)   # 1
print (9 % 3)    # 0



# אופרטור %
# מציאת ספרת האחדות של מספר
# על ידי שימוש במודולו 10
#----------------------------------------------------
num = 1983
print (num % 10) # 3

# בדיקה האם מספר מתחלק במספר אחר
# בדוגמה הבאה אנו בודקים האם המספר מתחלק ב-2
num=34
if num % 2 == 0 :
  print('num divid in 2')

# חלוקה של מספרים ושימוש באופרטורים
# /   חלוקה מתמטית רגילה
# // חלוקה רגילה ועיגול למטה
#----------------------------------------------------
n1 = 5
n2 = 2

# on python version 3.x
print (n1 / 2)   # 2.5    
print (n1 // 2)  # 2






# אופרטורים לתנאים
#----------------------------------------------------
print (3==5)   # False
print (3!=5)   # True