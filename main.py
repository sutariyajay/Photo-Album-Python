import tkinter
from PIL import Image, ImageTk
import os


root = tkinter.Tk()
root.geometry("%dx%d+0+0"%(root.winfo_screenwidth(),root.winfo_screenheight()))

os.chdir("E://Jay//New folder")#directory path
images=os.listdir()

#Importing Photos
image_list = [img for img in images]
current = 0

def move(Rd):
    global current, image_list
    if not (0 <= current + Rd < len(image_list)):
        return
    current += Rd
    image = Image.open(image_list[current])
    images=image.resize((500,500),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(images)

    label['image'] = photo
    label.photo = photo




label = tkinter.Label(root, compound=tkinter.TOP)
label.pack()

frame = tkinter.Frame(root)
frame.pack()

tkinter.Button(frame, text='Previous', command=lambda: move(-1)).pack(side=tkinter.LEFT)
tkinter.Button(frame, text='Next', command=lambda: move(+1)).pack(side=tkinter.LEFT)


move(0)

root.mainloop()
