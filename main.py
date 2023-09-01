import tkinter as tk
from tkinter import filedialog, Text
import os

apps = []

def addApp():
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=filename)
        label.pack(side=tk.TOP)

def runApp():
    for app in apps:
        os.startfile(app)



root = tk.Tk()
root.geometry("500x600")
root.maxsize(600, 600)
root.configure(bg="black")
root.title("Test")

canvas = tk.Canvas(root, height=500, width=500, bg="black")

frame = tk.Frame(root, bg="green")
frame.place(relwidth=0.8, relheight=0.77, relx=0.1, rely=0.1)

addApps = tk.Button(root, padx=3, pady=7, fg="black", bg="white", text="Add Apps", command=addApp)
addApps.pack(side=tk.BOTTOM)

runApps = tk.Button(root, padx=3, pady=7, fg="black", bg="white", text="Run Apps", command=runApp)
runApps.pack(side=tk.BOTTOM)

root.mainloop()

with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ",")