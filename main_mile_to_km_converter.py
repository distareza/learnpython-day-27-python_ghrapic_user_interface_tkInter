import tkinter.messagebox
from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=640, height=480)
window.config(padx=200, pady=150)

Label(text=" ").grid(row=0, column=0, columnspan=3)

entry_miles = Entry(width=10, justify="right")
entry_miles.grid(row=0, column=1)
Label(text="Miles").grid(row=0, column=2)

Label(text="is equal to").grid(row=1, column=0)
label_result = Label(text="0", width=10, anchor="e", justify="right")
label_result.grid(row=1, column=1)
Label(text="KM").grid(row=1, column=2)

def calculate() :
    try :
        mile_input = float(entry_miles.get())
        km_output = mile_input * 1.609
        label_result["text"] = "{:,.2f}".format(km_output)
    except Exception as ex:
        tkinter.messagebox.showerror(message=f"Error {ex}")

button = Button(text="calculate",command=calculate)
button.grid(row=2, column=1)

window.mainloop()