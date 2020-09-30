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
########################## YOUR CODE BELOW THIS LINE ##############################
MOUSE_CLICK = '<Button-1>' #left_click button
def make_rock(canvas, center, diameter):
    '''
    demo function that show you how to draw a rock, given the convenience
    functions that are available in this module
    '''
    helper.make_circle(
        canvas,
        center,
        diameter / 2,
        stroke_width=0,
        outline='white',
        color=random.choice(["purple","blue","orange", "yellow"])
    )
data=[]
for i in range(2000):
    make_rock(canvas, (random.uniform(0,window_width), 
    random.uniform(window_height*0.7, window_height)), 
    random.uniform(0,window_width/50))

def make_rock_from_click(event):
    make_rock(
        canvas,
        (event.x, event.y),
        random.uniform(0,window_width/50))

canvas.bind(MOUSE_CLICK, make_rock_from_click)
# sample code to make a creature:
helper.make_turtle(canvas,(750, 180), 100)
utilities.make_poly_oval(canvas, (800, window_height*0.7),100,80, color='brown', tag="big_rocks", stroke_width=1, outline=None)
helper.moving_circle_right(canvas,(100,500), 10, fill="green", tag="leafyright1")
helper.moving_circle_left(canvas,(100,500), 10, fill="green", tag="leafyright2")
helper.moving_circle_right(canvas,(300,500), 10, fill="green", tag="leafyright3")
helper.moving_circle_left(canvas,(300,500), 10, fill="green", tag="leafyright4")
helper.moving_circle_right(canvas,(800,500), 10, fill="green", tag="leafyright3")
helper.moving_circle_left(canvas,(800,500), 10, fill="green", tag="leafyright4")
helper.make_petal(canvas,(200, 300),30,angle=60,tag="petal", fill="yellow")

#make turtle by click
MOUSE_DRAG = '<B1-Motion>'
MOUSE_CLICK = '<Button-1>'
data = []
def make_turtle_by_click(event):
    tag = 'turtle_' + str(len(data))
    helper.make_turtle(canvas, (event.x, event.y), random.choice(range(0,100)), tag=tag, fill="green")
    data.append({
        'tag': tag,
        'speed': random.uniform(1, 5)
    })
canvas.bind(MOUSE_DRAG, make_turtle_by_click)



helper.make_creaturetwo(canvas,(75,75), 175, "#56E8C2","#FFD95E",tag="second")
helper.make_creaturetwo(
   canvas, (454, 423),141, '#aebb83', '#227876',tag="third")
helper.make_creaturetwo(
   canvas, (333, 227),99, '#94ba77', '#3f5364', tag="fourth")
helper.make_creaturetwo(
   canvas, (117, 314), 91, '#648d8e', '#afc272',tag="fifth")
helper.make_creaturetwo(canvas, (199, 469), 122, '#3f5364', '#bfdc65', tag="sixth")
def update_creature():
    helper.make_creaturetwo(canvas, (200,200), 120, "#FFD95E","#402E2A",tag="first")
    gui.update()
    time.sleep(3)
    utilities.update_fill_by_tag(canvas, 'first', color = 'yellow')
update_creature()
helper.make_flower(canvas,(360, 400),50,fill="yellow",tag="c1")
helper.make_flower(canvas,(450,250),50,fill="yellow",tag="c2")
helper.make_flower(canvas,(233,456),50,fill="yellow",tag="c3")
helper.make_flower(canvas,(129,400),50,fill="yellow",tag="c4")
helper.make_flower(canvas,(860,250),50,fill="yellow",tag="c5")
helper.make_flower(canvas,(950,456),50,fill="yellow",tag="c6")
helper.make_flower(canvas,(733,900),50,fill="yellow",tag="c7")
#make turtle swim
a = 0
while True:
    gui.update()
    print(data)
    utilities.rotate(canvas, 'c1', degrees=1, origin=(150, 150))
    utilities.rotate(canvas, 'c2', degrees=1, origin=(150, 150))
    utilities.rotate(canvas, 'c3', degrees=1, origin=(150, 150))
    utilities.rotate(canvas, 'c4', degrees=1, origin=(150, 150))
    utilities.rotate(canvas, 'c5', degrees=1, origin=(150, 150))
    utilities.rotate(canvas, 'c6', degrees=1, origin=(150, 150))
    utilities.rotate(canvas, 'c7', degrees=1, origin=(150, 150))
    gui.update()
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
        tag = item['tag']
        speed = -1 * item['speed']
        if utilities.get_bottom(canvas, tag) < 0:
            reset_position = window_height + utilities.get_width(canvas, tag)
            utilities.update_position_by_tag(canvas, tag=tag, y=reset_position)   
        utilities.update_position_by_tag(canvas, tag=tag, x=0, y=speed)
    gui.update()
    time.sleep(0.002)
    k = 1
    time.sleep(0.2)
    helper.update_position(canvas, 'first', x= k * 50, y=0)
    helper.update_position(canvas, 'second', x=k * -50, y=0)
    helper.update_position(canvas, 'third', x=k * 50, y=0)
    helper.update_position(canvas, 'fourth', x=k * -50, y=0)
    helper.update_position(canvas, 'fifth', x=k * 50, y=0)
    helper.update_position(canvas, 'sixth', x=k * -50, y=0)
    gui.update()
    
            

    # print(data)
    
    
    
    


        
########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()