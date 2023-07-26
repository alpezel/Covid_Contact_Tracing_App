import tkinter as tk
from tkinter import messagebox

class CovidContactTracingApp:
    def __init__(self,root):
        self.root = root
        self.root.title("COVID Contact Tracing App")
        self.root.geometry("100x100")

        frame = tk.Frame(root)
        frame.pack(side = tk.LEFT, padx=10, pady=10)

        self.name_label = tk.Label(frame, text="Name:")
        self.name_label.pack()
        self.name_intput = tk.Entry(frame)
        self.name_intput.pack()
