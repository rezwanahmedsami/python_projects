from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock By Sami")

def time():
   # string = strftime('%H:%M:%S %p')
   H = strftime('%H')
   M = strftime('%M')
   S = strftime('%S')
   p = strftime(' %p')
   if int(H) > 12:
     H = int(H) - 12
     clock = str(H)+':'+str(M)+':'+str(S)+p
   else:
     clock = str(H)+':'+str(M)+':'+str(S)+p
     

   label.config(text = clock)
   label.after(1000, time)


label = Label(root,font =("Tahoma",100), background = "black", foreground = "cyan")
label.pack(anchor="center")


time()

mainloop()