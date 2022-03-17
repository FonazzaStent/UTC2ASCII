import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import os
import io
from unidecode import unidecode
import pyperclip

img="iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABhGlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV9TpSKVIhYRcchQnSyIijhKFYtgobQVWnUwufQLmjQkKS6OgmvBwY/FqoOLs64OroIg+AHi6OSk6CIl/i8ptIjx4Lgf7+497t4BQqPCVLNrAlA1y0jFY2I2tyoGXuFHP0IYhE9ipp5IL2bgOb7u4ePrXZRneZ/7c/QpeZMBPpF4jumGRbxBPLNp6Zz3icOsJCnE58TjBl2Q+JHrsstvnIsOCzwzbGRS88RhYrHYwXIHs5KhEk8TRxRVo3wh67LCeYuzWqmx1j35C4N5bSXNdZojiGMJCSQhQkYNZVRgIUqrRoqJFO3HPPzDjj9JLplcZTByLKAKFZLjB/+D392ahalJNykYA7pfbPtjFAjsAs26bX8f23bzBPA/A1da219tALOfpNfbWuQICG0DF9dtTd4DLneAoSddMiRH8tMUCgXg/Yy+KQcM3AK9a25vrX2cPgAZ6mr5Bjg4BMaKlL3u8e6ezt7+PdPq7wcgdnKG+sXJsAAAAAZiS0dEAAAAAAAA+UO7fwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+YDEQ8fOTrP2b4AAAHPSURBVFjDtVdbcsMwCATMHXLqXCbnw95+tKiIygqKa894PFnLPJeVwgBA4dr3nbZtIyIiZm7PtKyEAejsjXzozHnFwAwTEQLQBZXX6cx5NFCpRnYEgJ7P5zQZBoD8gpnJzD7O3LEY7Fk1dBgVczMwyjJX6KznZtaSOY5j2FoZRe9G3aEbiPi+7w3zOyfjSWzbRo/Ho30rIr/rEC4zw89UtCczg4i6+wzLl5m199ne6/UCALCP4X9PQOSB80lE6DiO1loA31NwZkBVu/7mnuep8Ge055zJ65j5PQkzY51Iq9UYTZT70BkJV5VwZXT9W50t/i8ezDDNshkz/HQPqHCjC8DZeVeWM2WV7NzZmQ3MMK9WY7Zq+x0JNyKh5LKbWTd+FcxteJZZMXN7IibvysTMpKrdZGRHZ1lW2iPZUdyAot6PyunYKMtqQBINxO0y9zcGlDFvhWM+UTmZUUDMzLhzAs6mzDGNm8PqTEdirmjEHyUclX0kHl76SNaZyCwpYWWxj1XO/Ep79BMDs1PuKrZ8JqychivOS9txZUesjNrMh9w5fpdJuCqv8awXyTr7b6DvylThwWrZOyU0M1SU6y51HJJwVR2vYKdnwqsKV8W+AHoIWN2D2i7gAAAAAElFTkSuQmCC"

root= tk.Tk()
top= root
top.geometry("600x450+468+138")
top.resizable(0,0)
top.title("Convert Unicode to ASCII")
favicon=tk.PhotoImage(data=img) 
root.wm_iconphoto(True, favicon)


#Convert button
Convert=tk.Button(top)
Convert.place(relx=0.267, rely=0.911, height=24, width=67)
Convert.configure(text='''Convert''')


#Copy button
Copy=tk.Button(top)
Copy.place(relx=0.417, rely=0.911, height=24, width=47)
Copy.configure(text='''Copy''')


#Textbox
textbox = Text(top)
textbox.place(relx=0.033, rely=0.022, relheight=0.878, relwidth=0.933)

#quit
quitbutton=tk.Button(top)
quitbutton.place (relx=0.633, rely=0.911, height=24, width=34)
quitbutton.configure(text='''Quit''')

#clear
clearbutton=tk.Button(top)
clearbutton.place (relx=0.533, rely=0.911, height=24, width=34)
clearbutton.configure(text='''Clear''')

def paste_text():
        textbox.event_generate(("<<Paste>>"))

menu = Menu(root, tearoff = 0)
menu.add_command(label="Paste", command=paste_text)

def context_menu(event): 
    try: 
        menu.tk_popup(event.x_root, event.y_root)
    finally: 
        menu.grab_release() 

def Convertfn(event):
    global text
    text=textbox.get(1.0,2000.0)
    if text!='':
        asciitxt=unidecode(text)
    textbox.delete(1.0,2000.0)
    textbox.insert(INSERT, asciitxt)

def Copyfn(event):
    global text
    text=textbox.get(1.0,20.0)
    pyperclip.copy(text)

def ClearTextBox(event):
    textbox.delete(1.0,2000.0)

def QuitApp(event):
    top.destroy()

Convert.bind("<Button-1>",Convertfn)
Copy.bind("<Button-1>",Copyfn)
quitbutton.bind("<Button-1>",QuitApp)
clearbutton.bind("<Button-1>", ClearTextBox)
root.bind("<Button-3>", context_menu)


textbox.focus_set()

root.mainloop()
