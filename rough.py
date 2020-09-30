from tkinter import Canvas, Tk
import utilities
import helper
import time
from PIL import ImageTk,Image
from tkinter import *
import random
gui = Tk()
gui.title('My Terrarium')

data=[]
MOUSE_DRAG = '<B1-Motion>'
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='blue')
canvas.pack()
helper.make_turtle(canvas,(750, 180), 100, tag="turtle")
def make_turtle_by_click(event):
    tag = 'turtle_' + str(len(data))
    helper.make_turtle(canvas, (event.x, event.y), random.choice(range(0,100)), tag=tag, fill="green")
    data.append({
        'tag': tag,
        'speed': random.uniform(1, 5)
    })
canvas.bind(MOUSE_DRAG, make_turtle_by_click)
for item in data:
    tag = item['tag']
    speed = -1* item['speed']
    if utilities.get_bottom(canvas, tag) < 0:
        reset_position = window_height + utilities.get_width(canvas, tag)
        utilities.update_position_by_tag(canvas, tag=tag, y=reset_position)   
    utilities.update_position_by_tag(canvas, tag=tag, x=0, y=speed)
gui.update()
time.sleep(0.002)
for item in data:
    tag = item["turtle"]
    speed = -1 * item['speed']
    if utilities.get_bottom(canvas, tag) < 0:
        reset_position = window_height + utilities.get_width(canvas, tag)
        utilities.update_position_by_tag(canvas, tag="turtle", y=reset_position)   
    utilities.update_position_by_tag(canvas, tag="turtle", x=0, y=speed)
gui.update()
time.sleep(0.002)
canvas.mainloop()