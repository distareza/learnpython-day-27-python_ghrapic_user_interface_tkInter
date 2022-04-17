https://docs.python.org/3/library/tkinter.html

The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit. Both Tk and tkinter are available on most Unix platforms, including macOS, as well as on Windows systems.

This framework provides Python users with a simple way to create GUI elements using the widgets found in the Tk toolkit. Tk widgets can be used to construct buttons, menus, data fields, etc. in a Python application

syntax:

    import tkinter
    
    window = tkinter.Tk()
    window.title("Python GUI Program")
    window.minsize(width=640, height=480)
    
    window.mainloop()