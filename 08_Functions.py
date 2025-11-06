#----------------------------------------------
#פעולה שאינה מחזירה ערך ואינה מקבלת פרמטר

def ex1_print_hello():
    print ('hello')

ex1_print_hello()

#----------------------------------------------
# הפעולה המקבלת פרמטר ואינה מחזיר ערך

def print_full_name(first_name,last_name):
    print (first_name,last_name)

print_full_name('Tomer','Tubi')

#----------------------------------------------
# פעולה המקבלת פרמטר ומחזירה ערך
def sum_numbers(x,y):
    return x+y

# שימו לב כי חייב להופיע משתנה שישמור את ערך החזרה של הפעולה

total = sum_numbers(32,45)


