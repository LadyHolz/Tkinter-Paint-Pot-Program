import tkinter

#explaining the game instructions
print("To draw, hold down the left mouse button and move your mouse around.")
print("To change your brush colour, click on one of the colours.")

#import paint pot window and choose the canvas size
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=750, height=500, bg="white")
canvas.pack()

#create coordinates
lastX, lastY = 0,0
colour = "black"

#create function to track mouse pointer
def store_position(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y

#creat function to tell the computer what to do when you click the canvas
def on_click(event):
    store_position(event)

#create function to tell the computer to draw when the mouse moves across the canvas    
def on_drag(event):
    canvas.create_line(lastX, lastY, event.x, event.y, fill = colour, width = 3)
    store_position(event)
#contect the functions    
canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)


#to draw using diffenet colour add a colour pallete of clickable square
red_id = canvas.create_rectangle(10, 10, 30, 30, fill="red")
blue_id = canvas.create_rectangle(10, 35, 30, 55, fill="blue")
black_id = canvas.create_rectangle(10, 60, 30, 80, fill="black")
white_id = canvas.create_rectangle(10, 85, 30, 105, fill="white")

#function to change the paint colour by clicking on the pallete squares
def set_colour_red(event):
    global colour
    colour="red"
    
def set_colour_blue(event):
    global colour
    colour="blue"
    
def set_colour_black(event):
    global colour
    colour="black"
    
def set_colour_white(event):
    global colour
    colour="white"
#using tag_bing to to set the colours to the different squares    
canvas.tag_bind(red_id, "<Button-1>", set_colour_red)
canvas.tag_bind(blue_id, "<Button-1>", set_colour_blue)
canvas.tag_bind(black_id, "<Button-1>", set_colour_black)
canvas.tag_bind(white_id, "<Button-1>", set_colour_white)
#run the whole program
window.mainloop()