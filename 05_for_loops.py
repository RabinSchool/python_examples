#-----------------------Loops------------------------
#----------------------------------------------------
#----------------------------------------------------
# הדפסת המספרים מאחת עד עשר
# שימו לב : כל מספר יופיע בשורה נפרדת 
def loop_10_times_new_line():
  for i in range(10):
    print (i)
    
loop_10_times_new_line()


# הדפסת כל המספרים בטווח שבין 3 ל – 51 בקפיצות של 5:
# כל מספר יופיע בשורה חדשה

def print_numbers():
  
  for number in range(3, 51, 5):
    print (number)
    
print_numbers()

#----------------------------------------------------
# הדפסת המספרים מאחת עד עשר
# שימו לב : כל המספרים יופיעו באותה שורה עם רווחים בינהם
def loop_10_times():
  for i in range(10):
    print (i,end=' ')
loop_10_times()


#----------------------------------------------------
# הדפסת X
# מספרים עם רווח בין כל מספר למשנהו
def loop_x_times(x):
  for i in range(x):
    print (i,end=' ')
loop_x_times()




#----------------------------------------------------
# פעולה לסכימת כל המספרים הזוגיים עד מספר שנקלט מהמשתמש

def sum_all_even_numbers():
  num = int (input ("Enter number: "))
  count = 1
  sum = 0
  while count < num+1:
    if count% 2 == 0:
      sum += count
    count += 1
  print ("the sum of the even numbers is:", sum)
    


#------------------LOOP-STRINGS----------------------
#----------------------------------------------------

# הדפסת מחרוזת עם רווח בין כל אות
def print_text_with_space(str):
  for letter in str:
    print (letter,end=' ')
print_text_with_space('hello')

#----------------------------------------------------
# הדפסת מחרוזת עם רווח בין כל אות
def print_text_with_space2(str):
  # הפעולה len
  # מחזירה את מספר התוים במחרוזת
  for num in range (len(str)):
    print (str[num],end=' ')

print_text_with_space2('hello')

#----------------------------------------------------

def loop_string_every_third_letter(str):
  for ch in str[::3]:
    print (ch,end=' ')
loop_string_every_third_letter('abcdefghijk')


#----------------------------------------------------
# חיפוש האם תו מסוים נמצא בתוך מחרוזת המתקבלת כפרמטר לפעולה
# במקרה שלנו נחפש את התו a   
def search_for_char(text):
  flag=False
  for ch in text:
    if ch=='a':
      flag=True
  if flag==True:
    print ('a character found in string')
  else:
    print ('a character not found in string')
search_for_char('Hello world')
