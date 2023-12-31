# קריאה לספריה של תור
import queue
# יצירת-תור-ריק
q = queue.Queue()
# הכנסה-לתור
q.put(ערך_שנרצה_להכניס_לתור)
# הוצאה-מהתור
q.get()
# בדיקה-האם-התור-ריק?
if q.empty():
  print('empty queue')

#   מעבר על האיברים בתור ללא שמירת האיברים בתור
# יש לשים לב שבסוף הריצה התור יהיה ריק
while not q.empty():
  item = q.get()
  print(item)


#  מעבר על האיברים בתור ושמירת האיברים
# יש לשים לב שאנו שומרים את האיברים שמחקנו 

length = q.qsize()
for i in range(length):
  item = q.get()   # נוציא את האיבר בראש התור
  print(item)      # נדפיס את האיבר 
  q.put(item)      # נחזיר אותו לסוף התור
    

