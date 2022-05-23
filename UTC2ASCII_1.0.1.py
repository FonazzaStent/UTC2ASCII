import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import *
import os
import io
from unidecode import unidecode
import pyperclip
from tkinter import messagebox

#Create app window
def create_app_window():
    global top
    global root
    img="iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABhGlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV9TpSKVIhYRcchQnSyIijhKFYtgobQVWnUwufQLmjQkKS6OgmvBwY/FqoOLs64OroIg+AHi6OSk6CIl/i8ptIjx4Lgf7+497t4BQqPCVLNrAlA1y0jFY2I2tyoGXuFHP0IYhE9ipp5IL2bgOb7u4ePrXZRneZ/7c/QpeZMBPpF4jumGRbxBPLNp6Zz3icOsJCnE58TjBl2Q+JHrsstvnIsOCzwzbGRS88RhYrHYwXIHs5KhEk8TRxRVo3wh67LCeYuzWqmx1j35C4N5bSXNdZojiGMJCSQhQkYNZVRgIUqrRoqJFO3HPPzDjj9JLplcZTByLKAKFZLjB/+D392ahalJNykYA7pfbPtjFAjsAs26bX8f23bzBPA/A1da219tALOfpNfbWuQICG0DF9dtTd4DLneAoSddMiRH8tMUCgXg/Yy+KQcM3AK9a25vrX2cPgAZ6mr5Bjg4BMaKlL3u8e6ezt7+PdPq7wcgdnKG+sXJsAAAAAZiS0dEAAAAAAAA+UO7fwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+YDEQ8fOTrP2b4AAAHPSURBVFjDtVdbcsMwCATMHXLqXCbnw95+tKiIygqKa894PFnLPJeVwgBA4dr3nbZtIyIiZm7PtKyEAejsjXzozHnFwAwTEQLQBZXX6cx5NFCpRnYEgJ7P5zQZBoD8gpnJzD7O3LEY7Fk1dBgVczMwyjJX6KznZtaSOY5j2FoZRe9G3aEbiPi+7w3zOyfjSWzbRo/Ho30rIr/rEC4zw89UtCczg4i6+wzLl5m199ne6/UCALCP4X9PQOSB80lE6DiO1loA31NwZkBVu/7mnuep8Ge055zJ65j5PQkzY51Iq9UYTZT70BkJV5VwZXT9W50t/i8ezDDNshkz/HQPqHCjC8DZeVeWM2WV7NzZmQ3MMK9WY7Zq+x0JNyKh5LKbWTd+FcxteJZZMXN7IibvysTMpKrdZGRHZ1lW2iPZUdyAot6PyunYKMtqQBINxO0y9zcGlDFvhWM+UTmZUUDMzLhzAs6mzDGNm8PqTEdirmjEHyUclX0kHl76SNaZyCwpYWWxj1XO/Ep79BMDs1PuKrZ8JqychivOS9txZUesjNrMh9w5fpdJuCqv8awXyTr7b6DvylThwWrZOyU0M1SU6y51HJJwVR2vYKdnwqsKV8W+AHoIWN2D2i7gAAAAAElFTkSuQmCC"
    root= tk.Tk()
    top= root
    top.geometry("600x450+468+138")
    top.resizable(0,0)
    top.title("Convert Unicode to ASCII")
    favicon=tk.PhotoImage(data=img) 
    root.wm_iconphoto(True, favicon)

#Create menu
def create_menu():
    global menubar
    global sub_menu
    menubar=tk.Menu(top, tearoff=0)
    top.configure(menu=menubar)
    sub_menu=tk.Menu(top, tearoff=0)
    menubar.add_cascade(menu=sub_menu,compound="left", label="File")
    sub_menu.add_command(compound="left", label="Paste", command=paste_text, accelerator="Alt+P")
    sub_menu.add_command(compound="left",label="Convert", command=Convertfn, accelerator="Alt+V")
    sub_menu.add_command(compound="left",label="Copy", command=Copyfn,accelerator="Alt+C")
    sub_menu.add_command(compound="left",label="Clear", command=ClearTextBox,accelerator="Alt+L")
    sub_menu.add_command(compound="left",label="Quit", command=QuitApp, accelerator="Alt+Q")
    root.bind("<Button-3>", context_menu)
    top.bind_all("<Alt-p>",paste_text_hotkey)
    top.bind_all("<Alt-v>",Convertfn_hotkey)
    top.bind_all("<Alt-c>",Copyfn_hotkey)
    top.bind_all("<Alt-l>",ClearTextBox_hotkey)
    top.bind_all("<Alt-q>",QuitApp_hotkey)




#Textbox
def create_textbox():
    global textbox
    textbox = Text(top)
    textbox.place(relx=0.033, rely=0.022, relheight=0.878, relwidth=0.933)
    scroll_1=Scrollbar (top)
    scroll_1.pack(side=RIGHT, fill=Y)
    textbox.configure(yscrollcommand=scroll_1.set)
    scroll_1.configure(command=textbox.yview)
    textbox.focus_set()

def context_menu(event):
    menu = Menu(root, tearoff = 0)
    menu.add_command(label="Paste", command=paste_text)
    try: 
        menu.tk_popup(event.x_root, event.y_root)
    finally: 
        menu.grab_release()

def paste_text():
    textbox.event_generate(("<<Paste>>"))

def paste_text_hotkey(event):
    paste_text()

def Convertfn():
    global text
    text=textbox.get(1.0,2000.0)
    if text!='':
        asciitxt=unidecode(text)
    textbox.delete(1.0,2000.0)
    textbox.insert(INSERT, asciitxt)

def Convertfn_hotkey(event):
    Convertfn()

def Copyfn():
    global text
    text=textbox.get(1.0,2000.0)
    pyperclip.copy(text)

def Copyfn_hotkey(event):
    Copyfn()

def ClearTextBox():
    textbox.delete(1.0,2000.0)

def ClearTextBox_hotkey(event):
    ClearTextBox()

def QuitApp():
    okcancel= messagebox.askokcancel("Quit?","Do you want to quit the app?",default="ok")
    if okcancel== True:
        top.destroy()

def QuitApp_hotkey(event):
    QuitApp()

def main():
   create_app_window()
   create_textbox()
   create_menu()

main()
root.mainloop()
