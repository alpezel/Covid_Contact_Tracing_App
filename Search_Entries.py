import tkinter as tk

class Search_Entry:
    def __init__(self, root):
        self.root = root
        
        frame = tk.Frame(root)
        frame.pack()

        self.search_label = tk.Label(frame, text="Search Name:")
        self.search_label.pack()
        self.search_entry = tk.Entry(frame)
        self.search_entry.pack()

        self.search_button = tk.Button(frame, text="Search", command=self.search_entries)
        self.search_button.pack()

        self.exit_button = tk.Button(frame, text="Exit", command=root.quit)
        self.exit_button.pack()

    def search_entries(self):
        search_term = self.search_entry.get().strip().lower()
        if search_term:
            with open("contact_tracing.txt", "r") as file:
                matching_entries = [line.strip() for line in file if search_term in line.lower()]

            if matching_entries:
                self.display_results(matching_entries)
            else:
                print("No matching entries found.")
        else:
            print("Please enter a search term.")

    def display_results(self, entries):
        result_window = tk.Toplevel(self.root)
        result_window.title("Search Results")

        result_label = tk.Label(result_window, text="Search Results:")
        result_label.pack()

        result_text = tk.Text(result_window, height=20, width=60)
        result_text.pack()

        for entry in entries:
            result_text.insert(tk.END, entry + "\n")