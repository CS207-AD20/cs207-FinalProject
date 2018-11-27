
# import PIL.Image
# import PIL.ImageTk
import tkinter as tk


import tkinter.messagebox as tkMessageBox
top = tk.Tk()

def startEngine():
    tkMessageBox.showinfo("Welcome to AutoDiff Education Mode","Please follow the instruction")

def versionInfo():
    tkMessageBox.showinfo("Welcome to AutoDiff Education Mode","AD20 version 1.0")

button_start = tk.Button(top, text = "AD Demo", command = startEngine)

button_start.pack()

button_version = tk.Button(top, text = "Check Version", command = versionInfo)
button_version.pack()



my_canvas = tk.Canvas(top, bg = "gray", height= 250, width= 300)

main_bg = tk.PhotoImage( file = "background_3.gif")

image = my_canvas.create_image(150,105,anchor = "center",image = main_bg)
my_canvas.pack()

ask_numbers = tk.Label(top, text = "How many values:")
value0 = tk.Entry(top, bd = 1)
res = value0.get()


# ask_value = tk.Label(top, text = "Number Value:")
# value1 = tk.Entry(top, bd = 5)


ask_numbers.grid(row = 0, column =0)
value0.grid(row =0, column = 1)

# ask_value.grid(row =1, column = 0)
# value1.grid(row =1, column =1)

ask_numbers.pack(side = 'left')
value0.pack(side = 'right')
# ask_value.pack(side = 'left')
# value1.pack(side = 'right')



def get_value():
    val = value0.get()
    message = "You are going to use {} numbers.".format(val)
    tkMessageBox.showinfo("Welcome to AutoDiff Education Mode", message)

# try more buttons:
frame = tk.Frame(top)
frame.pack(side = 'bottom')
button_1 = tk.Button(frame, text = 'value') # can add command
button_1.pack(side = 'top')
button_2 = tk.Button(frame, text = 'derivative')
button_2.pack(side = 'bottom')
button_3 = tk.Button(frame, text = 'Confirm',command = get_value )
button_3.pack(side = 'top')

top.mainloop()
print("Okay, we get the value of {}".format(res))
