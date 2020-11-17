import tkinter as tk
import requests
from bs4 import BeautifulSoup
from bookfinder import caputer_image,boundingBox
from tkinter import filedialog

from Processing import get_grayscale,remove_noise
from Processing import deskew,thresholding
import numpy as np
# This import statement is to disable urllib3 'insecure platform warning' exception.
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import cv2
import pytesseract
global ret_list
import webbrowser
import re
# <==========================Input From user Function===============================>
def get_results(data):

    #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #img = cv2.imread('input4.jpeg')
    #text=pytesseract.image_to_string(img)
    #print(text)
    #entry11= ""
    #for i in text:
        #entry11+=i+' '
    #print(entry11)
    input_name = data
    print("\n")
    global ret_list
    global ret_url
    ret_list, ret_url = search(input_name)
    print("\n")
    #print(ret_list)
    tempstring=""
    i=1
    for book in ret_list:
        tempstring+='('+str(i)+') '+book+"\n"
        i+=1
    label['text']=tempstring



# <==========================SearchFunction===============================>
def search(book_name):

    headers = {'user-agent':"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}
    para = {"q":book_name,"search_type":"books"}
    r =requests.get("https://www.goodreads.com/search?utf8=?",params=para,headers=headers)

    data = r.text
    soup = BeautifulSoup(data,"html.parser")

    search_result=soup.find_all("a",{"class":"bookTitle"})
    search_list = []
    search_url = []

    for i in search_result:
        temp_title = i.span.text
        search_list.append(temp_title)
        search_url.append(i.get("href"))

        print (str(search_result.index(i)+1)+ " " + temp_title)

    return search_list,search_url

# <==========================View Online Function===============================>

def view_online(entry):
    #option_sel = input("Enter the your selection: ")
    option_sel=entry
    # print option_sel
    global ret_url
    global ret_list
    print(ret_list)
    book_sel = ret_list[int(option_sel) - 1]
    sel_bookurl = "https://www.goodreads.com" + ret_url[int(option_sel) - 1]

    print(book_sel, sel_bookurl)
    webbrowser.open(sel_bookurl, new=2)
    print("---------------------------------------------------")


def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))


def photo2text(in_image):

    image=cv2.resize(in_image, (300,300), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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
    data=correction(data)
    get_results(data)

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    file_directory="'" + filename +"'"
    load_image=cv2.imread(filename)
    print(file_directory)
    #cv2.imshow('Loaded Image',load_image)
    preview(filename)
def preview(img_loc):
    img = cv2.imread(img_loc)
    ##image = cv2.imread('C:/Users/aghaq/PycharmProjects/DIP_Project/input4.jpeg')
    scale_percent = 60  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    frame = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    retruned=boundingBox(frame)
    photo2text(img)
    cv2.imshow("Image",img)


#<==================================GUI CREATION================================>
HEIGHT = 600
WIDTH = 800

root = tk.Tk()
# adding title to the main window
root.title("Book Finder")
# Change the main windows icon
root.iconbitmap(r'icon.ico')
#GUI Screen Creator
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
#GUI BACKGROUND IMAGE CREATOR
background_image = tk.PhotoImage(file='bookshelves.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relx=0,rely=0,relwidth=1, relheight=1)
#INPUT FRAME FORMATION
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.9, relwidth=0.75, relheight=0.1,anchor='n')
def clear_search(event):
    entry1.delete(0, tk.END)
entry1 = tk.Entry(frame, font=40,fg='grey')
entry1.insert(0, "Enter your choice from above list:")
entry1.place(relwidth=0.65, relheight=1)
entry1.bind("<Button-1>", clear_search)

#Enter Button
button= tk.Button(frame, text="View Online", font=40, command=lambda: view_online(entry1.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)
#INPUT FRAME 2 FORMATION
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.6, rely=0.1, relwidth=0.75, relheight=0.09, anchor='n')
def clear_searchsecond(event):
    entry.delete(0, tk.END)
entry = tk.Entry(frame, font=40,fg='grey')
entry.insert(0, "Enter book name")
entry.place(relwidth=0.65, relheight=1)
entry.bind("<Button-1>", clear_searchsecond)
#View Online  Button
button= tk.Button(frame, text="Analyze", font=40, command=lambda: get_results(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)
#Output Display Area

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

#photo Capture  Button

button= tk.Button(background_label, text="Capture", font=40, command=lambda: caputer_image())
button.place(relx=0.1, rely=0.07,relheight=0.05, relwidth=0.15,anchor='n')
#photo Preview  Button
button= tk.Button(background_label, text="Load Image", font=40, command=UploadAction)
button.place(relx=0.1, rely=0.12,relheight=0.05, relwidth=0.15,anchor='n')
cap_image='C:/Users/aghaq/PycharmProjects/DIP_Project/filename.jpg'
button= tk.Button(background_label, text="Preview", font=40, command=lambda: preview(cap_image))
button.place(relx=0.1, rely=0.17,relheight=0.05, relwidth=0.15,anchor='n')

root.mainloop()