
# https://www.w3schools.com/python/python_strings.asp


text = "Happy Day" # השמה של טקסט למשתנה


print(text[0]) # הדפסת התו הראשון 


print(text[-1]) # הדפסת התו האחרון


# בדיקה האם מחרוזת נמצא במחרוזת כלשהי
if 'ab' in text:
  print('ab is in the string')

#   הפעולה מחזירה את הקוד המספרי המייצג את האות שבסוגריים
code = ord('a')   # המספר 97 יודפס
# מציאת התו המיוצג על ידי המספר שמועבר כפרמטר  והכנסתו למשתנה חדש
letter = chr(97)   # a יודפס התו
  
# ספירה כמה פעמים מחרוזת או אות נמצאים במחרוזת
cnt = text.count('a') # במקרה זה האות נמצאת פעמיים במחרוזת
  
# חיתוך מחרוזות

# חיתוך המחרוזת החל מהתו במקום השני עד המקום הרביעי לא כולל הרביעי
sub1 = text[1:4]  # app
# חיתוך המחרוזת החל מהתו במקום הראשון עד המקום השני לא כולל השני
sub2 = text[0:1]  # H
#  חיתוך המחרוזת החל מתחילת המחרוזת עד סוף המחרוזת בקפיצות של שניי תוים כל פעם
sub3 = text[::2]  # HpyDy
# היפוך מחרוזת
sub4 = text[::-1]  # yaD yppaH


# חיבור מחרוזות
sub6 = "abc" + "def"
# או
sub5 = sub1 + sub2

# הדפסה למסך באותה שורה
print(sub1, sub2)
# הדפסה למסך בשורות נפרדות
print(sub3)
print(sub4)
print(sub5)


new_text = text[::-1] #  הפיכת סדר אותיות במחרוזת והכנסת התוצאה למשתנה חדש

new_text =len(text) #  אורך המחרוזת והכנסת התוצאה למשתנה חדש

new_text =text.lower() #  המחרוזת באותיות קטנות  והכנסת התוצאה למשתנה חדש

new_text =text.upper() #  המחרוזת באותיות גדולות והכנסת התוצאה למשתנה חדש

# הפקודה הבאה תחליף את כל הפעמים של מחרוזת אחת במחרוזת השנייה
new_str=sub6.replace('ab','##')

#------------------LOOP-STRINGS----------------------
#----------------------------------------------------

# מעבר בלולאה לפי ערך
#  מחרוזת עם רווח בין כל אות

  for letter in str:
      print(letter, end=' ')

    

#----------------------------------------------------
# מעבר בלולאה לפי אינדקס 
#  שזה מעבר על מספרים שמייצגים את מיקום התו הנוכחי במחרוזת
# הדפסת מחרוזת עם רווח בין כל אות

  #  len הפעולה 
  # מחזירה את מספר התוים במחרוזת
  for num in range(len(str)):
      print(str[num], end=' ')



#----------------------------------------------------

# הדפסת כל אות שלישית במחרוזת 
def loop_string_every_third_letter(str):
    for ch in str[::3]:
        print(ch, end=' ')


loop_string_every_third_letter('abcdefghijk')


#----------------------------------------------------
# חיפוש האם תו מסוים נמצא בתוך מחרוזת המתקבלת כפרמטר לפעולה
# במקרה שלנו נחפש את התו a
def search_for_char(text):
    flag = False
    for ch in text:
        if ch == 'a':
            flag = True
    if flag == True:
        print('a character found in string')
    else:
        print('a character not found in string')


search_for_char('Hello world')
