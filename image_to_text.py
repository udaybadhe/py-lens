import tkinter as tk
from tkinter import PhotoImage, Canvas, Text
from PIL import Image
import os
import sys
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:/tes/tesseract.exe'
window = tk.Tk()
canvas = Canvas(window)
canvas.pack()
# Load the image file and add it to the canvas
image = PhotoImage(file=sys.argv[1])
canvas.create_image(0, 0, image=image, anchor='nw')

# Create a Text widget and add it to the window
text = Text(window)
text.pack()

# Perform OCR on the image and extract the text
# os.system('tesseract {} buffer'.format(sys.argv[1]))
test = pytesseract.image_to_string(sys.argv[1])
# text_string = open('buffer.txt','r').read()

# Set the text of the Text widget to the extracted text
text.insert('1.0', test)

# Run the Tkinter event loop
window.mainloop()

