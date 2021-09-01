from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

combo = Combobox(window,state='readonly')

combo['values']= ("Celsius to Fahrenheit", "Fahrenheit to Celsius", "Miles to Kilometers", "Kilometers to Miles")

combo.current(0)

combo.grid(column=0, row=0)

txt = Entry(window,width=10)

txt.grid(column=0, row=1)

window.mainloop()