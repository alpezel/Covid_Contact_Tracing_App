import tkinter as tk
from tkinter import messagebox
from Class_Tkinter_Search_Entries import Search_Entry
class CovidContactTracingApp:
    def __init__(self,root):
        self.root = root
        self.root.title("COVID Contact Tracing App")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 290) // 2
        y = (screen_height - 440) // 2
        self.root.geometry(f"290x440+{x}+{y}")

        frame = tk.Frame(root, bg="lightblue")
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        menu = tk.Menu(root)
        root.config(menu=menu)

        search_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Search Entries", menu=search_menu)
        search_menu.add_command(label="Open Search", command=self.open_search)

        self.name_label = tk.Label(frame, text="Name:",bg="lightblue", fg="black")
        self.name_label.grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(frame,bg="lightyellow")
        self.name_entry.grid(row=0, column=1, padx=5, pady=2, sticky="e")

        self.email_label = tk.Label(frame, text="Email:",bg="lightblue", fg="black")
        self.email_label.grid(row=1, column=0, sticky="w")
        self.email_entry = tk.Entry(frame,bg="lightyellow")
        self.email_entry.grid(row=1, column=1, padx=5, pady=2, sticky="e")

        self.address_label = tk.Label(frame, text="Address:",bg="lightblue", fg="black")
        self.address_label.grid(row=2, column=0, sticky="w")
        self.address_entry = tk.Entry(frame,bg="lightyellow")
        self.address_entry.grid(row=2, column=1, padx=5, pady=2, sticky="e")

        self.number_label = tk.Label(frame, text="Contact Number:",bg="lightblue", fg="black")
        self.number_label.grid(row=3, column=0, sticky="w")
        self.number_entry = tk.Entry(frame,bg="lightyellow")
        self.number_entry.grid(row=3, column=1, padx=5, pady=2, sticky="e")

        self.sex_label = tk.Label(frame, text="Sex:",bg="lightblue", fg="black")
        self.sex_label.grid(row=4, column=0, sticky="w")
        self.sex= tk.StringVar()
        self.sex.set("Prefer not to say")
        self.other_button = tk.Radiobutton(frame, text="Prefer not to say", variable=self.sex, value="Prefer not to say",bg="lightyellow")
        self.female_button = tk.Radiobutton(frame, text="Female", variable=self.sex, value="Female",bg="lightyellow")
        self.male_button = tk.Radiobutton(frame, text="Male", variable=self.sex, value="Male",bg="lightyellow")

        
        self.other_button.grid(row=4, column=1, padx=5, pady=2, sticky="w")
        self.female_button.grid(row=5, column=1, padx=5, pady=2, sticky="w")
        self.male_button.grid(row=6, column=1, padx=5, pady=2, sticky="w")

        self.disclaimer_label = tk.Label(frame, text="Data Privacy Disclaimer:",bg="lightblue", fg="black")
        self.disclaimer_label.grid(row=7, column=0, sticky="w")

        self.disclaimer =  ("I hereby authorize this Covid Contact Tracing App, to collect and process the data indicated "
                           "for contact tracing to control the COVID-19 transmission. I understand that my personal "
                           "information is protected by RA 10173 or the Data Privacy Act of 2012 and this entry will "
                           "be deleted after 30 days from the date of accomplishment, following the National Archives of "
                           "the Philippines protocol.")
        
        self.disclaimer_frame = tk.Frame(frame)
        self.disclaimer_frame.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="w")
        self.disclaimer_widget = tk.Label(frame, text=self.disclaimer, wraplength=250, anchor="w",justify="left",bg="lightyellow") 
        self.disclaimer_widget.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="w")
       
        self.disclaimer_check_bool = tk.BooleanVar()
        
        self.disclaimer_check = tk.Checkbutton(frame, text="I Agree to the Disclaimer", variable=self.disclaimer_check_bool,bg="lightblue")
        self.disclaimer_check.grid(row=9, column=0, columnspan=2, pady=5, sticky="w")

        self.submit_buttom = tk.Button(frame,text="Submit", command=self.save_file,bg="white")
        self.submit_buttom.grid(row=10, column=0, columnspan=2, pady=5, sticky="w")
   

    def validate_userinput(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()
        number = self.number_entry.get().strip()
        
        if not all((name, email, address, number)):
            print("Please Fill in All the Required Fields.")
            return False
        if not self.sex.get():
            print("Please Select in the Choices.")
            return False
        if not self.disclaimer_check_bool.get():
            print("Please Agree to the Disclaimer.")
            return False
        
        return True
    
    def save_file(self):
        if not self.validate_userinput():
            messagebox.showwarning("Invalid Input","Please Fill in All the Required Fields, Agree to the Disclaimer, and Select in the Sex Choices.")
            return
        
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()
        number = self.number_entry.get().strip()
        sex = self.sex.get()

        with open("contact_tracing.txt","a") as file:
            file.write(f"Name:{name}, Email:{email}, Address:{address}, Contact Number:{number}, Sex:{sex}\n")
        
        self.name_entry.delete(0,tk.END)
        self.email_entry.delete(0,tk.END)
        self.address_entry.delete(0,tk.END)
        self.number_entry.delete(0,tk.END)
        self.disclaimer_check.deselect()
        self.sex.set("Prefer not to say")
        print("Data Saved Successfully!")
        messagebox.showinfo("Entry Saved","Data Saved Successfully!")

    def open_search(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Entries")
        screen_width = search_window.winfo_screenwidth()
        screen_height = search_window.winfo_screenheight()
        x = (screen_width - 290) // 2
        y = (screen_height - 460) // 2
        search_window.geometry(f"290x460+{x}+{y}")
        search_entry = Search_Entry(search_window)
      
    