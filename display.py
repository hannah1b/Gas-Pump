from Tkinter import *
import digit

class Display(Frame):
    def __init__(self, window, starting_value):
        Frame.__init__(self, window)
        self.pack()
        self.gaspumped = litres_this_sale(self)
        self.Gasdigit1 = digit.Digit(self,0)
        self.Gasdigit2 = digit.Digit(self,0)
        self.Gasdigit3 = digit.Digit(self,0)
        self.Gasdecimal = create_decimal(self)
        self.Gasdigit4 = digit.Digit(self,0)
        self.Gasdigit5 = digit.Digit(self,0)
        self.set_value(starting_value)


    def create_price_display(self):
        self.pack()
        self.price = price_this_sale(self)
        self.pricedigit1 = digit.Digit(self)
        self.pricedigit2 = digit.Digit(self)
        self.pricedigit3= digit.Digit(self)
        self.pricedecimal = create_decimal(self)
        self.pricedigit4 = digit.Digit(self)
        self.pricedigit5 = digit.Digit(self)

    def set_value(self, target):
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
        self.Gasdigit1.set_value(digit1)
        self.Gasdigit2.set_value(digit2)
        self.Gasdigit3.set_value(digit3)
        self.Gasdigit4.set_value(digit4)
        self.Gasdigit5.set_value(digit5)




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


def create_decimal(window):
    width, height = 12, 100
    e = Canvas(window, width=width, height=height)
    e.pack(side = LEFT)
    decimal = e.create_rectangle(10,90,15,95,fill='black')
    return e

