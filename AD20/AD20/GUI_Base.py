import tkinter
import tkMessageBox
top = tkinter.Tk()
def startEngine():
    tkMessageBox.showinfo("Welcome to AutoDiff Education Mode","Please follow the instruction")

heads = tkinter.Button(top, text = "AD Calculator", command = startEngine)

heads.pack()
top.mainloop()