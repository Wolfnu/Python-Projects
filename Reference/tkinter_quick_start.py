from tkinter import *


# functions that the buttons interact should be defined at the very top (good practice)
def click():
    # gets the text from the text entry box.
    entered_text = text_entry.get().lower().strip()
    # allows us to clear our textbox from before the first character to the end of the box
    output.delete(0.0, END)
    try:
        definition = my_comp_dictionary[entered_text]
    # if try code throws an error the except will run
    except:
        definition = "sorry there is no word like that please try again"
    output.insert(END, definition)


# exit function
def close_window():
    # this will destroy that running window (we can't see it or do anything to it), but the code will still be running.
    root.destroy()
    # this will stop the code from running and exit.
    exit()


# main
root = Tk()
root.title("CS Glossary")
root.configure(background="black")

# locate custom picture
photo1 = PhotoImage(file="earth.gif")
# add onto the screen as a grid on the right hand side (sticky= E)
Label(root, image=photo1, bg="black").grid(row=0, column=0, sticky=E)

# add a text onto the screen, if there was no sticky it would be in the middle of screen; change sticky (N,S,E,W)
Label(root, text="Enter the word you will like a definition for:", bg="black", fg="white", font="none 12 bold").grid(
    row=1, column=0, sticky=W)

# create a text input field onto the screen
text_entry = Entry(root, width=20, bg="white")
# best practice to add onto the screen in new line if we set it up as a variable; else might not work properly
text_entry.grid(row=2, column=0, sticky=W)

# we make a button that submits, the width is 6 because 6 letters in text. The command= calls a function; no '()'.
Button(root, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky=W)

# second text added onto the screen
Label(root, text="\nDefinition:", bg="black", fg="white", font="none 12 bold").grid(row=4, column=0, sticky=W)

# makes a textbox
output = Text(root, width=75, height=6, wrap=WORD, background="white")
# columnspan allows you to use more than one column (will not increase the size of the column but uses another column)
output.grid(row=5, column=0, columnspan=2, sticky=W)

# holds the definition to the user's dictionary search
my_comp_dictionary = {"algorithm": "step by step instructions to complete a task",
                      "bug": "piece of program that causes a program to fail",
                      "python": "a programming language that was used to make this program"}

# final label
Label(root, text="click to exit: ", bg="black", fg="white", font="none 12 bold").grid(row=6, column=0, sticky=W)

Button(root, text="Exit", width=14, command=close_window).grid(row=7, column=0, sticky=E)

# end
root.mainloop()
