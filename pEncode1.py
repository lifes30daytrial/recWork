from PIL import Image as img
import tkinter as tk
from tkinter import filedialog
import numpy as np
# x represents the index of the encode[] array
x = -1
# initiates tkinter
root = tk.Tk()
# hides root window
root.withdraw()
# ask for file path via dialog box
filePath = filedialog.askopenfilename()
# open file from given file path
ncrypt = img.open(fr"{filePath}")
# open image for user
ncrypt.show()
# assign width and height from image as a variable
width, height = ncrypt.size
# convert img to array
ncryptArray = np.array(ncrypt)
# recieve input text
userInput = input("Put encoded text here: ")
# converts user input to binary
binUI = ''.join(format(ord(x), '07b') for x in userInput)
# stops program if text entered is too much for given image
if len(binUI) > int(ncryptArray.size):
    print("Text value too large for image.")
    sys.stop()
# flattens array (2d to 1d)
encrypt = ncryptArray.flatten()
# any value lower than 5 will become 6
encrypt = np.where(encrypt < 5, 6, encrypt)
# remove any multiples of 5
encrypt = np.where(encrypt % 5 == 0, abs(encrypt - 1), encrypt)
# for every number in binUI, this loop is repeated
for i in binUI:
    # increase index value by one each time, starting from -1
    x += 1
    # if the bit in binUI is 1:
    if int(i) == 1:
        # if it is already a multiple of five (which it shouldn't be):
        if encrypt[x] % 5 == 0:
            # debug: print out the value, which should be impossible
            print(f"something went wrong at index {x}, with value {encrypt[x]}")
        else:
            # turn encrypt[x] into a multiple of 5
            encrypt[x] = abs(encrypt[x] - (encrypt[x] % 5))
# gets image from array encrypt[] and reshapes encrypt to the height,
# width, and colour channels (from len(ncrypt.getbands()), which gets
# how many colour channels were in the image.
product = img.fromarray(encrypt.reshape((height, width, len(ncrypt.getbands()))))
# open savefile dialog with the default extension being .png
f = filedialog.asksaveasfile(defaultextension='.png')
# saves the file with the file path and name from the file dialog
product.save(f.name)
