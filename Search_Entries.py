import tkinter as tk
from tkinter import messagebox

class Search_Entry:
    def __init__(self,root):
        self.root = root
        
        search_frame = tk.Frame(root)
        search_frame.pack()
        self.search_label = tk.Label(search_frame, text="Search:")
        self.search_label.pack()
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack()