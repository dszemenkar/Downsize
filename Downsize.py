import sys
from Tkinter import *
import os
from PIL import Image
resize_method = Image.ANTIALIAS
    #Image.NEAREST)  # use nearest neighbour
    #Image.BILINEAR) # linear interpolation in a 2x2 environment
    #Image.BICUBIC) # cubic spline interpolation in a 4x4 environment
    #Image.ANTIALIAS) # best down-sizing filter

window = Tk()
window.title("Downsize")

l1 = Label(window, text = "Height")
l1.grid(row = 0, column = 0)
l2 = Label(window, text = "Width")
l2.grid(row = 0, column = 2)

heightInput = IntVar()
e1 = Entry(window, textvariable = heightInput)
e1.grid(row = 0, column = 1)
widthInput = IntVar()
e2 = Entry(window, textvariable = widthInput)
e2.grid(row = 0, column = 3)

extensions= ['JPG']
path= os.path.abspath(".")

def adjusted_size(width,height):
    max_height = e1.get()
    max_width = e2.get()
    if width>max_width or height>max_height:
        if width>height:
            return max_width, int (max_width * height/ width)
        else:
            return int (max_height*width/height), max_height
    else:
        return width,height


def run():
    if __name__ == "__main__":
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path,f)):
                f_text, f_ext= os.path.splitext(f)
                f_ext= f_ext[1:].upper()
                if f_ext in extensions:
                    print f
                    image = Image.open(os.path.join(path,f))
                    width, height= image.size
                    image = image.resize(adjusted_size(width, height))
                    image.save(os.path.join(path,f))

b1 = Button(window, text = "Convert!", width = 12, command=run)
b1.grid(row = 1, column = 1)
b1 = Button(window, text = "Exit", width = 12, command=window.destroy)
b1.grid(row = 1, column = 3)

window.mainloop()
