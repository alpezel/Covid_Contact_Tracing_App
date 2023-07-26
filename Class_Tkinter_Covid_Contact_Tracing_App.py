import tkinter as tk
from tkinter import messagebox

class CovidContactTracingApp:
    def __init__(self,root):
        self.root = root
        self.root.title("COVID Contact Tracing App")
        self.root.geometry("200x200")

        frame = tk.Frame(root)
        frame.pack(side = tk.LEFT, padx=10, pady=10)

        self.name_label = tk.Label(frame, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(frame)
        self.name_entry.pack()

        self.address_label = tk.Label(frame, text="Address:")
        self.address_label.pack()
        self.address_entry = tk.Entry(frame)
        self.address_entry.pack()

        self.number_label = tk.Label(frame, text="Contact Number:")
        self.number_label.pack()
        self.number_entry = tk.Entry(frame)
        self.number_entry.pack()

