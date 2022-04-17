from tkinter import *

window = Tk()
window.title("Python GUI Program")
window.minsize(width=640, height=480)
window.config(padx=200, pady=150)

my_label = Label(text="Label", font=("Arial", 24, "bold italic"))
my_label.grid(row=0, column=0, columnspan=3)

Label(text="Enter a Value :").grid(row=1, column=0)
my_entry = Entry(width="10")
my_entry.grid(row=1, column=1)

button = Button(text="Submit")
button.grid(row=1, column=2)

def change_label():
    my_label.config(text=my_entry.get())
    
button.config(command=change_label)

window.mainloop()