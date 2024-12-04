from tkinter import *

window = Tk()
window.geometry('500x360') #500x354
window.title('Calculator')
window.resizable(False, False)

def click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def stergere():
    global expression
    expression = ''
    input_text.set('')

def egalitate():
    try:
        global expression
        rezultat = str(eval(expression))
        input_text.set(rezultat)
        expression = rezultat
    except:
        expression = ''
        input_text.set('Eroare! Te rugam sa apesi tasta CLEAR')

expression = ''
input_text = StringVar()

input_frame = Frame(window, width=312, height=50)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg='#eee', bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack()

frame_butoane = Frame(window, width=500, height=304, bg='grey')
frame_butoane.pack()

# RAND 1
#buton stergere
Button(frame_butoane, text='CLEAR', width=43, height=3, bg='#eee', cursor='hand2',  # la mac width = 38
       command=lambda: stergere()).grid(row=0, column=0, columnspan=3)
#buton impartire
Button(frame_butoane, text='/', width=12, height=3, bg='#FFA500', cursor='hand2',  # la mac width = 10
       command=lambda: click('/')).grid(row=0, column=3)


# RAND 2
#buton sapte
Button(frame_butoane, text='7', width=12, height=3, bg='#eee', cursor='hand2',
       command=lambda: click('7')).grid(row=1, column=0)
#buton opt
Button(frame_butoane, text='8', width=12, height=3, bg='#eee', cursor='hand2',
       command=lambda: click('8')).grid(row=1, column=1)
#buton noua
Button(frame_butoane, text='9', width=12, height=3, bg='#eee', cursor='hand2',
       command=lambda: click('9')).grid(row=1, column=2)
#buton inmultire
Button(frame_butoane, text='*', width=12, height=3, bg='#FFA500', cursor='hand2',
       command=lambda: click('*')).grid(row=1, column=3)


# RAND 3
#buton patru
Button(frame_butoane, text='4', width=12, height=3, bg='#eee', cursor='hand2',
       command=lambda: click('4')).grid(row=2, column=0)
#buton cinci
Button(frame_butoane, text='5', width=12, height=3, bg='#eee', cursor='hand2',
       command=lambda: click('5')).grid(row=2, column=1)
#buton sase
Button(frame_butoane, text='6', width=12, height=3, bg='#eee', cursor='hand2',
       command=lambda: click('6')).grid(row=2, column=2)
#buton minus
Button(frame_butoane, text='-', width=12, height=3, bg='#FFA500', cursor='hand2',
       command=lambda: click('-')).grid(row=2, column=3)


# RAND 4
#buton unu
Button(frame_butoane, text='1', width=12, height=3, bg='#eee', cursor='hand2',
       command=lambda: click('1')).grid(row=3, column=0)
#buton doi
Button(frame_butoane, text='2', width=12, height=3, bg='#eee', cursor='hand2',
       command=lambda: click('2')).grid(row=3, column=1)
#buton trei
Button(frame_butoane, text='3', width=12, height=3, bg='#eee', cursor='hand2',
       command=lambda: click('3')).grid(row=3, column=2)
#buton plus
Button(frame_butoane, text='+', width=12, height=3, bg='#FFA500', cursor='hand2',
       command=lambda: click('+')).grid(row=3, column=3)

# RAND 5
#buton zero
Button(frame_butoane, text='0', width=12, height=3, bg='#eee', cursor='hand2',
       command=lambda: click('0')).grid(row=4, column=0)
#buton zerozero
Button(frame_butoane, text='00', width=12, height=3, bg='#eee', cursor='hand2',
       command=lambda: click('00')).grid(row=4, column=1)
#buton punct
Button(frame_butoane, text='.', width=12, height=3, bg='#eee', cursor='hand2',
       command=lambda: click('.')).grid(row=4, column=2)
#buton egal
Button(frame_butoane, text='=', width=12, height=3, bg='#FFA500', cursor='hand2',
       command=lambda: egalitate()).grid(row=4, column=3)


window.mainloop()
