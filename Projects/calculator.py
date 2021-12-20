from tkinter import *

# Button Commands
num = 0
temp = 0
final = 0
method = " "


def b7():
    global num
    text_input.insert(END, 7)
    num = int(text_input.get())


def b8():
    global num
    text_input.insert(END, 8)
    num = int(text_input.get())


def b9():
    global num
    text_input.insert(END, 9)
    num = int(text_input.get())


def b4():
    global num
    text_input.insert(END, 4)
    num = int(text_input.get())


def b5():
    global num
    text_input.insert(END, 5)
    num = int(text_input.get())


def b6():
    global num
    text_input.insert(END, 6)
    num = int(text_input.get())


def b3():
    global num
    text_input.insert(END, 3)
    num = int(text_input.get())


def b2():
    global num
    text_input.insert(END, 2)
    num = int(text_input.get())


def b1():
    global num
    text_input.insert(END, 1)
    num = int(text_input.get())


def multiply():
    global num, temp, final, method
    final = text_input.get()
    temp = int(final)
    num = 0
    text_input.delete(0, END)
    method = "multiply"


def subtract():
    global num, temp, final, method
    final = text_input.get()
    temp = int(final)
    num = 0
    text_input.delete(0, END)
    method = "subtract"


def add():
    global num, temp, final, method
    final = text_input.get()
    temp = int(final)
    num = 0
    text_input.delete(0, END)
    method = "add"


def clear():
    global num, final, temp, method
    num = 0
    temp = 0
    final = 0
    method = " "
    text_input.delete(0, END)


def equal():
    text_input.delete(0, END)
    global num, final, temp, method
    if method == "multiply":
        final = (temp * num)
    elif method == "subtract":
        final = temp - num
    elif method == "add":
        final = temp + num
    text_input.insert(END, final)


root = Tk()
root.title("Samyam's Calculator")

text_input = Entry(root, width=30)
text_input.grid(row=0, column=0, columnspan=3, sticky=W)

# Buttons
# first row
Button(root, text="7", font="none 14 bold", width=5, height=2, command=b7).grid(row=1, column=0)
Button(root, text="8", font="none 14 bold", width=5, height=2, command=b8).grid(row=1, column=1)
Button(root, text="9", font="none 14 bold", width=5, height=2, command=b9).grid(row=1, column=2)
Button(root, text="X", font="none 14 bold", width=5, height=2, command=multiply).grid(row=1, column=3)

# second row
Button(root, text="4", font="none 14 bold", width=5, height=2, command=b4).grid(row=2, column=0)
Button(root, text="5", font="none 14 bold", width=5, height=2, command=b5).grid(row=2, column=1)
Button(root, text="6", font="none 14 bold", width=5, height=2, command=b6).grid(row=2, column=2)
Button(root, text="-", font="none 14 bold", width=5, height=2, command=subtract).grid(row=2, column=3)

# third row
Button(root, text="1", font="none 14 bold", width=5, height=2, command=b1).grid(row=3, column=0)
Button(root, text="2", font="none 14 bold", width=5, height=2, command=b2).grid(row=3, column=1)
Button(root, text="3", font="none 14 bold", width=5, height=2, command=b3).grid(row=3, column=2)
Button(root, text="+", font="none 14 bold", width=5, height=2, command=add).grid(row=3, column=3)

# fourth row
Button(root, text="0", font="none 14 bold", width=5, height=2, command=equal).grid(row=4, column=0)
Button(root, text="CE", font="none 14 bold", width=5, height=2, command=clear).grid(row=4, column=1)
Button(root, text="=", font="none 14 bold", width=11, height=2, command=equal).grid(row=4, column=2, columnspan=2, sticky=W)

root.mainloop()
