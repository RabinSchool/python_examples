#-----------------------Lists------------------------
#----------------------------------------------------


lst=[]                        # יצירת רשימה חדשה
lst.append(13)                # הוספת המספר 13 לרשימה
lst.append('hello')           # הוספת טקסט לרשימה

if value in lst:              # בדיקה האם איבר נמצא ברשימה

print(lst[0])                 # הדפסת האיבר הראשון ברשימה
size = len(lst)               # פקודה המחזירה את אורך הרשימה / מספר איברים
cnt_value  = lst.count(value) # החזרת כמות המופעים של value ברשימה
position =  lst.index(value)  # החזרת המיקום הראשון ברשימה בו מופיע הערך , אם לא קיים מוחזרת שגיאה

# החזרת רשימה ע"פ חיתוך רשימה קיימת
# start - מאיפה    
# end - עד איפה, לא כולל    
# step - בקפיצות    
sub_list = lst[ start : end : step ]  


lst.insert(pos, item)  # הוספת איבר  במציין/מיקום  של הרשימה
lst.remove(value)      # מחיקת ערך מהרשימה, לפי ערך (מוחק את המופע הראשון של הערך שמועבר לפעולה). אם לא נמצא ברשימה, מחזיר שגיאה.
x = lst.pop(index)     # מוחק את האיבר האחרון ברשימה.
lst.sort()             # מיון רשימה בסדר עולה (מהקטן לגדול)
lst.sort(reverse=True) # מיון רשימה בסדר יורד  (מהגדול לקטן)
s = '_'.join(my_list)  # הפיכת איברי רשימה למחרוזת כאשר בין כל איבר במחרוזת יופיע התו המצוין
lst = text.split(' ')  #  הפיכת מחרוזת לרשימה של איברים כך שכל איבר נקבע לפי התו המפריד שמועבר כפרמטר 
new_lst= lst.extends([2,3,4])   # חיבור בין שתי רשימות
                    





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
