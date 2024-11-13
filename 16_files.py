# פעולה הקוראת תוכן של קובץ שורה אחרי שורה
def reading_method1(file_name):
  file = open(file_name,"r")
  for line in file:
    print (line)
  file.close


# פעולה הקוראת תוכן של קובץ 
def reading_method2(file_name):
  file = open(file_name,"r")
  content = file.read()
  print (content)
  file.close

# פעולה הקוראת שורה מתוך קובץ 
def reading_method_recommended(file_name):
  with open(file_name,"r") as file:
    content = file.read()
    print (content)
    
# פעולה הקוראת שורה מתוך קובץ 
def reading_method3(file_name):
  with open(file_name,"r") as file:
    content = file.readline()
    print (content)


# כתיבה לסוף של קובץ 
def write_to_file(file_name):
  f = open(file_name, "a")
  f.write("write some content!")
  f.close()
  
  #open and read the file after the appending:
  f = open("demofile2.txt", "r")
  print(f.read())
