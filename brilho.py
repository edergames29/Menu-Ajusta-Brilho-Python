from tkinter import *
import time
import threading
import os


def swv():
    brilho = w.get() /10
    while True:
        if (brilho == w.get() / 10):
            #print("parado")
            pass
        else:
            brilho = w.get() /10
            #time.sleep(0.2)
            os.system(f"xrandr --output LVDS-1 --brightness {brilho}")
            print(f"xrandr --output LVDS-1 --brightness {brilho}")

def botaoset():
    brilho = w.get() /10
    print(brilho)
    os.system(f"xrandr --output LVDS-1 --brightness {brilho}")

def ola():
    print("ola")
    
master = Tk()

w = Scale(master,label="Brilho", from_=1, to=10,resolution=0.1, orient=HORIZONTAL)
w.pack()

threading.Thread(target=swv).start()


Button(master, text='Show', command=botaoset).pack()


mainloop()


