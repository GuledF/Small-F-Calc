from tkinter import *
import os
import subprocess

root = Tk()
root.title("Guled's Future Value Calculator")
root.configure(bg="dark grey")
root.geometry("512x288")
root.resizable(width=False, height=False)

labelp = Label(root)


def calc():
    global labelp
    labelp.destroy()

    try:
        float(round(float(s.get()) * pow((float(i.get()) / 100 + 1), float(n.get())), 2))
    except ValueError:
        labelp = Label(frame1, text="only enter numbers")
        labelp.grid(row=4, column=1, sticky=W, padx=5)

    labelp = Label(frame1, text=round(float(s.get()) * pow((float(i.get()) / 100 + 1), float(n.get())), 2))
    labelp.grid(row=4, column=1, sticky=W, padx=5)

    word3 = Label(frame1, text="Future-Value is: ", bg="black", fg="white")
    word3.grid(row=4, column=0, sticky=E)


frame1 = Frame(root, padx=140, pady=70, bg="blue")
frame1.pack(padx=0, pady=0, )

word1 = Label(frame1, text="Future Value Calculator", bg="blue", fg="white", anchor="e", justify=RIGHT)
word1.grid(row=0, column=0, sticky=E)
word1 = Label(frame1, text="Enter starting payment: ", bg="black", fg="white", anchor="e", justify=RIGHT)
word1.grid(row=1, column=0, sticky=E)
# word2 = Label(frame1, text="Enter monthly payment: ", bg="black", fg="white")
# word2.grid(row=1, column=0, sticky=E)
word3 = Label(frame1, text="Enter amount of years: ", bg="black", fg="white")
word3.grid(row=2, column=0, sticky=E)
word3 = Label(frame1, text="Enter interest (whole number): ", bg="black", fg="white")
word3.grid(row=3, column=0, sticky=E)

s = Entry(frame1)
s.grid(row=1, column=1, padx=5)

# m = Entry(frame1)
# m.grid(row=1, column=1, padx=5)

n = Entry(frame1)
n.grid(row=2, column=1, padx=5)

i = Entry(frame1)
i.grid(row=3, column=1)

e1 = Label(frame1, bg="blue")
e1.grid(row=4, column=1)
e1 = Label(frame1, bg="blue")
e1.grid(row=5, column=1)

startb = Button(frame1, text="click here", bg="dark orange", fg="dark red", command=calc)
startb.grid(row=6, column=1)

root.mainloop()
