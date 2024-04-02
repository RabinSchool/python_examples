# להלן קישור אשר מכיל דוגמאות קוד רבות בנושא תמונות
# https://realpython.com/image-processing-with-the-python-pillow-library/

from PIL import Image,ImageEnhance
import requests

# הצגת תמונה מכתובת אינטרנט
url=r'https://i.pinimg.com/474x/66/dd/c2/66ddc2d630d4d6cf31a92601fd1fa0e5.jpg'
img = Image.open(requests.get(url, stream=True).raw)
display(img)  # im.show() במחשב מקומי יש להשתמש ב- 


# מעבר על כל הפיקסלים בתמונה
def read_and_change_image_pixel(img):
    pix = img.load() # קבלת כל הנקודות של המסך 
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            #  הכנסת ערכי אדום ירוק וכחול למשתנים 
            r, g, b = pix[x, y] 
            # הכנסת ערכים חדשים לצבעים לנקודה ספציפית 
            pix[x, y]=(r,g,b) # עדכון הערכים של  האדום  , ירוד וכחול של כל נקודה
          
    display(img)  # הצגת התמונה


# שינוי מאפיינים של תמונה

im_output = ImageEnhance.Contrast(img).enhance(factor) #  factor > 0 
im_output = ImageEnhance.Brightness(img).enhance(factor) #  factor > 0 
im_output = ImageEnhance.Sharpness(img).enhance(factor) #  factor > 0 
im_output = ImageEnhance.Color(img).enhance(factor) #  factor > 0 
