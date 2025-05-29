import tkinter as tk
from tkinter import messagebox
from pyfiglet import figlet_format, Figlet
import random

def sampleFontTest():
    name="kaled"
    asciiMsg = figlet_format(name, font="xttyb")
    messagebox.showinfo("Greeting", f"{name}\n\n{asciiMsg}")
    # messagebox.showinfo(figlet_format(name, font="xttyb"))


def previewAllFonts():
    from pyfiglet import Figlet
    f = Figlet(font='standard')
    for font in f.getFonts():
        f.setFont(font=font)
        print(font+"\n" +f.renderText('Kaled'))

def listAllFontsInDictionary():
    fontStyleList = sorted(Figlet().getFonts())
    print(fontStyleList)

# printAllFonts()
# sampleFontTest()
listAllFontsInDictionary()