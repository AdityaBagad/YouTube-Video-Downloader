'''
Author : Aditya Bagad
'''
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube

def clickDownload():
    if(getURL.get() == ""):
        messagebox.showinfo("ERROR", "ENTER url ")
        return
    elif (getLoc.get() == ""):
        messagebox.showinfo("ERROR", "ENTER LOCATION ")
        return

    select = listbox.curselection()
    quality = videos[select[0]]
    location = getLoc.get()
    quality.download(location)
    messagebox.showinfo("Downloading Finish", yt.title+" has been downloaded Sucessfully!!!")

def setURL():
    #Get URL of the Video
    url = getURL.get()
    print(url)

    #Create Object to hold the URL
    global yt
    yt = YouTube(url)
    print(yt.title)

    # Get the Quality of the Videos and store in the 'videos' variable
    global videos
    videos = yt.streams.filter(mime_type='video/mp4').all()

    #Get Quality and display as list in the Listbox
    count = 1
    for v in videos:
        listbox.insert(END, str(count)+". "+str(v)+"\n\n")
        count += 1


def clickBrowse():
    location_of_download = filedialog.askdirectory()
    getLoc.set(location_of_download)

def clickReset():
    getURL.set("")
    getLoc.set("")
    listbox.delete(0,END)

#Create Root Object
root = Tk()

#Set Title
root.title("YouTube Video Dowloader")

#Set size of window
root.geometry("855x500")

#Make the Window not Resizeable
root.resizable(False, False)

#Set Labels
headLabel       = Label(root,   text="YOUTUBE VIDEO DOWNLOADER",  font=("Century Gothic",25)).grid(row=0, column=1, padx=10, pady=10)
urlLabel        = Label(root,   text="URL",                 font=("Century Gothic",15)).grid(row=1, column=0, padx=10, pady=10)
qualityLabel    = Label(root,   text="SELECT QUALITY",      font=("Century Gothic",15)).grid(row=2, column=0, padx=10, pady=10)
locLabel        = Label(root,   text="LOCATION",            font=("Century Gothic",15)).grid(row=3, column=0, padx=10, pady=10)

#Get Input
getURL = StringVar()
getLoc = StringVar()

#Set Entry
urlEntry    = Entry(root,   font=("Century Gothic",12), textvariable = getURL, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=1,column=1, padx=10, pady=10)
locEntry    = Entry(root,   font=("Century Gothic",12), textvariable = getLoc, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=3,column=1, padx=10, pady=10)

#List box for video Quality
listbox     = Listbox(root, font=("Century Gothic",11), width = 56, height = 12, bd=3, relief=SOLID, borderwidth=1)
listbox.grid(row=2,column=1, padx=10, pady=10)

#Set Buttons
urlButton       = Button(root, text = "SET URL",    font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=setURL).grid(row=1, column=2, padx=10, pady=10)
browseButton    = Button(root, text = "BROWSE",     font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=clickBrowse).grid(row=3, column=2, padx=10, pady=10)
downloadButton  = Button(root, text = "DOWNLOAD",   font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=clickDownload).grid(row=4, column=1, padx=10, pady=10)
resetButton     = Button(root, text = "CLEAR ALL",  font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=clickReset).grid(row=4, column=2, padx=10, pady=10)


#Set an infinite loop so window stays in view
root.mainloop()
