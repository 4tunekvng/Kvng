from tkinter import Canvas, Tk
from tkinter import *
import utilities
import random
import math

def make_creature(canvas, center, size=100, tag='creature', fill='hotpink'):
    # just a demo of how you might think about making your creature:
    left_eye_pos = (center[0] - size / 4, center[1] - size / 5)
    right_eye_pos = (center[0] + size / 4, center[1] - size / 5)
    eye_width = eye_height = size / 10
    utilities.make_circle(canvas, center, size, color=fill, tag=tag)
    utilities.make_oval(canvas, left_eye_pos, eye_width, eye_height, color='black', tag=tag)
    utilities.make_oval(canvas, right_eye_pos, eye_width ,eye_height, color='black', tag=tag)
    utilities.make_line(canvas, [
        (center[0] - size / 2, center[1] + size / 3), 
        (center[0], center[1] + size / 1.2), 
        (center[0] + size / 2, center[1] + size / 3)
    ], curvy=True)
def make_face(canvas: Canvas, center: tuple, width: int, fill: str="#D8A47F",tag='face'):
    make_circle(canvas, center, width/2, fill,tag)
    make_oval(canvas, (center[0]-width/6, center[1]-width/8), width/16, width/12, "black",tag)
    make_oval(canvas, (center[0]+width/6, center[1]-width/8), width/16, width/12, "black",tag)
def make_creaturetwo(canvas: Canvas, center=tuple, width=float, fill_face:str="#D8A47F", fill_ear:str="#402E2A", tag="creaturetwo"):
    make_face(canvas, center, width, fill_face,tag)
    make_circle(canvas,(center[0]+(width/2.5),center[1]-(width/2)),width/3.5,fill_ear,tag)
    make_circle(canvas,(center[0]-(width/2.5),center[1]-(width/2)),width/3.5,fill_ear,tag)
    make_oval(canvas,(center[0],(width/10)+center[1]),width/5,width/14,fill_ear,tag)
stuff=[]
def make_turtle(canvas, center, size=100, tag="turtle", fill="green"):
    tag = 'turtle_' + str(len(stuff))
    eye_width = eye_height = size /15
    utilities.make_oval(canvas,center,size/1.5,size,color="brown",tag=tag)
    utilities.make_circle(canvas, (center[0]-(0.73*size),center[1]- size/2.5),size/4.5, color=fill, tag=tag)
    utilities.make_circle(canvas, (center[0]+(0.73*size),center[1]- size/2.5),size/4.5, color=fill, tag=tag)
    utilities.make_circle(canvas, (center[0]-(0.73*size),center[1]+ size/2.5),size/4.5, color=fill, tag=tag)
    utilities.make_circle(canvas, (center[0]+(0.73*size),center[1]+ size/2.5),size/4.5, color=fill, tag=tag)
    utilities.make_circle(canvas, (center[0],center[1]-size),size/4, color=fill, tag=tag)
    utilities.make_oval(canvas, (center[0]-size/4,center[1]-size), eye_width, eye_height, color='black', tag=tag)
    utilities.make_oval(canvas, (center[0]+size/4,center[1]-size), eye_width, eye_height, color='black', tag=tag)
    stuff.append({
        'tag': tag,
        'speed': random.uniform(1, 5)
    })








    
def make_petal(canvas, center, size=100,angle=60,tag="petal", fill="yellow"):
    canvas.create_line(center[0]-size*math.cos(angle), center[1]-size*math.sin(angle),
        center[0]+(size/2)*math.cos(90-angle), center[1]-(size/2)*math.sin(90-angle),
        center[0]+size*math.cos(angle),center[1]+size*math.sin(angle),
        smooth=True
        )
    canvas.create_line(center[0]-size*math.cos(angle), center[1]-size*math.sin(angle),
        center[0]-(size/2)*math.cos(90-angle), center[1]+(size/2)*math.sin(90-angle),
        center[0]+size*math.cos(angle),center[1]+size*math.sin(angle),
        smooth=True
        )

def make_flower(canvas,center,size=100,tag="flower",fill="yellow"):
    for i in range(0,360,30):
        make_petal(canvas, center,size,angle=i)
    utilities.make_circle(canvas,center,size/4,color="brown", tag=tag)
def moving_circle_right(canvas,initial_center: tuple, size, fill="green", tag="leafyright"):
    utilities.make_circle(canvas, initial_center,size, color=fill, tag=tag)
    utilities.make_circle(canvas, (initial_center[0]+size*1.414,initial_center[1]-size*1.414),size,color=fill)
    utilities.make_circle(canvas, (initial_center[0]+size*1.414*2,initial_center[1]-size*1.414*2),size,color=fill)
    utilities.make_circle(canvas, (initial_center[0]+size*1.414*3,initial_center[1]-size*1.414*3),size,color=fill)
    utilities.make_circle(canvas, (initial_center[0]+size*1.414*4,initial_center[1]-size*1.414*4),size,color=fill)
    utilities.make_circle(canvas, (initial_center[0]+size*1.414*5,initial_center[1]-size*1.414*5),size,color=fill)
def moving_circle_left(canvas,initial_center:tuple, size, fill="green", tag="leafyleft"):
    utilities.make_circle(canvas, initial_center,size, color=fill, tag=tag)
    utilities.make_circle(canvas, (initial_center[0]-size*1.414,initial_center[1]-size*1.414),size,color=fill)
    utilities.make_circle(canvas, (initial_center[0]-size*1.414*2,initial_center[1]-size*1.414*2),size,color=fill)
    utilities.make_circle(canvas, (initial_center[0]-size*1.414*3,initial_center[1]-size*1.414*3),size,color=fill)
    utilities.make_circle(canvas, (initial_center[0]-size*1.414*4,initial_center[1]-size*1.414*4),size,color=fill)
    utilities.make_circle(canvas, (initial_center[0]-size*1.414*5,initial_center[1]-size*1.414*5),size,color=fill)



def make_leaf(canvas, center, size=100, tag="leaf", fill="green"):
    make_rectangle(canvas, (center[0]-size/10,center[1]+size/2), size/5, size, color=fill, tag=tag)
    




def make_landscape_object(canvas, position, size=100):
    # your code to create your creature goes here:
    # replace the code below...
    print('make_landscape_object...')
    print('size:', size, 'center:', position) 


def _get_coordinates(canvas, id):
    return canvas.coords(id)

def _set_coordinates(canvas, id, coordinates):
    canvas.coords(id, coordinates)

def _update_position_by_id(canvas, id, x=2, y=0):
    coords = _get_coordinates(canvas, id)
    # update coordinates:
    for i in range(0, len(coords)):
        if i % 2 == 0:
            coords[i] += x
        else:
            coords[i] += y
    # set the coordinates:
    _set_coordinates(canvas, id, coords)

def _get_x_coordinates(canvas, tag):
    return _get_coordinates_by_dimension(canvas, tag, dimension='x')

def _get_y_coordinates(canvas, tag):
    return _get_coordinates_by_dimension(canvas, tag, dimension='y')

def make_circle(canvas, center, radius, color='#FF4136', tag=None, stroke_width=2, outline=None):
    make_oval(
        canvas, center, radius, radius, color=color, tag=tag,
        stroke_width=stroke_width, outline=outline
    )

def make_oval(canvas, center, radius_x, radius_y, color='#FF4136', tag=None, stroke_width=1, outline=None):
    x, y = center
    return canvas.create_oval(
        [ x - radius_x, y - radius_y, x + radius_x, y + radius_y ],
        fill=color,
        width=stroke_width,
        tags=tag,
        outline=outline
    )

def make_rectangle(canvas, top_left, width, height, color="#3D9970", tag=None):
    x, y = top_left
    return canvas.create_rectangle(
        [(x, y), (x + width, y + height)], 
        fill=color, 
        width=0,
        tags=tag
    )
    
def _get_coordinates_by_dimension(canvas, tag, dimension='x'):
    '''
    updates the x and y position of all shapes that have been tagged
    with the tag argument
    '''
    if dimension == 'x':
        pos = 0
    else:
        pos = 1
    shape_ids = canvas.find_withtag(tag)
    coords = []
    for id in shape_ids:
        shape_coords = _get_coordinates(canvas, id)
        for i in range(0, len(shape_coords)):
            if i % 2 == pos:
                coords.append(shape_coords[i])
    return coords

def update_position(canvas, tag, x=2, y=0):
    '''
    updates the x and y position of all shapes that have been tagged
    with the tag argument
    '''
    shape_ids = canvas.find_withtag(tag)
    for id in shape_ids:
        _update_position_by_id(canvas, id, x, y)

def get_left(canvas, tag):
    '''
    returns the left boundary of the shape group
    '''
    return min(*_get_x_coordinates(canvas, tag))

def get_right(canvas, tag):
    '''
    returns the right boundary of the shape group
    '''
    return max(*_get_x_coordinates(canvas, tag))

def get_top(canvas, tag):
    '''
    returns the top boundary of the shape group
    '''
    return min(*_get_y_coordinates(canvas, tag))

def get_bottom(canvas, tag):
    '''
    returns the bottom boundary of the shape group
    '''
    return max(*_get_y_coordinates(canvas, tag))

def get_width(canvas, tag):
    '''
    returns the width of the shape group
    '''
    x_coords = _get_x_coordinates(canvas, tag)
    return max(*x_coords) - min(*x_coords)

def get_height(canvas, tag):
    '''
    returns the height of the shape group
    '''
    y_coords = _get_y_coordinates(canvas, tag)
    return max(*y_coords) - min(*y_coords)

def make_car(canvas, top_left=(0, 0), color="#3D9970", tag=None):
    '''
    demo function that show you how to draw a car, given the convenience
    functions that are available in this module
    '''
    a, b = top_left
    make_rectangle(canvas, (a + 50, b), 100, 40, color=color, tag=tag)
    make_rectangle(canvas, (a, b + 30), 200, 45, color=color, tag=tag)
    make_circle(canvas, (a + 50, b + 80), 20, color='black', tag=tag)
    make_circle(canvas, (a + 150, b + 80), 20, color='black', tag=tag)

def make_star(canvas, center, diameter):
    '''
    demo function that show you how to draw a star, given the convenience
    functions that are available in this module
    '''
    make_circle(
        canvas,
        center,
        diameter / 2,
        stroke_width=0,
        outline='white',
        color=random.choice(["purple","blue","orange", "yellow"])
    )

def make_bubble(canvas, center, diameter):
    '''
    demo function that show you how to draw a bubble, given the convenience
    functions that are available in this module
    '''
    make_circle(
        canvas,
        center,
        diameter / 2,
        stroke_width=1,
        outline='white',
        color=None
    )