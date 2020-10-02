#!/usr/bin/python
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import imghdr
import bpcs
import os


def UploadPayload():
    filename = filedialog.askopenfilename()
    if len(e1.get()) > 0:
        e1.config(state=NORMAL)
        e1.delete(0, END)
    e1.insert(1, str(filename))


def UploadCover():
    filename = filedialog.askopenfilename()
    if len(e2.get()) > 0:
        e2.config(state=NORMAL)
        e2.delete(0, END)
    e2.insert(1, str(filename))


def ExtractPayload(file, option, alpha, message=None):
    if option == 1:
        # output = open("decoded_message.txt", "x")
        tk.Label(window, text="File is saved to:decoded_message.txt").grid(row=2, column=1)
        bpcs.decode(file, "decoded_message.txt", alpha)
        with open('decoded_message.txt') as file:
            data = str(file.read())
            # print(data)
        output.insert(tk.END, data)
    elif option == 2 and message is not None:
        bpcs.encode(file, message, "encoded_file.png", alpha)
    else:
        print("Invalid Option")

def ConfirmAction():
    fileext = ["jpg", "jpeg", "png"]
    payloadname = e1.get()
    covername = e2.get()
    print(payloadname[-1:])
    if payloadname[-1:-3:1] == "txt":
        lab = tk.Label(window, width=30, text=payloadname.split("/")[-1])
        lab.grid(row=3, column=1)
    elif imghdr.what(covername) in fileext:
        canvas = Canvas(window, width=300, height=300)
        canvas.grid(row=3, column=1)
        img = PhotoImage(file=covername)
        canvas.create_image(10, 10, anchor=NW, image=img)
    else:
        lab = tk.Label(window, width=15, text="Incorrect file format")
        lab.grid(row=3, column=1)
    ExtractPayload(covername, 2, 0.45, message=payloadname)
    ExtractPayload("encoded_file.png", 1, 0.45)
    canvas2 = Canvas(window, width=300, height=300)
    canvas2.grid(row=3, column=3)
    img2 = ImageTk.PhotoImage(Image.open("encoded_file.png"))
    canvas2.create_image(10, 10, anchor=NW, image=img2)
    window.mainloop()


window = tk.Tk()
window.title("Test 1")
window.geometry("700x700")
payloadlabel = tk.Label(window, text="Payload file").grid(row=0, column=0)
coverlabel = tk.Label(window, text="Cover image").grid(row=0, column=3)
e1 = tk.Entry(window, width=30)
e1.grid(row=0, column=1)
e2 = tk.Entry(window, width=30)
e2.grid(row=0, column=4)
button3 = tk.Button(window, text='Upload', command=UploadCover).grid(row=0, column=5)
output = tk.Text(window, height=50, width=30, bg="light yellow")
output.grid(row=5, column=1, columnspan=4, sticky=tk.W + tk.E)
outputlabel = Label(window, text="Output text").grid(row=5, column=0, sticky=NW)

button1 = tk.Button(window, text='Upload', command=UploadPayload).grid(row=0, column=2)
button2 = tk.Button(window, text='Submit', command=ConfirmAction).grid(row=1, column=2)

window.mainloop()
