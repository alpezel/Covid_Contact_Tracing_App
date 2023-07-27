import tkinter as tk
from tkinter import messagebox

class CovidContactTracingApp:
    def __init__(self,root):
        self.root = root
        self.root.title("COVID Contact Tracing App")
        self.root.geometry("500x500")

        frame = tk.Frame(root)
        frame.pack(side = tk.LEFT, padx=10, pady=10)

        self.name_label = tk.Label(frame, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(frame)
        self.name_entry.pack()

        self.email_label = tk.Label(frame, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(frame)
        self.email_entry.pack()

        self.address_label = tk.Label(frame, text="Address:")
        self.address_label.pack()
        self.address_entry = tk.Entry(frame)
        self.address_entry.pack()

        self.number_label = tk.Label(frame, text="Contact Number:")
        self.number_label.pack()
        self.number_entry = tk.Entry(frame)
        self.number_entry.pack()

        self.sex_label = tk.Label(frame, text="Sex:")
        self.sex= tk.StringVar()
        self.sex.set("Prefer not to say")
        self.male_button = tk.Radiobutton(frame, text="Male", variable=self.sex, value="Male")
        self.female_button = tk.Radiobutton(frame, text="Female", variable=self.sex, value="Female")
        self.other_button = tk.Radiobutton(frame, text="Prefer not to say", variable=self.sex, value="Prefer not to say")
        self.male_button.pack()
        self.female_button.pack()
        self.other_button.pack()

        self.disclaimer_label = tk.Label(frame, text="Data Privacy Disclaimer:")
        self.disclaimer_label.pack()

        self.disclaimer =  ("I hereby authorize this Covid Contact Tracing App, to collect and process the data indicated "
                           "for contact tracing to control the COVID-19 transmission. I understand that my personal "
                           "information is protected by RA 10173 or the Data Privacy Act of 2012 and that this entry will "
                           "be deleted after 30 days from the date of accomplishment, following the National Archives of "
                           "the Philippines protocol.")
        
        self.disclaimer_frame = tk.Frame(frame)
        self.disclaimer_frame.pack()
        self.disclaimer_widget = tk.Label(frame, text=self.disclaimer, wraplength=250, anchor="w",justify="left") 
        self.disclaimer_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
       
        self.disclaimer_check_bool = tk.BooleanVar()
        
        self.disclaimer_check = tk.Checkbutton(frame, text="I Agree to the Disclaimer", variable=self.disclaimer_check_bool)
        self.disclaimer_check.pack()

        self.submit_buttom = tk.Button(frame,text="Submit", command=self.save_file)
        self.submit_buttom.pack()
   

    def validate_userinput(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()
        number = self.number_entry.get().strip()
        
        if not all((name, email, address, number)):
            print("Please Fill")
            return False
        if not self.sex.get():
            print("Please select in the choices")
            return False
        if not self.disclaimer_check_bool.get():
            print("Please Agree to the Disclaimer")
            return False
        return True
    
    def save_file(self):
        if not self.validate_userinput():
            messagebox.showwarning("Invalid Input")
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()
        number = self.number_entry.get().strip()
        sex = self.sex.get()

        with open("contact_tracing.txt","a") as file:
            file.write(f"Name:{name}\n, Email:{email}\n, Address:{address}\n, Contact Number:{number}\n, Sex:{sex}\n")
        
        self.name_entry.delete(0,tk.END)
        self.email_entry.delete(0,tk.END)
        self.address_entry.delete(0,tk.END)
        self.number_entry.delete(0,tk.END)
        self.disclaimer_check.deselect()
        self.sex.set("Prefer not to say")
        print("Data Saved Successfully!")
        messagebox.showinfo("Entry Saved","Data Saved Successfully!")

      
    