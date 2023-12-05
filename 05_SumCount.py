# תכנית אשר סוכמת את כל המספרים מ-0 עד 9 כולל

def sum_numbers():
  sum = 0
  for i in range(0,10):
    sum = sum + i
  
  print('the sum of numbers 0 till 9 is :',sum)




# תכנית אשר סופרת כמה תלמידים הם מעל גיל 13

def count_studuents():
  cnt = 0
  for i in range(0,100):
    age = int(input('please enter your age'))
    if age >13 :
      cnt = cnt + 1 
  
  print('number of students with age above 13 is :',cnt)
  
