
# import PIL.Image
# import PIL.ImageTk


import tkinter as tk
from tkinter import messagebox
top = tk.Tk()

###Basic setup============================
top.title("AutoDiff Calculator")
top.geometry("500x500")
def startEngine():
    text = "Please press the function button to enter the function you want to calculate, this calculator allows 1 or 2 variables"
    messagebox.showinfo("Welcome to AutoDiff Education Mode",text)

def versionInfo():
    messagebox.showinfo("Welcome to AutoDiff Education Mode","AD20 version 1.0")

button_start = tk.Button(top, text = "Instruction", command = startEngine)

button_start.pack()

button_version = tk.Button(top, text = "Check Version", command = versionInfo)
button_version.pack()

my_canvas = tk.Canvas(top, bg = "gray", height= 120, width= 400)

#main_bg = tk.PhotoImage( file = "background_3.gif")

#image = my_canvas.create_image(160,60,anchor = "center",image = main_bg)
my_canvas.pack()
###=========


ask_numbers = tk.Label(top, text = "How many values:")
value0 = tk.Entry(top, bd = 1)
res = value0.get()


# ask_value = tk.Label(top, text = "Number Value:")
# value1 = tk.Entry(top, bd = 5)


# ask_numbers.grid(row = 0, column =0)
# value0.grid(row =0, column = 1)

# ask_value.grid(row =1, column = 0)
# value1.grid(row =1, column =1)

ask_numbers.pack(side = 'left')
# value0.pack(side = 'right')
# ask_value.pack(side = 'left')
# value1.pack(side = 'right')



def get_value():
    val = value0.get()
    message = "You are going to use {} numbers.".format(val)
    messagebox.showinfo("Welcome to AutoDiff Education Mode", message)
def calc():
    messagebox.showinfo("This is a function", "X + X is 2X")
# try more buttons:
frame = tk.Frame(top)
frame.pack(side = 'left')
button_add = tk.Button(frame, text = '+', command = calc) # can add command
button_add.pack(side = 'top')
button_2 = tk.Button(frame, text = 'derivative')
# button_2.pack(side = 'bottom')
button_3 = tk.Button(frame, text = 'Confirm',command = get_value )
# button_3.pack(side = 'top')

top.mainloop()
print("Okay, we get the value of {}".format(res))

