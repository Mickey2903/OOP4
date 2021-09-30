import string 
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

#window initialisation
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

#combobox initialisation
combo = Combobox(window, state="readonly")
combo['values']= ("Celsius to Fahrenheit","Fahrenheit to Celsius","Miles to Kilometers","Kilometers to Miles")
combo.current(2)
combo.grid(column=0, row=0)

#output label initialisation
lbl = Label(window, text="")
lbl.grid(column=2, row=2)

#input entry initialisation
txt = Entry(window,width=10)
txt.grid(column=0, row=2)

#button function
def clicked():

    #read input
    number1 = txt.get()

    #test for float
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
        lbl.configure(text= round(answer,2))

    except:
        #error handler
        messagebox.showinfo('Conversion Fault', 'The input may only contain numbers or digits')

#button initialisation   
btn = Button(window,text='Convert', command=clicked)
btn.grid(column=1,row=2)

#window update
window.mainloop()

 