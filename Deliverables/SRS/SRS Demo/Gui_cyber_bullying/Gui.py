import csv
from tkinter import *
import tkinter.ttk as ttk

import nltk

list_of_bad_words=[]
with open("bad-words.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        list_of_bad_words.append(row[0])

frame = Tk()
frame.title("Demo")
frame.configure(background='white')
frame.geometry('{}x{}'.format(480,200))
label1 = Label(frame,text="Cyberbullying Detection Demo",bg="white")
label1.pack()
e = Entry(frame,width=50)
e.pack(side=BOTTOM)
e.focus_set()
def callback():
    var = "no cyberbullying detected"
    stat = e.get()
    stat1 = nltk.word_tokenize(stat)
    for x in stat1:
        for y in list_of_bad_words:
            if(x==y):
                var="cyberbullying detected"

    label = Label(frame, text=var, bg="white")
    label.pack(side=BOTTOM)


b = Button(frame, text="Check", width=10,fg="blue", command=callback,bg="white")
b.pack(side=BOTTOM)

mainloop()

