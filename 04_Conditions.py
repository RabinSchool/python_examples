# example1
# בדיקה האם שני מספרים שווים זה לזה
def condition1():
  n1 = int(input('enter first number'))
  n2 = int(input('enter second number'))
  if n1 == n2:
      print ("=")
  else:
      print ("!=")
condition1()
	
# example2
# בדיקה האם מחרוזת שווה למחרוזת אחרת
def condition2():
  word = input('enter text')
  if word == 'hi':
      print ("hi")
  else: 
      print ("not hi")
condition2()

# example3
# בדיקה האם מספר הינו חיובי או שלילי או אפס
def condition3():

  num = int (input ("Please enter number"))
  if num > 0:
      print ("+")
  elif num < 0:
      print ("-")
  else:
      print ("0")
condition3()


# example4
# בדיקה האם מספר נמצא בטווח מספרים
def condition4():	
  num = int (input ("Enter number")) 
  if num < 10 and num > (-10):
      print ("Single digit number")
  else:
      print ("Not a single digit number")
condition4()
