#!/usr/bin/python
from tkinter import *
import tkinter as tk
import tkinter.font as TkFont
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

        bpcs.decode(file, "decoded_message.txt", alpha)
        with open('decoded_message.txt') as file:
            data = str(file.read())
            return data
        # decodedoutput.insert(tk.END, data)
    elif option == 2 and message is not None:
        pic = "encoded_file.png"  # +file.split('.')[1]
        bpcs.encode(file, message, pic, alpha)
    else:
        print("Invalid Option")
    return None


def ConfirmAction():
    payloadname = e1.get()
    covername = e2.get()
    # print(payloadname[-3:],"payload type","//cover==",covername.split(".")[1])
    encodedfilename = ""
    outputtext = tk.Text(window, width=25, height=20, bg="white")
    imagecanvas = Canvas(window, width=picwidth, height=picheight)
    if covername[-3:] == "txt":
        print("Error: Cannot put txt file as Cover Image")
    else:
        canvas = Canvas(window, width=picwidth, height=picheight)

        encodedimg = Canvas(window, width=picwidth, height=picheight)
        img = ImageTk.PhotoImage(Image.open(covername).resize((200, 200), Image.ANTIALIAS))  # prep payload image
        canvas.grid(row=5, column=1)
        encodedimg.grid(row=5, column=5)
        canvas.create_image(10, 10, anchor=NW, image=img)

        if payloadname[-3:] == "txt" and covername.split(".")[1] == "png":
            # lab = tk.Label(window, width=30, text=payloadname.split("/")[-1])
            # lab.grid(row=3, column=1)
            # coverlabel1 = tk.Label(window, text="Cover image:").grid(row=3, column=1)  # prep payload label

            encodedfilename = "encoded_file.png"
            ExtractPayload(covername, 2, 0.45, message=payloadname)
            data = ExtractPayload(encodedfilename, 1, 0.45)

            outputtext.grid(row=8, column=1, sticky=tk.N + tk.W)
            # Display image with encoded stuff
            outputtext.insert(tk.END, data)
            # encodedimg = Canvas(window, width=picwidth, height=picheight)
            # encodedimg.grid(row=5, column=5)
            # img2 = ImageTk.PhotoImage(Image.open("encoded_file.png").resize((300, 300), Image.ANTIALIAS))#prep cover image
            # canvas2.create_image(10, 10,  image=img2)

            button4 = tk.Button(window, text='Clear Text', command=outputtext.destroy).grid(row=8, column=4, sticky=NE)
        elif payloadname[-3:] == "txt" and covername.split(".")[1] == "jpg":

            # print("jpg detected")
            #
            # # coverlabel1 = tk.Label(window, text="Cover image:").grid(row=3, column=1)  # prep cover label
            # canvas = createImage(covername)
            # canvas.grid(row=5, column=1)
            # # img = ImageTk.PhotoImage(Image.open(covername), Image.ANTIALIAS)#prep cover image
            # # canvas.create_image(10, 10,  image=img)

            ExtractPayload(covername, 2, 0.45, message=payloadname)
            data = ExtractPayload("encoded_file.png", 1, 0.45)

            encodedfilename = "encoded_file.jpg"
            origPNG = Image.open("encoded_file.png")  # convert png to jpeg
            rgb_jpg = origPNG.convert('RGB')
            rgb_jpg.save(encodedfilename)
            # outputtext = tksText(window, width=25, height=20, bg="white")
            outputtext.grid(row=8, column=1, sticky=tk.N + tk.W)
            # Display image with encoded stuff
            outputtext.insert(tk.END, data)
            # encodedimg=createImage('encoded_file.jpg')
            # canvas2 = Canvas(window, width=picwidth, height=picheight)
            # canvas2.grid(row=5, column=5)
            # img2 = ImageTk.PhotoImage(Image.open('encoded_file.jpg').resize((300, 300), Image.ANTIALIAS))
            # canvas2.create_image(10, 10, anchor=NW, image=img2)

            button4 = tk.Button(window, text='Clear Text', command=outputtext.destroy).grid(row=8, column=4, sticky=NE)
        elif imghdr.what(covername) == "png" and imghdr.what(payloadname) == "png":
            # coverlabel1 = tk.Label(window, text="Cover image:").grid(row=3, column=1) #prep cover label
            # canvas =createImage(covername)
            # # canvas = Canvas(window, width=picwidth, height=picheight)
            # canvas.grid(row=5, column=1)
            # img = ImageTk.PhotoImage(Image.open(covername).resize((300, 300), Image.ANTIALIAS))
            # canvas.create_image(10, 10, anchor=NW, image=img)
            EncodeDecodePNG2PNG(payloadname, covername)
            imagecanvas = Canvas(window, width=picwidth, height=picheight)
            imagecanvas.grid(row=8, column=1)
            imagemsg = ImageTk.PhotoImage(Image.open("RetrievedImage.png").resize((200, 200), Image.ANTIALIAS))
            imagecanvas.create_image(10, 10, anchor=NW, image=imagemsg)
            encodedfilename = "encoded_file.png"
            button4 = tk.Button(window, text='Clear Image', command=imagecanvas.destroy).grid(row=8, column=4, sticky=NE)
        elif covername.split(".")[1] == "jpg" and payloadname.split(".")[1] == "jpg":
            # coverlabel1 = tk.Label(window, text="Cover image:").grid(row=3, column=1)  # prep payload label
            # canvas = Canvas(window, width=picwidth, height=picheight)
            # canvas =createImage(covername)
            # # canvas = Canvas(window, width=picwidth, height=picheight)
            # canvas.grid(row=5, column=1)
            # canvas.grid(row=4, column=1)
            # img = ImageTk.PhotoImage(Image.open(covername).resize((300, 300), Image.ANTIALIAS))
            # canvas.create_image(10, 10, anchor=NW, image=img)
            EncodeDecodeJPG2JPG(payloadname, covername)
            encodedfilename = "encoded_file.jpg"

            imagecanvas.grid(row=8, column=1)
            imagemsg = ImageTk.PhotoImage(Image.open('RetrievedImage.jpg').resize((200, 200), Image.ANTIALIAS))
            imagecanvas.create_image(10, 10, anchor=NW, image=imagemsg)
            button4 = tk.Button(window, text='Clear Image', command=imagecanvas.destroy).grid(row=8, column=4, sticky=NE)
        elif covername.split(".")[1] != payloadname.split(".")[1]:
            temp1 = ""
            temp2 = ""
            # coverlabel1 = tk.Label(window, text="Cover image:").grid(row=3, column=1)  # prep cover label
            # canvas = Canvas(window, width=picwidth, height=picheight)
            # # canvas.grid(row=4, column=1)
            # img = ImageTk.PhotoImage(Image.open(covername).resize((300, 300), Image.ANTIALIAS))
            # canvas.create_image(10, 10, anchor=NW, image=img)

            # coverlabel1 = tk.Label(window, text="Payload image:").grid(row=3, column=2)  # prep payload label

            # decodecanvas=createImage(payloadname)
            # # canvas11 = Canvas(window, width=picwidth, height=picheight)
            # canvas11.grid(row=4, column=2)
            # img11 = ImageTk.PhotoImage(Image.open(payloadname).resize((300, 300), Image.ANTIALIAS))
            # canvas11.create_image(10, 10, anchor=NW, image=img11)

            origPNG = Image.open(payloadname)  # convert png to jpeg
            rgb_jpg = origPNG.convert('RGB')
            rgb_jpg.save('temp1.png')

            origPNG2 = Image.open(covername)  # convert png to jpeg
            rgb_jpg2 = origPNG2.convert('RGB')
            rgb_jpg2.save('temp2.png')

            EncodeDecodePNG2PNG("temp1.png", "temp2.png")
            encodedfilename = "encoded_file.png"

            imagecanvas = Canvas(window, width=picwidth, height=picheight)
            imagecanvas.grid(row=8, column=1)
            imagemsg = ImageTk.PhotoImage(Image.open("RetrievedImage.png").resize((200, 200), Image.ANTIALIAS))
            imagecanvas.create_image(10, 10, anchor=NW, image=imagemsg)
            button4 = tk.Button(window, text='Clear Image', command=imagecanvas.destroy).grid(row=8, column=4, sticky=NE)

        img2 = ImageTk.PhotoImage(Image.open(encodedfilename).resize((200, 200), Image.ANTIALIAS))  # prep cover image
        encodedimg.create_image(10, 10, anchor=NW, image=img2)

    window.mainloop()


def EncodeDecodeJPG2JPG(payloadname, covername):
    fileext = ["jpg", "jpeg", "png"]
    payloadname = e1.get()
    covername = e2.get()

    origJPG = Image.open(payloadname)  # convert jpeg to png
    rgb_jpg = origJPG.convert('RGB')
    rgb_jpg.save('encoded_file.png')

    with open('encoded_file.png', 'rb') as fp, open('base64String.txt', 'wb') as fp2:
        base64.encode(fp, fp2)  # let base64 do encoding and export excoded text to txt file

    strg = os.path.dirname(os.path.abspath(__file__)) + "\\base64String.txt"  # locate text file

    # payloadlabel1 = tk.Label(window, text="Payload image:").grid(row=3, column=2)  # prep payload label

    canvas2 = Canvas(window, width=picwidth, height=picheight)
    # canvas2.grid(row=4, column=2)
    cover2 = Image.open(payloadname)
    image2 = cover2.resize((300, 300), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(image2)  # cover image
    canvas2.create_image(10, 10, anchor=NW, image=img2)  # show payload image (before stego)

    ExtractPayload(covername, 2, 0.45, message=strg)  # encode cover image with payload image
    ExtractPayload("encoded_file.png", 1,
                   0.45)  # decode and place base64 (of image) to text file as decoded output (decoded_message.txt)

    origPNG = Image.open("encoded_file.png")  # convert png to jpeg
    rgb_jpg = origPNG.convert('RGB')
    rgb_jpg.save('encoded_file.jpg')

    # stegolabel1 = tk.Label(window, text="Stego image:").grid(row=3, column=2)  # prep stego iamge label
    # canvas3 = Canvas(window, width=picwidth, height=picheight)
    # # canvas3.grid(row=6, column=1)  # encoded Image (Stego)
    # img3 = ImageTk.PhotoImage(Image.open("encoded_file.jpg").resize((300, 300), Image.ANTIALIAS))
    # canvas3.create_image(10, 10, anchor=NW, image=img3)

    origPNG = Image.open("encoded_file.jpg")  # convert jpeg to png
    rgb_jpg = origPNG.convert('RGB')
    rgb_jpg.save('encoded_file.png')

    with open("decoded_message.txt", 'rb') as fp, open('RetrievedImage.png', 'wb') as fp2:
        base64.decode(fp, fp2)  # let base64 do decoding to png image and export image to png file

    origPNG = Image.open("RetrievedImage.png")  # convert png to jpeg
    rgb_jpg = origPNG.convert('RGB')
    rgb_jpg.save('RetrievedImage.jpg')

    # recoveredlabel1 = tk.Label(window, text="Recovered Hidden image:").grid(row=5, column=2)
    # imagecanvas = Canvas(window, width=picwidth, height=picheight)
    # imagecanvas.grid(row=8, column=1)
    # imagemsg = ImageTk.PhotoImage(Image.open('RetrievedImage.jpg').resize((200, 200), Image.ANTIALIAS))
    # imagecanvas.create_image(10, 10, anchor=NW, image=imagemsg) #show extracted hidden payload image from previously encoded image
    # window.mainloop()


def EncodeDecodePNG2PNG(payloadname, covername):
    with open(payloadname, 'rb') as fp, open('base64String.txt', 'wb') as fp2:
        base64.encode(fp, fp2)  # let base64 do encoding and export excoded text to txt file

    strg = os.path.dirname(os.path.abspath(__file__)) + "\\base64String.txt"  # locate text file

    ExtractPayload(covername, 2, 0.45, message=strg)  # encode cover image with payload image
    ExtractPayload("encoded_file.png", 1,
                   0.45)  # decode and place base64 (of image) to text file as decoded output (decoded_message.txt)

    # stegolabel1 = tk.Label(window, text="Stego image:").grid(row=3, column=2) #prep stego iamge label
    # canvas3 = Canvas(window, width=picwidth, height=picheight)
    # # canvas3.grid(row=6, column=1) #encoded Image (Stego)
    # img3 = ImageTk.PhotoImage(Image.open("encoded_file.png").resize((200, 200), Image.ANTIALIAS))
    # canvas3.create_image(10, 10, anchor=NW, image=img3)

    with open("decoded_message.txt", 'rb') as fp, open('RetrievedImage.png', 'wb') as fp2:
        base64.decode(fp, fp2)  # let base64 do decoding to png image and export image to png file

    # recoveredlabel1 = tk.Label(window, text="Recovered Hidden image:").grid(row=5, column=2)
    # imagecanvas = Canvas(window, width=picwidth, height=picheight)
    # imagecanvas.grid(row=8, column=1)
    # imagemsg = ImageTk.PhotoImage(Image.open("RetrievedImage.png").resize((200,200), Image.ANTIALIAS))
    # imagecanvas.create_image(10, 10, anchor=NW, image=imagemsg) #show extracted hidden payload image from previously encoded image


window = tk.Tk()
picwidth = 200
picheight = 200
bgimg = ImageTk.PhotoImage(Image.open("bgimg.jpg").resize((1600, 900), Image.ANTIALIAS))  # PIL solution
background_label = Label(window, image=bgimg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
window.title("BPCS Module")
window.geometry("1600x900")


payloadlabel = tk.Label(window, text="Cover image file:").grid(row=2, column=0, padx=(210, 0))
coverlabel = tk.Label(window, text="Cover image").grid(row=4, column=1, sticky=NW)
stegolabel1 = tk.Label(window, text="Stego image").grid(row=4, column=5, sticky=NE)  # prep stego iamge label
payloadlabel = tk.Label(window, text="Payload file:").grid(row=1, column=0, padx=(210, 0))
e1 = tk.Entry(window, width=30)
e1.grid(row=1, column=1)
button1 = tk.Button(window, text='Upload', command=UploadPayload).grid(row=1, column=1, sticky=NE)
payloadlabel = tk.Label(window, text="Cover image file:").grid(row=2, column=0, padx=(210, 0))
e2 = tk.Entry(window, width=30)
e2.grid(row=2, column=1)
button3 = tk.Button(window, text='Upload', command=UploadCover).grid(row=2, column=1, sticky=NE)
button2 = tk.Button(window, text='Submit', command=ConfirmAction, height=1, width=10).grid(row=3, column=1, sticky=NW)
decodedlabel = tk.Label(window, text="Decoded Message").grid(row=7, column=1, sticky=NW)

# outputlabel = Label(window, text="Output:").grid(row=8, column=0, sticky=NW,padx=(210, 0))

# quitbutton = tk.Button(window, text="Quit", command=window.destroy, fg="red").grid(row=8, column=6)
#
helv36 = TkFont.Font(family="Helvetica", size=36, weight="bold")
title = tk.Label(window, text="BPCS Encoder", font=helv36).grid(row=0, column=2)


window.mainloop()
