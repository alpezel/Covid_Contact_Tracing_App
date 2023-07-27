import tkinter as tk
from tkinter import messagebox
from Class_Tkinter_Covid_Contact_Tracing_App import CovidContactTracingApp
from Search_Entries import Search_Entry


if __name__ == "__main__":
    root = tk.Tk()
    app = CovidContactTracingApp(root)
    search = Search_Entry(root)
    root.mainloop()