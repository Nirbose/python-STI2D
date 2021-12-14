from tkinter import *

class Components:
    def label(self, text):
        label = Label(text=text)
        label.pack()
        return label

    def input(self):
        entry = Entry()
        entry.pack()
        return entry
        
    def radio(self, text, value, variable):
        radio = Radiobutton(text=text, value=value, variable=variable)
        radio.pack()
        return radio
    
    def btn(self, text, command):
        btn = Button(text=text, command=command)
        btn.pack()
        return btn 