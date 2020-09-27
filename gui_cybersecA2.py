#!/usr/bin/python
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import imghdr
import bpcs
import os


def UploadAction():
    filename = filedialog.askopenfilename()
    # e1.insert(filename)
    if len(e1.get()) > 0:
        e1.config(state=NORMAL)
        e1.delete(0, END)
    e1.insert(10, str(filename))


def ExtractPayload(file, option, alpha, message=None):
    if option == "Decode":
        # output = open("decoded_message.txt", "x")
        tk.Label(window, text="File is saved to:decoded_message.txt").grid(row=3, column=1)
        bpcs.decode(file, "decoded_message.txt", alpha)
        with open('decoded_message.txt') as file:
            data = str(file.read())
            print(data)
        output.insert(tk.END, data)
    elif option == "Encode" and message is not None:
        bpcs.encode(file, message, "encoded_file.png", alpha)
    else:
        print("Invalid Option")


def ConfirmAction():
    fileext = ["jpg", "jpeg", "png"]
    filename = e1.get()
    print(filename[-1:-4:1])
    if filename[-1:-4:1] == "txt":
        lab = tk.Label(window, width=30, text=filename.split("/")[-1])
        lab.grid(row=4, column=1)
    elif imghdr.what(filename) in fileext:
        canvas = Canvas(window, width=300, height=300)
        canvas.grid(row=4, column=1)
        img = PhotoImage(file=filename)
        canvas.create_image(10, 10, anchor=NW, image=img)
    else:
        lab = tk.Label(window, width=15, text="Incorrect file format")
        lab.grid(row=4, column=1)
    ExtractPayload(filename, option, 0.45)
    window.mainloop()


def change_dropdown(*args):
    global option
    option = str(tkdropdown.get())


window = tk.Tk()
window.title("Test 1")
window.geometry("700x700")
label = tk.Label(window, text="File name").grid(row=0)
e1 = tk.Entry(window, width=30)
e1.grid(row=0, column=1)
output = tk.Text(window, height=50, width=50, bg="light yellow")
output.grid(row=6, column=1)
choices = {"Select an Option", "Encode", "Decode"}
tkdropdown = StringVar(window)
tkdropdown.set("Select an Option")
popupMenu = OptionMenu(window, tkdropdown, *choices)
label1 = Label(window, text="Command").grid(row=1, column=0)
label2 = Label(window, text="Output text").grid(row=5, column=0)

popupMenu.grid(row=1, column=1)

tkdropdown.trace('w', change_dropdown)
button1 = tk.Button(window, text='Upload', command=UploadAction).grid(row=0, column=2)
button2 = tk.Button(window, text='Submit', command=ConfirmAction).grid(row=2, column=1)

window.mainloop()
