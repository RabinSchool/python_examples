def reading_method1(file_name):
  file = open(file_name,"r")
  for line in file:
    print (line)
  file.close


# all file into one string
def reading_method2(file_name):
  file = open(file_name,"r")
  content = file.readline()
  print (content)
  file.close

def reading_method3(file_name):
  with open(file_name,"r") as file:
    content = file.readline()
    print (content)


# write to end of file 
def write_to_file(file_name):
  f = open(file_name, "a")
  f.write("write some content!")
  f.close()
  
  #open and read the file after the appending:
  f = open("demofile2.txt", "r")
  print(f.read())