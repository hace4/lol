
from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("Shmelkov get 5")
root.geometry("250x200")
 
languages = ["Python", "C#", "Java", "JavaScript"]

languages_var = StringVar(value=languages[0])   
 
label = ttk.Label(textvariable=languages_var)
label.pack(anchor=NW, x=100, y=50)
 
combobox = ttk.Combobox(textvariable=languages_var, values=languages)
combobox.pack(anchor=NW, padx=6, pady=6)
 
print(combobox.get())
root.mainloop()