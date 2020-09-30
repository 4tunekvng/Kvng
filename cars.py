from tkinter import Canvas, Tk
import time
import helpers

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# draw car (and give it a unique tag 'car1')
def cars_drive():
    a=0
    helpers.make_car(canvas, top_left=(a-250, 50), tag='car1')
    helpers.make_car(canvas, top_left=(a+550, 300), tag='car2')
    while a==a: 
        a =0
        while a<900:
            time.sleep(0.2)
            helpers.update_position(canvas, 'car1', x=50, y=0)
            helpers.update_position(canvas, 'car2', x=-50, y=0)
            gui.update()
            a=a+50
        a=850
        while a<900:
            time.sleep(0.2)
            helpers.update_position(canvas, 'car1', x=-50, y=0)
            helpers.update_position(canvas, 'car2', x=50, y=0)
            gui.update()
            a=a-50

        

cars_drive()

    
# move shapes that have the tag 'car1' 50 pixels to the right:

# move shapes that have the tag 'car1' 50 pixels to the right (exact same code):


# move shapes that have the tag 'car1' 50 pixels to the right (exact same code):











########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()