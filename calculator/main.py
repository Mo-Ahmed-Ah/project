from tkinter import *
import os

# get the file path  
my_path = os.getcwd()

# ---------------------------------------------
# functions
# ---------------------------------------------

# ---------------------------------------------
# windows

root = Tk()
root.geometry("250x350")
root.title("Calculator")
root.iconbitmap(my_path+"/calculator/assets/icon.ico")
root.configure(background="#000" , bd=0)


# create element 


root.mainloop()
# ---------------------------------------------
