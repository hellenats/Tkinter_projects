from tkinter import *

def click(item):
    global expression
    expression = expression + str(item)
    equation_text.set(expression)

def clear():
    global expression
    expression = ""
    equation_text.set("")

def equal():

    global expression
    try:
        total = str(eval(expression))

        equation_text.set(total)

        expression = total

    except SyntaxError:

        equation_text.set("syntax error")

        expression = ""

    except ZeroDivisionError:

        equation_text.set("arithmetic error")

        expression = ""

window = Tk()
window.title('Calculator')  #gives the name to the file
window.geometry('350x330')  #sets the size of the window
window.resizable(0, 0) #prevents the root window from being resized

expression = ""
equation_text = StringVar()  #'StringVar()' :It is used to get the instance of input field

label = Label(window, font=('Garamond', 20, 'bold'), textvariable=equation_text, width=22, height=2, fg='#420F2A',
              bg='white')
label.pack()

buton_frame = Frame(window)
buton_frame.pack()

# creating the first row
clear_btn = Button(buton_frame, text='C', fg='#36005B', activeforeground='#420F2A', width=15, height=1,bg='#E7BBE7',
                   font=('Garamond',20), command=clear)
clear_btn.grid(row=0, column=0, columnspan=3, sticky="nsew")

divide_btn = Button(buton_frame, text='/', fg='#36005B', activeforeground='#420F2A', width=6, height=1,bg='#E7BBE7',
                   font=('Garamond',20), command=lambda: click('/'))
divide_btn.grid(row=0, column=3, sticky="nsew")

button7 = Button(buton_frame, text='7', fg='#36005B', activeforeground='#420F2A', width=5, height=1,bg='#E7BBE7',
                   font=('Garamond',20), command=lambda: click('7'))
button7.grid(row=1, column=0, sticky="nsew")

button8 = Button(buton_frame, text='8', fg='#36005B', activeforeground='#420F2A', width=5, height=1,bg='#E7BBE7',
                   font=('Garamond',20), command=lambda: click('8'))
button8.grid(row=1, column=1, sticky="nsew")

button9 = Button(buton_frame, text='9', fg='#36005B', activeforeground='#420F2A', width=5, height=1,bg='#E7BBE7',
                   font=('Garamond',20), command=lambda: click('9'))
button9.grid(row=1, column=2, sticky="nsew")

multiply = Button(buton_frame, text='*', fg='#36005B', activeforeground='#420F2A', width=6, height=1,
                   bg='#E7BBE7', font=('Garamond',20), command=lambda: click('*'))
multiply.grid(row=1, column=3, sticky="nsew")

# creating the second row

button4 = Button(buton_frame, text='4', fg='#36005B', activeforeground='#420F2A', width=5, height=1,
                   bg='#E7BBE7', font=('Garamond',20), command=lambda: click('4'))
button4.grid(row=2, column=0, sticky="nsew")

button5 = Button(buton_frame, text='5', fg='#36005B', activeforeground='#420F2A', width=5, height=1,
                   bg='#E7BBE7', font=('Garamond',20), command=lambda: click('5'))
button5.grid(row=2, column=1, sticky="nsew")

button6 = Button(buton_frame, text='6', fg='#36005B', activeforeground='#420F2A', width=5, height=1,
                   bg='#E7BBE7', font=('Garamond',20), command=lambda: click('6'))
button6.grid(row=2, column=2, sticky="nsew")

subtract = Button(buton_frame, text='-', fg='#36005B', activeforeground='#420F2A', width=6, height=1,
                   bg='#E7BBE7', font=('Garamond',20), command=lambda: click('-'))
subtract.grid(row=2, column=3, sticky="nsew")

#third row

button1= Button(buton_frame, text='1', fg='#36005B', activeforeground='#420F2A', width=5, height=1,
                   bg='#E7BBE7', font=('Garamond',20), command=lambda: click('1'))
button1.grid(row=3, column=0, sticky="nsew")

button2 = Button(buton_frame, text='2', fg='#36005B', activeforeground='#420F2A', width=5, height=1,
                   bg='#E7BBE7', font=('Garamond',20), command=lambda: click('2'))
button2.grid(row=3, column=1, sticky="nsew")

button3 = Button(buton_frame, text='3', fg='#36005B', activeforeground='#420F2A', width=5, height=1,
                   bg='#E7BBE7', font=('Garamond',20), command=lambda: click('3'))
button3.grid(row=3, column=2, sticky="nsew")

plus = Button(buton_frame, text='+', fg='#36005B', activeforeground='#420F2A', width=5, height=1,
                   bg='#E7BBE7', font=('Garamond',20), command=lambda: click('+'))
plus.grid(row=3, column=3, sticky="nsew")

#forth row
button0= Button(buton_frame, text='0', fg='#36005B', activeforeground='#420F2A', width=5, height=1,
                   bg='#E7BBE7', font=('Garamond',20), command=lambda: click('0'))
button0.grid(row=4, column=0,columnspan=2, sticky="nsew")

dot= Button(buton_frame, text='.', fg='#36005B', activeforeground='#420F2A', width=5, height=1,
                   bg='#E7BBE7', font=('Garamond',20), command=lambda: click('.'))
dot.grid(row=4, column=2, sticky="nsew")

equal= Button(buton_frame, text='=', fg='#36005B', activeforeground='#420F2A', width=5, height=1,
                   bg='#E7BBE7', font=('Garamond',20), command=equal)
equal.grid(row=4, column=3, sticky="nsew")
window.mainloop()
