import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.canvas = tk.Canvas(self)
        self.pack()

    def setup_window(self):
        self.master.title("My Do-Nothing Application")
        self.master.maxsize(1000, 400)
        self.master.geometry("300x300")

        #self.canvas.create_line(15, 25, 200, 25)
        self.canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        self.canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        
        self.canvas.pack(fill=tk.BOTH, expand=1)

    def add_line(self):
        self.canvas.create_line(15, 25, 200, 25)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.pack()