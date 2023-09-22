import tkinter as tk

master = tk.Tk()

WIDTH = 500
HEIGHT = 500

canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT)
canvas.pack()


x0 = WIDTH / 2
y0 = HEIGHT / 2
edge = 50
step = 5

blue = canvas.create_rectangle(
    x0-edge, y0-edge, x0, y0, fill='blue', outline='white')
red = canvas.create_rectangle(
    x0, y0-edge, x0+edge, y0, fill='red', outline='white')
yellow = canvas.create_rectangle(
    x0-edge, y0, x0, y0+edge, fill='yellow', outline='white')
green = canvas.create_rectangle(
    x0, y0, x0+edge, y0+edge, fill='green', outline='white')

backwards = False


def redraw():
    global step, backwards

    canvas.after(50, redraw)

    if backwards:
        canvas.move(blue, step, step)
        canvas.move(red, -step, step)
        canvas.move(yellow, step, -step)
        canvas.move(green, -step, -step)
        if canvas.coords(blue)[2] >= x0:
            backwards = False
    else:
        canvas.move(blue, -step, -step)
        canvas.move(red, step, -step)
        canvas.move(yellow, -step, step)
        canvas.move(green, step, step)
        if canvas.coords(blue)[0] <= 0:
            backwards = True

redraw()

master.mainloop()
