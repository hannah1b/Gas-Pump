from Tkinter import *
import display

window = Tk()
HEIGHT = 100
WIDTH = 300
window.title('Gas Pump')

display1 = display.Display(window, 0.0)
display2 = display.Display(window, 0.0)

gaspumped = 0
gasprice = 1.64


def bAaction():
    display1.set_value(000.00)
    display2.set_value(000.00)

def bBaction():
    global gaspumped
    gaspumped += 0.34
    totalcost = gaspumped * gasprice
    display1.set_value(gaspumped)
    display2.set_value(totalcost)
buttonA = Button(window, text='Pick Up Pump', command=bAaction)
buttonB = Button(window, text='Pump Gas', command=bBaction)
buttonA.pack()
buttonB.pack()


window.mainloop()

