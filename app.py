import tkinter as tk
from tkinter import filedialog, Text
import os
import sys, subprocess


def load_prev():
    if os.path.isfile('save.dl'):
        with open ('save.dl') as f:
            infile = f.readlines()[0]
            app_lists = infile.split(',')
            for app in app_lists:
                lablel = tk.Label(frame, text=app, bg="gray")
                lablel.pack()
            return app_lists
            
    return []



def addApp():
    apps = []
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select File", filetypes=(("executable", "*.exe"), ("all files", "*.*")))

    apps.append(filename)
    app_lists.append(filename)
    for app in apps:
        lablel = tk.Label(frame, text=app, bg="gray")
        lablel.pack()
    
    with open('save.dl','w') as f:
        app_list = ",".join(app_lists)
        f.write(app_list)


def openApp():

    for filename in app_lists:
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, filename])

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="#263d42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, rely=0.1, relx=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#263d42", command=addApp)
openFile.pack()

runFile = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="#263d42", command=openApp)
runFile.pack()


app_lists = load_prev()

root.mainloop()
