import tkinter as tk
import os


class MasterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x150+150+50')
        self.counter = 0
        self.nerdVar = tk.IntVar(self, 0)
        self.textvar = tk.StringVar(self, f'{self.counter}')

        self.nlabel = tk.Label(self, textvar=self.textvar, fg='red')

        self.label = tk.Label(self, text='Click On Me', font=('Arial', 20))
        self.label.bind('<Triple-Button-1>', self.triple_click)
        self.label.pack(padx=10, pady=10)

        self.checkNerd = tk.Checkbutton(
            self, text='Nerd stats', command=self.check_changed, variable=self.nerdVar)
        self.checkNerd.pack()

    def triple_click(self, event):
        self.counter += 1
        self.textvar.set(f'{self.counter}')
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')
        print(f"You triple-clicked {self.counter} times...")

    def check_changed(self):
        if self.nerdVar.get():
            self.nlabel.place(x=10, y=10)
        else:
            self.nlabel.place_forget()


if __name__ == '__main__':
    app = MasterApp()
    app.mainloop()
