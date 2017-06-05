from tkinter import *
import random

class Alz(object):
    def __init__(self):
        self.side = 600
        self.delay = 10
        self.chars = '紅綠藍黃黑'
        self.curr_char = random.choice(self.chars)
        self.colors = ['red', 'green', 'blue', 'yellow', 'black']
        self.curr_color = random.choice(self.colors)

        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.side, height=self.side)
        self.canvas.pack()
        self.root.bind('<Key>', self.key)

    def key(self, event):
        self.curr_char = random.choice(self.chars)
        self.curr_color = random.choice(self.colors)

    def draw_char(self):
        self.canvas.create_text(self.side / 2, self.side / 2, text=self.curr_char, font='LiSongPro 200', fill=self.curr_color)

    def redraw(self):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(0, 0, self.side, self.side, width=0, fill='darkGrey')

        self.draw_char()

        self.canvas.update()

    def timer(self):
        self.redraw()
        self.canvas.after(self.delay, self.timer)

    def run(self):
        self.timer()
        self.root.mainloop()

alz = Alz()
alz.run()
