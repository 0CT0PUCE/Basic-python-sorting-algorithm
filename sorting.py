import os, shutil
import tkinter as tk
from tkinter import *

directorya = r"path/to/png"
dirpng = r"path/to/Photo"
dirmp4 = r"path/to/video"
direv3 = r"path/to/EV3"
dirlego = r"path/to/lego_digital_designer"
dirmc = r"path/to/Minecraft"
dirmus = r"path/to/Music"
dirscra = r"path/to/Scratch"
bin = r"path/to/bin"
dirmkv = r"path/to/Film"
dirdoc = r"path/to/cours"
dirzip = r"path/to/Zip"
direxe = r"path/to/Computer_stuff"
dirpy = r"path/to/python"

moved = 0
deleted = 0

window = tk.Tk()
window.title("Sorting Program")
window.geometry('800x50')
lbl = Label(window, text="Directory to sort:")
lbl.grid(column=0, row=0)
txt = Entry(window,width=100)
txt.grid(column=1, row=0)
txt.pack
log1 = Label(window, text="Log :")
log1.grid(column=0, row=1)
log = Label(window, text="test", bg='white',fg='black')
log.grid(column=1, row=1)
directorya = txt.get()

def sort():
    directorya = txt.get()
    lbl = Label(window, text="Votre vidéo :" + txt.get() + "")
    txt.delete(0, END)
    folders = [folder for folder in os.listdir(directorya) if os.path.isdir(os.path.join(directorya, folder))]
    files = [file for file in os.listdir(directorya) if os.path.isfile(os.path.join(directorya, file))]
    moved = 0
    deleted = 0
    for file in files:
        try:
            if os.path.splitext(file)[1] == ".png" or os.path.splitext(file)[1] == ".jpg" or os.path.splitext(file)[1] == ".PNG" or os.path.splitext(file)[1] == ".JPG" or os.path.splitext(file)[1] == ".jpeg" or os.path.splitext(file)[1] == ".webp" or os.path.splitext(file)[1] == ".dng":
                if not os.path.exists(os.path.join(dirpng, file)):
                    print(file,"is png")
                    shutil.move(os.path.join(directorya, file), dirpng)
                    moved=moved+1
                else :
                    print(file, "is moving to bin")
                    shutil.move(os.path.join(directorya, file), bin)
                    deleted=deleted+1
            if os.path.splitext(file)[1] == ".mp4" or os.path.splitext(file)[1] == ".AVI" or os.path.splitext(file)[1] == ".gif":
                if not os.path.exists(os.path.join(dirmp4, file)):
                    print(file,"is mp4")
                    shutil.move(os.path.join(directorya, file), dirmp4)
                    moved=moved+1
                else :
                    print(file, "is moving to bin")
                    shutil.move(os.path.join(directorya, file), bin)
                    deleted=deleted+1
            if os.path.splitext(file)[1] == ".ev3":
                if not os.path.exists(os.path.join(direv3, file)):
                    print(file,"is EV3")
                    shutil.move(os.path.join(directorya, file), direv3)
                    moved=moved+1
                else :
                    print(file, "is moving to bin")
                    shutil.move(os.path.join(directorya, file), bin)
                    deleted=deleted+1
            if os.path.splitext(file)[1] == ".lxf" or os.path.splitext(file)[1] == ".io":
                if not os.path.exists(os.path.join(dirlego, file)):
                    print(file,"is lego")
                    shutil.move(os.path.join(directorya, file), dirlego)
                    moved=moved+1
                else :
                    print(file, "is moving to bin")
                    shutil.move(os.path.join(directorya, file), bin)
                    deleted=deleted+1
            if os.path.splitext(file)[1] == ".mcworld" or os.path.splitext(file)[1] == ".mcpack":
                if not os.path.exists(os.path.join(dirmc, file)):
                    print(file,"is minecraft")
                    shutil.move(os.path.join(directorya, file), dirmc)
                    moved=moved+1
                else :
                    print(file, "is moving to bin")
                    shutil.move(os.path.join(directorya, file), bin)
                    deleted=deleted+1
            if os.path.splitext(file)[1] == ".mp3":
                if not os.path.exists(os.path.join(dirmus, file)):
                    print(file,"is mp3")
                    shutil.move(os.path.join(directorya, file), dirmus)
                    moved=moved+1
                else :
                    print(file, "is moving to bin")
                    shutil.move(os.path.join(directorya, file), bin)
                    deleted=deleted+1
            if os.path.splitext(file)[1] == ".sb2":
                if not os.path.exists(os.path.join(dirscra, file)):
                    print(file,"is sb2")
                    shutil.move(os.path.join(directorya, file), dirscra)
                    moved=moved+1
                else :
                    print(file, "is moving to bin")
                    shutil.move(os.path.join(directorya, file), bin)
                    deleted=deleted+1
            if os.path.splitext(file)[1] == ".mkv" or os.path.splitext(file)[1] == ".mts":
                if not os.path.exists(os.path.join(dirmkv, file)):
                    print(file,"is mkv")
                    shutil.move(os.path.join(directorya, file), dirmkv)
                    moved=moved+1
                else :
                    print(file, "is moving to bin")
                    shutil.move(os.path.join(directorya, file), bin)
                    deleted=deleted+1
            if os.path.splitext(file)[1] == ".doc" or os.path.splitext(file)[1] == ".pdf" or os.path.splitext(file)[1] == ".odt" or os.path.splitext(file)[1] == ".odp":
                if not os.path.exists(os.path.join(dirdoc, file)):
                    print(file,"is doc")
                    shutil.move(os.path.join(directorya, file), dirdoc)
                    moved=moved+1
                else :
                    print(file, "is moving to bin")
                    shutil.move(os.path.join(directorya, file), bin)
                    deleted=deleted+1
            if os.path.splitext(file)[1] == ".zip" or os.path.splitext(file)[1] == ".gz" or os.path.splitext(file)[1] == ".tar":
                if not os.path.exists(os.path.join(dirzip, file)):
                    print(file,"is zip")
                    shutil.move(os.path.join(directorya, file), dirzip)
                    moved=moved+1
                else :
                    print(file, "is moving to bin")
                    shutil.move(os.path.join(directorya, file), bin)
                    deleted=deleted+1
            if os.path.splitext(file)[1] == ".exe" or os.path.splitext(file)[1] == ".html" or os.path.splitext(file)[1] == ".css":
                if not os.path.exists(os.path.join(direxe, file)):
                    print(file,"is exe")
                    shutil.move(os.path.join(directorya, file), direxe)
                    moved=moved+1
                else :
                    print(file, "is moving to bin")
                    shutil.move(os.path.join(directorya, file), bin)
                    deleted=deleted+1
            if os.path.splitext(file)[1] == ".THM" or os.path.splitext(file)[1] == ".nes" or os.path.splitext(file)[1] == ".sfc":
                print(file, "is moving to bin")
                shutil.move(os.path.join(directorya, file), bin)
                deleted=deleted+1
            if os.path.splitext(file)[1] == ".py" or os.path.splitext(file)[1] == ".whl":
                if not os.path.exists(os.path.join(dirpy, file)):
                    print(file,"is py")
                    shutil.move(os.path.join(directorya, file), dirpy)
                    moved=moved+1
                else :
                    print(file, "is moving to bin")
                    shutil.move(os.path.join(directorya, file), bin)
                    deleted=deleted+1
        except:
            print("restarting script because of an error")
            print(exception)

    print("moved",moved,"files and deleted",deleted,"files in the directory :", directorya)
    final = "moved",moved,"files and deleted",deleted,"files in the directory :", directorya
    log.config(text=final)
    os.path

btn = Button(window, text="Sort", command=sort, bg='black',fg='white')
btn.grid(column=2, row=0)
window.mainloop()
