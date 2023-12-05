
#---------------------WHILE -------------------------
#----------------------------------------------------
# הדפסת המספרים חד ספרתיים

# def print_numbers_till_9():


def print_numbers_till_9():
  num = 0
  while num < 10:
    print (num ,)
    num +=1

print_numbers_till_9()
    
# print_numbers_till_9()


#----------------------------------------------------
# קליטת מחרוזות עד אשר נקלוט את הטקסט
# hello

def input_hello_only():
  n = input("Please enter 'hello': ")
  while n != 'hello':
    n = input("Please enter 'hello': ")
  print ("end")

