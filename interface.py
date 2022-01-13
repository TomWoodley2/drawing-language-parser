import tkinter as tk

class App(tk.Frame):

#--------------------------------------------------------------------------------------------------

    def __init__(self, master=None):
        super().__init__(master)
        self.canvas = tk.Canvas(self)
        self.pack()

#--------------------------------------------------------------------------------------------------

    def setup_window(self, start_pos):
        self.master.title("My Do-Nothing Application")
        self.master.maxsize(1000, 400)
        self.master.geometry("300x300")
        
        self.start_pos   = start_pos
        self.current_pos = start_pos
        
        self.canvas.pack(fill=tk.BOTH, expand=1)

#--------------------------------------------------------------------------------------------------

    def add_line(self, direction, length):
        # line is defined by 2 points

        x1 = self.current_pos[0]
        y1 = self.current_pos[1]
        x2 = x1
        y2 = y1

        if direction == 'N':
            y2 = y1 - length
        elif direction == 'E':
            x2 = x1 + length
        elif direction == 'S':
            y2 = y1 + length
        elif direction == 'W':
            x2 = x1 - length
        else:
            print("Invalid direction '" + direction + "' provided")
            return -1

        self.current_pos = (x2, y2)

        self.canvas.create_line(x1, y1, x2, y2)
        self.canvas.pack(fill=tk.BOTH, expand=1)

#--------------------------------------------------------------------------------------------------