from tkinter import Canvas, Tk
import utilities
import helper
import time
from PIL import ImageTk,Image
from tkinter import *
import random
gui = Tk()
gui.title('My Terrarium')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='aqua') #sea colored background
canvas.pack()

image_path="C:\\Users\\King\\Downloads\\seabackground.jpg"
utilities.make_image(
        canvas,image_path, position=(0, 0), rotation=None, 
        size=(window_width*3,window_height*2), anchor='nw')

canvas.mainloop()