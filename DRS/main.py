# All media file is available for download as a zip file (See description)
import tkinter 
import cv2  # pip install opencv-python
import PIL.Image,PIL.ImageTk  # pip install pillow
from functools import partial
import threading
import time


# Set the main scrien hight and width
SET_WIDTH = 720
SET_HEIGHT = 550

# Tkinter gui start here

window = tkinter.Tk()
window.title("Himadri's DRS system")
cv_img = cv2.cvtColor(cv2.imread("himadri.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(cv_img))
window.mainloop()