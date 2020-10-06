#!/usr/bin/python
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import imghdr
import bpcs
import os
import base64


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
            print(type(data))
        output.insert(tk.END, data)
    elif option == 2 and message is not None:
        pic="encoded_file.png"#+file.split('.')[1]
        bpcs.encode(file, message,pic , alpha)
    else:
        print("Invalid Option")

def ConfirmAction():
    fileext = ["jpg", "jpeg", "png"]
    payloadname = e1.get()
    covername = e2.get()
    print(payloadname[-3:],"payload type","//cover==",covername.split(".")[1])

    if(covername[-3:]=="txt"):
        print("Error: Cannot put txt file as Cover Image")
    elif payloadname[-3:] == "txt" and covername.split(".")[1]=="png":
        lab = tk.Label(window, width=30, text=payloadname.split("/")[-1])
        lab.grid(row=3, column=1)

        coverlabel1 = tk.Label(window, text="Cover image:").grid(row=3, column=1)  # prep payload label
        canvas = Canvas(window, width=300, height=300)
        canvas.grid(row=3, column=2)
        img = PhotoImage(file=covername) #prep payload image
        canvas.create_image(10, 10, anchor=NW, image=img)

        stego = tk.Label(window, text="Stego image:").grid(row=3, column=3)  # prep payload label
        ExtractPayload(covername, 2, 0.45, message=payloadname)
        ExtractPayload("encoded_file.png", 1, 0.45)
        canvas2 = Canvas(window, width=300, height=300)
        canvas2.grid(row=3, column=4)
        img2 = ImageTk.PhotoImage(Image.open(covername).resize((300, 300), Image.ANTIALIAS))#prep cover image
        canvas2.create_image(10, 10, anchor=NW, image=img2)

    elif payloadname[-3:] == "txt" and covername.split(".")[1]=="jpg":
        print("jpg detected")

        coverlabel1 = tk.Label(window, text="Cover image:").grid(row=3, column=1)  # prep cover label
        canvas = Canvas(window, width=300, height=300)
        canvas.grid(row=3, column=2)
        img = ImageTk.PhotoImage(Image.open(covername).resize((300, 300), Image.ANTIALIAS))#prep cover image
        canvas.create_image(10, 10, anchor=NW, image=img)

        stego = tk.Label(window, text="Stego image:").grid(row=3, column=3)  # prep stego label
        ExtractPayload(covername, 2, 0.45, message=payloadname)
        ExtractPayload("encoded_file.png", 1, 0.45)

        origPNG = Image.open("encoded_file.png")#convert png to jpeg
        rgb_jpg = origPNG.convert('RGB')
        rgb_jpg.save('encoded_file.jpg')

        canvas2 = Canvas(window, width=300, height=300)
        canvas2.grid(row=3, column=4)
        img2 = ImageTk.PhotoImage(Image.open('encoded_file.jpg').resize((300, 300), Image.ANTIALIAS))
        canvas2.create_image(10, 10, anchor=NW, image=img2)

    elif imghdr.what(covername)=="png" and imghdr.what(payloadname)=="png":
        coverlabel1 = tk.Label(window, text="Cover image:").grid(row=3, column=1) #prep cover label
        canvas = Canvas(window, width=300, height=300)
        canvas.grid(row=3, column=2)
        img = ImageTk.PhotoImage(Image.open(covername).resize((300, 300), Image.ANTIALIAS))
        canvas.create_image(10, 10, anchor=NW, image=img)

        EncodeDecodePNG2PNG(payloadname,covername)
    elif covername.split(".")[1]=="jpg" and payloadname.split(".")[1]=="jpg":
        coverlabel1 = tk.Label(window, text="Cover image:").grid(row=3, column=1)  # prep payload label
        canvas = Canvas(window, width=300, height=300)
        canvas.grid(row=3, column=2)
        img = ImageTk.PhotoImage(Image.open(covername).resize((300, 300), Image.ANTIALIAS))
        canvas.create_image(10, 10, anchor=NW, image=img)
        EncodeDecodeJPG2JPG(payloadname,covername);
    elif covername.split(".")[1]!=payloadname.split(".")[1]:
        temp1=""
        temp2=""
        coverlabel1 = tk.Label(window, text="Cover image:").grid(row=3, column=1)  # prep cover label
        canvas = Canvas(window, width=300, height=300)
        canvas.grid(row=3, column=2)
        img = ImageTk.PhotoImage(Image.open(covername).resize((300, 300), Image.ANTIALIAS))
        canvas.create_image(10, 10, anchor=NW, image=img)

        coverlabel1 = tk.Label(window, text="Payload image:").grid(row=3, column=3)  # prep payload label
        canvas11 = Canvas(window, width=300, height=300)
        canvas11.grid(row=3, column=4)
        img11 = ImageTk.PhotoImage(Image.open(payloadname).resize((300, 300), Image.ANTIALIAS))
        canvas11.create_image(10, 10, anchor=NW, image=img11)

        origPNG = Image.open(payloadname)  # convert png to jpeg
        rgb_jpg = origPNG.convert('RGB')
        rgb_jpg.save('temp1.png')

        origPNG2 = Image.open(covername)  # convert png to jpeg
        rgb_jpg2 = origPNG2.convert('RGB')
        rgb_jpg2.save('temp2.png')

        EncodeDecodePNG2PNG("temp1.png", "temp2.png")
    window.mainloop()

def EncodeDecodeJPG2JPG(payloadname,covername):
    fileext = ["jpg", "jpeg", "png"]
    payloadname = e1.get()
    covername = e2.get()


    origJPG = Image.open(payloadname)#convert jpeg to png
    rgb_jpg = origJPG.convert('RGB')
    rgb_jpg.save('encoded_file.png')

    with open('encoded_file.png', 'rb') as fp, open('base64String.txt', 'wb') as fp2:
        base64.encode(fp, fp2)  # let base64 do encoding and export excoded text to txt file

    strg = os.path.dirname(os.path.abspath(__file__)) + "\\base64String.txt"  # locate text file

    payloadlabel1 = tk.Label(window, text="Payload image:").grid(row=3, column=3)  # prep payload label

    canvas2 = Canvas(window, width=300, height=300)
    canvas2.grid(row=3, column=4)
    cover2 = Image.open(payloadname)
    image2 = cover2.resize((300, 300), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(image2)  # cover image
    canvas2.create_image(10, 10, anchor=NW, image=img2)  # show payload image (before stego)

    ExtractPayload(covername, 2, 0.45, message=strg)  # encode cover image with payload image
    ExtractPayload("encoded_file.png", 1,0.45)  # decode and place base64 (of image) to text file as decoded output (decoded_message.txt)

    origPNG = Image.open("encoded_file.png")  # convert png to jpeg
    rgb_jpg = origPNG.convert('RGB')
    rgb_jpg.save('encoded_file.jpg')

    stegolabel1 = tk.Label(window, text="Stego image:").grid(row=3, column=5)  # prep stego iamge label
    canvas3 = Canvas(window, width=300, height=300)
    canvas3.grid(row=3, column=6)  # encoded Image (Stego)
    img3 = ImageTk.PhotoImage(Image.open("encoded_file.jpg").resize((300, 300), Image.ANTIALIAS))
    canvas3.create_image(10, 10, anchor=NW, image=img3)


    origPNG = Image.open("encoded_file.jpg")  # convert jpeg to png
    rgb_jpg = origPNG.convert('RGB')
    rgb_jpg.save('encoded_file.png')

    with open("decoded_message.txt", 'rb') as fp, open('encoded_file.png', 'wb') as fp2:
        base64.decode(fp, fp2) #let base64 do decoding to png image and export image to png file

    origPNG = Image.open("encoded_file.png")  # convert png to jpeg
    rgb_jpg = origPNG.convert('RGB')
    rgb_jpg.save('encoded_file.jpg')

    recoveredlabel1 = tk.Label(window, text="Recovered Hidden image:").grid(row=3, column=7)
    canvas4 = Canvas(window, width=300, height=300)
    canvas4.grid(row=3, column=8)
    img4 = ImageTk.PhotoImage(Image.open('encoded_file.jpg').resize((300, 300), Image.ANTIALIAS))
    canvas4.create_image(10, 10, anchor=NW, image=img4) #show extracted hidden payload image from previously encoded image
    window.mainloop()

def EncodeDecodePNG2PNG(payloadname,covername):
    with open(payloadname, 'rb') as fp, open('base64String.txt', 'wb') as fp2:
        base64.encode(fp, fp2) #let base64 do encoding and export excoded text to txt file

    strg=os.path.dirname(os.path.abspath(__file__))+"\\base64String.txt" #locate text file



    ExtractPayload(covername, 2, 0.45, message=strg) #encode cover image with payload image
    ExtractPayload("encoded_file.png", 1, 0.45) #decode and place base64 (of image) to text file as decoded output (decoded_message.txt)

    stegolabel1 = tk.Label(window, text="Stego image:").grid(row=3, column=5) #prep stego iamge label
    canvas3 = Canvas(window, width=300, height=300)
    canvas3.grid(row=3, column=6) #encoded Image (Stego)
    img3 = ImageTk.PhotoImage(Image.open("encoded_file.png").resize((300, 300), Image.ANTIALIAS))
    canvas3.create_image(10, 10, anchor=NW, image=img3)


    with open("decoded_message.txt", 'rb') as fp, open('RetrievedImage.png', 'wb') as fp2:
        base64.decode(fp, fp2) #let base64 do decoding to png image and export image to png file

    recoveredlabel1 = tk.Label(window, text="Recovered Hidden image:").grid(row=3, column=7)
    canvas4 = Canvas(window, width=300, height=300)
    canvas4.grid(row=3, column=8)
    img4 = ImageTk.PhotoImage(Image.open("RetrievedImage.png").resize((300, 300), Image.ANTIALIAS))
    canvas4.create_image(10, 10, anchor=NW, image=img4) #show extracted hidden payload image from previously encoded image
    window.mainloop()


window = tk.Tk()
window.title("Cyber Security Part 1 & 2")
window.geometry("2100x900")
payloadlabel = tk.Label(window, text="Payload file:").grid(row=0, column=0)
coverlabel = tk.Label(window, text="Cover image:").grid(row=0, column=3)
e1 = tk.Entry(window, width=30)
e1.grid(row=0, column=1)
e2 = tk.Entry(window, width=30)
e2.grid(row=0, column=4)
button3 = tk.Button(window, text='Upload', command=UploadCover).grid(row=0, column=5)
output = tk.Text(window, height=50, width=100, bg="light yellow")
output.grid(row=5, column=1, columnspan=4, sticky=tk.W + tk.E)
outputlabel = Label(window, text="Output text:").grid(row=5, column=0, sticky=NW)

button1 = tk.Button(window, text='Upload', command=UploadPayload).grid(row=0, column=2)
button2 = tk.Button(window, text='Submit', command=ConfirmAction).grid(row=1, column=2)

window.mainloop()
