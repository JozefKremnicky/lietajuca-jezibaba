import tkinter
import random

canvas = tkinter.Canvas(width=1000,height=500)
canvas.pack()

def striga():
    global x,y
    global x1,y1
    speed1 = random.randint(0,11)
    speed2 = random.randint(0,11)
    first = 0
    canvas.delete('all')

    canvas.create_line(x-30,y,x+30,y,width=3)
    canvas.create_line(x-40,y-20,x-30,y,width=2)
    canvas.create_line(x-40,y-15,x-30,y,width=2)
    canvas.create_line(x-40,y-10,x-30,y,width=2)
    canvas.create_line(x-40,y-5,x-30,y,width=2)
    canvas.create_line(x-40,y-0,x-30,y,width=2)
    canvas.create_line(x-40,y+5,x-30,y,width=2)
    canvas.create_line(x-40,y+10,x-30,y,width=2)
    canvas.create_line(x-40,y+15,x-30,y,width=2)
    canvas.create_line(x-40,y+20,x-30,y,width=2)
    canvas.create_rectangle(x-5,y-15,x+5,y+10,width=2)
    canvas.create_oval(x-5,y-25,x+5,y-15,width=2)

    canvas.create_line(x1-30,y1,x1+30,y1,width=3,fill='brown')
    canvas.create_line(x1-40,y1-20,x1-30,y1,width=2,fill='brown')
    canvas.create_line(x1-40,y1-15,x1-30,y1,width=2,fill='brown')
    canvas.create_line(x1-40,y1-10,x1-30,y1,width=2,fill='brown')
    canvas.create_line(x1-40,y1-5,x1-30,y1,width=2,fill='brown')
    canvas.create_line(x1-40,y1-0,x1-30,y1,width=2,fill='brown')
    canvas.create_line(x1-40,y1+5,x1-30,y1,width=2,fill='brown')
    canvas.create_line(x1-40,y1+10,x1-30,y1,width=2,fill='brown')
    canvas.create_line(x1-40,y1+15,x1-30,y1,width=2,fill='brown')
    canvas.create_line(x1-40,y1+20,x1-30,y1,width=2,fill='brown')
    canvas.create_rectangle(x1-5,y1-15,x1+5,y1+10,width=2,fill='red')
    canvas.create_oval(x1-5,y1-25,x1+5,y1-15,width=2,fill='red')

    y = y + speed1
    y1 = y1 + speed2

    

    if y > 500:
        first += 1   
    if y1 > 500:
        first -= 1
    
    if go == 1:
        canvas.after(100, striga)
    if first == 1:
        canvas.create_text(500,200,text='ČIERNA',font='Ariel 20')
    if first == -1:
        canvas.create_text(500,200,text='ČERVENÁ',fill='red',font='Ariel 20')

        

go = 1
x = 200
y = 100
x1 = 600
y1 = 100
striga()
