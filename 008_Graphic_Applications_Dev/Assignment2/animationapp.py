import tkinter as tk


class AnimationApp(tk.Tk):
    WIDTH = 500
    HEIGHT = 500

    def __init__(self, edge = 50, step = 5):
        super().__init__()
        self.title('ANESCU - Graphic Applications Development - Assignment 2')
        self.x0 = AnimationApp.WIDTH / 2
        self.y0 = AnimationApp.HEIGHT / 2
        self.edge = edge
        self.step = step
        self.backwards = False

        self.canvas = tk.Canvas(self, width=AnimationApp.WIDTH, height=AnimationApp.HEIGHT)
        self.canvas.pack()

        self.blue = self.canvas.create_rectangle(
            self.x0-self.edge,self.y0-self.edge, 
            self.x0, self.y0, 
            fill='blue', outline='white')
        self.red = self.canvas.create_rectangle(
            self.x0, self.y0-self.edge, 
            self.x0+self.edge, self.y0, 
            fill='red', outline='white')
        self.yellow = self.canvas.create_rectangle(
            self.x0-self.edge, self.y0, 
            self.x0, self.y0+self.edge, 
            fill='yellow', outline='white')
        self.green = self.canvas.create_rectangle(
            self.x0, self.y0, 
            self.x0+edge, self.y0+edge, 
            fill='green', outline='white')
        self.start()
    def start(self):
        self.canvas.after(50, self.start)
        if self.backwards:
            self.canvas.move(self.blue, self.step, self.step)
            self.canvas.move(self.red, -self.step, self.step)
            self.canvas.move(self.yellow, self.step, -self.step)
            self.canvas.move(self.green, -self.step, -self.step)
            if self.canvas.coords(self.blue)[2] >= self.x0:
                self.backwards = False
        else:
            self.canvas.move(self.blue, -self.step, -self.step)
            self.canvas.move(self.red, self.step, -self.step)
            self.canvas.move(self.yellow, -self.step, self.step)
            self.canvas.move(self.green, self.step, self.step)
            if self.canvas.coords(self.blue)[0] <= 0:
                self.backwards = True

if __name__ == '__main__':
    app = AnimationApp(step=20)
    app.mainloop()
