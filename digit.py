from Tkinter import *

class Digit(Canvas):
    def __init__(self, parent, starting_value):
        width, height = 100, 100
        Canvas.__init__(self, parent, width=width, height=height, bg='white')
        # draw your digit to show the starting_value
        self.pack(side = LEFT)
        self.digitTop = self.create_rectangle(25,10,60,20, fill='black',)
        self.digitTL= self.create_rectangle(10,15,20,45, fill ='black')
        self.digitMid = self.create_rectangle(25,50,60,60, fill = 'black')
        self.digitBL = self.create_rectangle(10,55,20,90, fill ='black')
        self.digitBottom = self.create_rectangle(25,85,60,95, fill='black')
        self.digitTR = self.create_rectangle(65,15,75,45, fill='black')
        self.digitBR = self.create_rectangle(65,55,75,90,fill='black')
        self.set_value(starting_value)

    def set_value(self, number):
        # redraw your digit to show value
        self.itemconfig(self.digitTop, state = NORMAL)
        self.itemconfig(self.digitTL, state = NORMAL)
        self.itemconfig(self.digitMid, state = NORMAL)
        self.itemconfig(self.digitBL, state = NORMAL)
        self.itemconfig(self.digitBottom, state = NORMAL)
        self.itemconfig(self.digitBR, state = NORMAL)
        self.itemconfig(self.digitTR, state = NORMAL)
        if number == 1 :
            self.itemconfig(self.digitTop, state = HIDDEN)
            self.itemconfig(self.digitTL, state = HIDDEN)
            self.itemconfig(self.digitMid, state = HIDDEN)
            self.itemconfig(self.digitBL, state = HIDDEN)
            self.itemconfig(self.digitBottom, state = HIDDEN)
        elif number ==  2:
            self.itemconfig(self.digitTL, state = HIDDEN)
            self.itemconfig(self.digitBR, state = HIDDEN)
        elif number == 3:
            self.itemconfig(self.digitTL, state = HIDDEN)
            self.itemconfig(self.digitBL, state = HIDDEN)
        elif number == 4:
            self.itemconfig(self.digitTop, state = HIDDEN)
            self.itemconfig(self.digitBR, state = HIDDEN)
            self.itemconfig(self.digitBottom, state = HIDDEN)
        elif number == 5:
            self.itemconfig(self.digitTR, state = HIDDEN)
            self.itemconfig(self.digitBL, state = HIDDEN)
        elif number == 6:
            self.itemconfig(self.digitTR, state = HIDDEN)
        elif number == 7:
            self.itemconfig(self.digitTL, state = HIDDEN)
            self.itemconfig(self.digitMid, state = HIDDEN)
            self.itemconfig(self.digitBL, state = HIDDEN)
            self.itemconfig(self.digitBottom, state = HIDDEN)
        elif number == 9:
            self.itemconfig(self.digitBL, state = HIDDEN)
            self.itemconfig(self.digitBottom, state = HIDDEN)
        elif number == 0:
            self.itemconfig(self.digitMid, state = HIDDEN)


# window = Tk()
# HEIGHT = 100
# WIDTH = 300
# window.title('Gas Pump')
# digit1 = Digit(window, 1)
# digit1.set_value(5)
# window.mainloop()