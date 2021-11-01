from PIL import Image as img
import numpy as np
import tkinter as tk
from tkinter import filedialog
# temp variable to store the decoded data
decodedData = ''
# initiate tkinter
root = tk.Tk()
# hide root window
root.withdraw()
# ask for file name, with a dialog box
filePath = filedialog.askopenfilename()
# open image with previously given file path
dcode = img.open(fr"{filePath}")
# convert image into array
dcodeArray = np.array(dcode)
# flattens (2d to 1d) array
decode = dcodeArray.flatten()
# converts all multiples of 5 into 1, and the rest as 0.
bin = np.where(decode % 5 == 0, 1, 0)
# processes in groups of 7 (a byte)
for i in range(0, len(bin), 7):
    # temp variable to store data
    temp = ''
    # from i to i+7, decode the byte into ascii
    for i2 in bin[i:i + 7]:
        # array values stored in str because there's no seperations
        temp += str(i2)
    # converts temp (7 bits/1 byte) from base 2 to base 10, then to ascii.
    decodedData += chr(int(str(temp), 2))
# prints result
print(decodedData)
