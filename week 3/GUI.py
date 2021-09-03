import string 

from tkinter import *

from tkinter import messagebox

from tkinter.ttk import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

combo = Combobox(window, state="readonly")

combo['values']= ("Celsius to Fahrenheit","Fahrenheit to Celsius","Miles to Kilometers","Kilometers to Miles")

combo.current(0)

combo.grid(column=0, row=0)

def check(value): 
    for letter in value: 
        if letter not in (string.digits + "."): 
            return False
    return True

lbl = Label(window, text="")

lbl.grid(column=2, row=2)

txt = Entry(window,width=10)

txt.grid(column=0, row=2)

def clicked():
    number1 = txt.get()
    try:
        #string to float
        number1 = float(number1)
        
        # conversion
        if combo.get() =="Celsius to Fahrenheit":
            answer = number1 *1.8 + 32
        elif combo.get() =="Fahrenheit to Celsius":
            answer = (number1 - 32)/1.8
        elif combo.get() =="Miles to Kilometers":
            answer = number1 * 1.609344
        elif combo.get() =="Kilometers to Miles":
            answer = number1 / 1.609344

        #output
        lbl.configure(text= answer)
    except:
        #error handler
        messagebox.showinfo('Conversion Fault', 'The input may only contain numbers or digits')

    
    
btn = Button(window,text='Convert', command=clicked)

btn.grid(column=1,row=2)



window.mainloop()

 