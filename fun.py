import tkinter as tk
from tkinter import  messagebox, Toplevel, Text, Scrollbar
from pyfiglet import figlet_format, Figlet
import random

def centerWindow(win, width=300, height=150):
    win.update_idletasks()
    screenWidth = win.winfo_screenwidth()
    screenHeight = win.winfo_screenheight()
    x = (screenWidth // 2) - (width // 2)
    y = (screenHeight // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

def greet():
    name = entry.get()
    statements = [
        f"{name}, your keyboard probably types faster than light!",
        f"{name}, you're the bug-free wizard of Python!",
        f"{name}, even your print statements are hilarious!",
        f"{name}, PyInstaller asks for your permission before building!",
        f"{name}, you're the chosen one… to debug this code!",
        f"{name}, your Python code passed flake8 without a scratch!",
        f"{name}, your functions don’t need parameters—they just know!",
        f"{name}, the compiler runs because it’s scared of your code!",
        f"{name}, your code runs faster when you stare at it.",
        f"{name}, you're the reason the semicolon retired from Python.",
        f"{name}, you once `rm -rf /` and nothing bad happened!",
        f"{name}, you bring `__magic__` to every module!",
        f"{name}, even the bugs fear your keyboard.",
        f"{name}, you're the final boss of Stack Overflow!",
        f"{name}, your try-except blocks never need the except.",
        f"{name}, your print statements *always* find the bug.",
        f"{name}, `None` returns your calls.",
        f"{name}, you've never seen a segmentation fault. It’s seen you.",
        f"{name}, the cloud asks *you* for permission to scale.",
        f"{name}, even ChatGPT asks you for help debugging.",
    ]
    fontStyleList2 = [
        "train",
        "doh",
        "sub-zero", 
        "larry3d", 
        "xtty",
        "electronic",
        "big",
        "epic",
        "dos_rebel",
    ]
    # fontStyleList = sorted(Figlet().getFonts())
    fontStyleList = [f for f in Figlet().getFonts() if len(f) <= 10]
    msg = random.choice(statements)
    fontStyle=random.choice(fontStyleList)
    # fontStyle = random.choice(fontStyleList2)
    asciiMsg = figlet_format(name, font=fontStyle, justify="left")
    # messagebox.showinfo("Greeting", f"{msg}\n\n{asciiMsg}")
    top = Toplevel(root)
    top.title("Greeting (Sample for Education)")
    # top.geometry("600x400")

    scrollbar = Scrollbar(top)
    scrollbar.pack(side="right", fill="y")

    text = Text(top, font=("Courier", 10), yscrollcommand=scrollbar.set)
    text.pack(expand=True, fill="both")
    scrollbar.config(command=text.yview)


    text.insert("end", f"{msg}\n\n{asciiMsg}")
    # print(fontStyle)
    text.insert("end", f"\n\nThe font style is {fontStyle}.")    
    text.insert("end", f"\nPress Enter for more!")
    text.insert("end", f"\nClose the main window to exit.")
    text.insert("end", "\n\nYou can check some samples of styles here: http://www.figlet.org/examples.html")
    text.insert("end", "\nOr the full list here: https://github.com/xero/figlet-fonts/tree/master")
    text.config(state="disabled") 

root = tk.Tk()
root.title("Fun App (Sample for Education)")
# root.geometry("300x120")
centerWindow(root, 400, 185)

label = tk.Label(root, text="What's your name?")
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)
entry.focus()
# entry.bind("<Return>", lambda event: greet())

button = tk.Button(root, text="Greet Me!", command=greet)
button.pack(pady=10)
# entry.delete(0, 'end')

label2 = tk.Label(root, text="Created by: Kaled Aljebur\nhttps://github.com/kaledaljebur/py-to-exe")
label2.pack(pady=10)

root.bind('<Return>', lambda event: button.invoke())

root.mainloop()
