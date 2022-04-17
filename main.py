"""
    Introduction to python GUI program using tkInter
    https://docs.python.org/3/library/tkinter.html

    http://tcl.tk/man/tcl8.6/TkCmd/pack.htm
    http://tcl.tk/man/tcl8.6/TkCmd/entry.htm
"""
import tkinter

window = tkinter.Tk()
window.title("Python GUI Program")
window.minsize(width=640, height=480)

# Label
my_label = tkinter.Label(text="Label", font=("Arial", 24, "bold italic"))
my_label.pack() # packed to windows layout

my_label["text"] = "New Text"
my_label.config(text="Update Text")

# Button
button = tkinter.Button(text = "click me", font=("Times New Roman", 12, "normal"))
button.pack()
ntimes = 0
def button_clicked():
    global ntimes
    ntimes+=1
    my_label.config(text=f"I got clicked {ntimes} times")

button.config(command=button_clicked)

#Entry
input = tkinter.Entry(width=30)
input.place(x=250, y=103)

button2 = tkinter.Button(text="Change the Label")
def change_label():
    new_label = input.get()
    my_label.config(text=new_label)
button2.config(command=change_label)
button2.place(x= 100, y=100)



window.mainloop()