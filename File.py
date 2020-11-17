import cv2
import pytesseract
global ret_list
import re
import csv

def listToString(s):
    # initialize an empty string
    str1 = " "
    # return string
    return (str1.join(s))

img = cv2.imread('C:/Users/aghaq/PycharmProjects/DIP_Project/doc06082920200117125740-page-001.jpg')
#img = cv2.imread('C:/Users/aghaq/Desktop/pan-no-registration-services-1478069127-2522248.jpeg')

cv2.imshow("Image",img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh=cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

cv2.imshow('Output', thresh)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')
print(data)
new_data = ''.join([i for i in data if not i.isdigit()])
print(new_data)
f_data = re.findall(r'[^\W\d]+', new_data)
print(f_data)
new_words = []
for x in range(0, len(f_data)):
    if (len(f_data[x]) >= 3):
        new_words.append(f_data[x])
print(new_words)
finalList = []
for word in new_words:
    if word[0].isupper():
        finalList.append(word)

data = listToString(finalList)
print(data)
cv2.waitKey(0)
newRow = ['Book_name', data]
#with open('C:/Users/aghaq/Desktop/data.csv', 'a+', newline='') as write_obj:
    #csv_writer = csv.writer(write_obj)  # Create a writer object from csv module
    #csv_writer.writerow(newRow)  # Add contents of list as last row in the csv file
