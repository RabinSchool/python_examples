#-----------------------Lists------------------------
#----------------------------------------------------

# יצירת רשימה חדשה
lst=[]

# הוספת המספר 13 לרשימה
lst.append(13)
# הוספת טקסט לרשימה
lst.append('hello')


# בדיקה האם איבר נמצא ברשימה
value = 13
if value in lst:
  print('the value ',value,' in the list')

# הדפסת האיבר הראשון ברשימה
print(lst[0])

# פקודה המחזירה את אורך הרשימה / מספר איברים
size = len(lst)


# החזרת כמות המופעים של value ברשימה

cnt_value  = lst.count(value) 


# החזרת המציין הראשון ברשימה בו מופיע value
# אם לא קיים מחזיר הודעת שגיאה בזמן ריצה!

position =  lst.index(value) 

# בדיקה האם איבר קיים ברשימה
if item in lst: 

# החזרת רשימה ע"פ חיתוך רשימה קיימת

# start - מאיפה    

# end - עד איפה, לא כולל    

# step - בקפיצות    

sub_list = lst[ start : end : step ] 


# הוספת איבר  לסוף רשימה 

lst.append(item)


# הוספת איבר  במציין/מיקום  של הרשימה

lst.insert(pos, item) 

# מחיקת ערך מהרשימה, לפי ערך (מוחק את המופע הראשון של הערך שמועבר לפעולה). אם לא נמצא ברשימה, מחזיר שגיאה.

lst.remove(value) 


# מחיקת ערך מהרשימה, לפי מיקום (מוחק את האיבר במקום ה-אינדקס), והחזרת ערכו. אם אין מיקום כזה, מחזיר שגיאה.

# מוחק את האיבר האחרון ברשימה.

x = lst.pop(index) 

# מיון רשימה בסדר עולה (מהקטן לגדול)

lst.sort()

# מיון רשימה בסדר יורד  (מהגדול לקטן)

lst.sort(reverse=True) 


# הפיכת סדר הפריטים ברשימה
# הפיכת רשימה למחרוזת על ידי חיבור על האיברים עם תו  .
# delimiter מפריד


lst = [‘I’, ‘love’, ‘Python’]

delimiter = ‘_’

s = delimiter.join(my_list)

print (s)







#  מעבר בלולאה לפי ערך על איברי הרשימה

def print_list_items(lst):
    for item in lst:
        print(item)


print_list_items([1,2,3,5,10])

#  מעבר בלולאה לפי אינדקס על איברי הרשימה

def print_list_items_by_index(lst):
    for i in range(len(lst)):
        print(lst[i])


print_list_items_by_index([1,2,3,5,10])



# דוגמא שלמה להגדרת רשימה , הוספת איבר והדפסת כל איברי הרשימה
def show_items_in_list():
    colors = ['red', 'orange', 'yellow', 'green']
    colors.append('blue')
    for color in colors:
        print( color)
show_items_in_list()







# עוד דוגמאות ניתן למצוא בכתובת 
# https://www.w3schools.com/python/python_lists.asp

#text="hello#world"
#data = text.split('#')   #  (מחלק מחרוזת לרשימה)
#text = "@".join(data)    # (מצרף את הרשימה למחרוזת המופרדת ע"י "@")
def split_words(text):

    lst = text.split(' ') #  חלוקת מחרוזת לרשימת מילים
    print (text)
    print (lst)
    new_string = "_".join(lst)  # איסוף מילים מרשימה למחרוזתprint new_string
    print (new_string)

str = "I love programming in Python"
split_words(str)