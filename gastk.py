from Tkinter import *
import random
import digit

window = Tk()
HEIGHT = 100
WIDTH = 300
window.title('Gas Pump')

def litres_this_sale(window):
    width, height = 50, 100
    canvas = Canvas(window, width=width, height=height, bg='white')
    canvas.create_text(30, 40, text='LITRES')
    canvas.create_text(30, 54, text='THIS')
    canvas.create_text(30, 65, text='SALE')
    canvas.pack(side = LEFT)

def price_this_sale(window):
    width, height = 50, 100
    canvas = Canvas(window, width=width, height=height, bg='white')
    canvas.create_text(30, 40, text='PRICE')
    canvas.create_text(30, 54, text='THIS')
    canvas.create_text(30, 65, text='SALE')
    canvas.pack(side = LEFT)

def create_digit(window):
    width, height = 100, 100
    c = Canvas(window, width=width, height=height, bg='white')
    c.pack(side = LEFT)
    c.digitTop = c.create_rectangle(25,10,60,20, fill='black',)
    c.digitTL= c.create_rectangle(10,15,20,45, fill ='black')
    c.digitMid = c.create_rectangle(25,50,60,60, fill = 'black')
    c.digitBL = c.create_rectangle(10,55,20,90, fill ='black')
    c.digitBottom = c.create_rectangle(25,85,60,95, fill='black')
    c.digitTR = c.create_rectangle(65,15,75,45, fill='black')
    c.digitBR = c.create_rectangle(65,55,75,90,fill='black')
    return c

def create_decimal(window):
    width, height = 12, 100
    e = Canvas(window, width=width, height=height)
    e.pack(side = LEFT)
    decimal = e.create_rectangle(10,90,15,95,fill='black')
    return e

def set_digit_to(canvas, number):
    canvas.itemconfig(canvas.digitTop, state = NORMAL)
    canvas.itemconfig(canvas.digitTL, state = NORMAL)
    canvas.itemconfig(canvas.digitMid, state = NORMAL)
    canvas.itemconfig(canvas.digitBL, state = NORMAL)
    canvas.itemconfig(canvas.digitBottom, state = NORMAL)
    canvas.itemconfig(canvas.digitBR, state = NORMAL)
    canvas.itemconfig(canvas.digitTR, state = NORMAL)
    if number == 1 :
        canvas.itemconfig(canvas.digitTop, state = HIDDEN)
        canvas.itemconfig(canvas.digitTL, state = HIDDEN)
        canvas.itemconfig(canvas.digitMid, state = HIDDEN)
        canvas.itemconfig(canvas.digitBL, state = HIDDEN)
        canvas.itemconfig(canvas.digitBottom, state = HIDDEN)
    elif number ==  2:
        canvas.itemconfig(canvas.digitTL, state = HIDDEN)
        canvas.itemconfig(canvas.digitBR, state = HIDDEN)
    elif number == 3:
        canvas.itemconfig(canvas.digitTL, state = HIDDEN)
        canvas.itemconfig(canvas.digitBL, state = HIDDEN)
    elif number == 4:
        canvas.itemconfig(canvas.digitTop, state = HIDDEN)
        canvas.itemconfig(canvas.digitBR, state = HIDDEN)
        canvas.itemconfig(canvas.digitBottom, state = HIDDEN)
    elif number == 5:
        canvas.itemconfig(canvas.digitTR, state = HIDDEN)
        canvas.itemconfig(canvas.digitBL, state = HIDDEN)
    elif number == 6:
        canvas.itemconfig(canvas.digitTR, state = HIDDEN)
    elif number == 7:
        canvas.itemconfig(canvas.digitTL, state = HIDDEN)
        canvas.itemconfig(canvas.digitMid, state = HIDDEN)
        canvas.itemconfig(canvas.digitBL, state = HIDDEN)
        canvas.itemconfig(canvas.digitBottom, state = HIDDEN)
    elif number == 9:
        canvas.itemconfig(canvas.digitBL, state = HIDDEN)
        canvas.itemconfig(canvas.digitBottom, state = HIDDEN)
    elif number == 0:
        canvas.itemconfig(canvas.digitMid, state = HIDDEN)

def create_gas_display(window):
    frame = Frame(window)
    frame.pack()
    frame.gaspumped = litres_this_sale(frame)
    frame.Gasdigit1 = create_digit(frame)
    frame.Gasdigit2 = create_digit(frame)
    frame.Gasdigit3= create_digit(frame)
    frame.Gasdecimal = create_decimal(frame)
    frame.Gasdigit4 = create_digit(frame)
    frame.Gasdigit5 = create_digit(frame)
    return frame
display = create_gas_display(window)

def create_price_display(window):
    frame = Frame(window)
    frame.pack()
    frame.price = price_this_sale(frame)
    frame.pricedigit1 = create_digit(frame)
    frame.pricedigit2 = create_digit(frame)
    frame.pricedigit3= create_digit(frame)
    frame.pricedecimal = create_decimal(frame)
    frame.pricedigit4 = create_digit(frame)
    frame.pricedigit5 = create_digit(frame)
    return frame
display2 = create_price_display(window)

gaspumped = 0
gasprice = 1.64

def gas_litre(target, digitDisplay):
    targetstr = str(target)
    parts = targetstr.split('.')
    before = parts[0]
    after = parts[1]
    before = before.rjust(3, '0')
    after = after.ljust(2, '0')
    print 'before',before
    print 'after', after
    targetstr = before + '.' + after
    print 'targetstr', targetstr
    digit1 = int(targetstr[0])
    digit2 = int(targetstr[1])
    digit3 = int(targetstr[2])
    digit4 = int(targetstr[4])
    digit5 = int(targetstr[5])
    set_digit_to(digitDisplay.Gasdigit1,digit1)
    set_digit_to(digitDisplay.Gasdigit2,digit2)
    set_digit_to(digitDisplay.Gasdigit3,digit3)
    set_digit_to(digitDisplay.Gasdigit4,digit4)
    set_digit_to(digitDisplay.Gasdigit5,digit5)
gas_litre(000.00,display)

def sale_price(target, digitDisplay):
    targetstr = str(target)
    parts = targetstr.split('.')
    before = parts[0]
    after = parts[1]
    before = before.rjust(3, '0')
    after = after.ljust(2, '0')
    print 'before',before
    print 'after', after
    targetstr = before + '.' + after
    print 'targetstr', targetstr
    digit1 = int(targetstr[0])
    digit2 = int(targetstr[1])
    digit3 = int(targetstr[2])
    digit4 = int(targetstr[4])
    digit5 = int(targetstr[5])
    set_digit_to(digitDisplay.pricedigit1,digit1)
    set_digit_to(digitDisplay.pricedigit2,digit2)
    set_digit_to(digitDisplay.pricedigit3,digit3)
    set_digit_to(digitDisplay.pricedigit4,digit4)
    set_digit_to(digitDisplay.pricedigit5,digit5)
sale_price(000.00, display2)

def bAaction():
    gas_litre(000.00,display)
    sale_price(000.00, display2)
def bBaction():
    global gaspumped
    gaspumped += 0.34
    totalcost = gaspumped * gasprice
    gas_litre(gaspumped,display)
    sale_price(totalcost,display2)
buttonA = Button(window, text='Pick Up Pump', command=bAaction)
buttonB = Button(window, text='Pump Gas', command=bBaction)
buttonA.pack()
buttonB.pack()
# josephdigit = digit.Digit(window, 2)

window.mainloop()

