# Covid Contact Tracing App
This App uses 3 Python files the following are for the contact tracing app, searching entries, and a main Python file where the program will be run.
## Class_Tkinter_Covid_Contact_Tracing_App.py
The "Class_Tkinter_Covid_Contact_Tracing_App.py" script is a Python application that provides a graphical user interface (GUI) for contact tracing related to COVID-19. The app allows users to input their personal information, such as name, email, address, contact number, and sex. It also includes a data privacy disclaimer for user consent.
### Usage
1. Make sure you have Python 3.x installed on your system.
2. Ensure that the Tkinter library is available. It is usually included in the standard Python distribution, so you likely won't need to install anything separately.
3. Run the "CovidContactTracingApp.py" script. This will open a window with fields to enter personal information and a checkbox for agreeing to the data privacy disclaimer.
4. Fill in all the required fields: name, email, address, and contact number. Select your sex from the available options: "Prefer not to say," "Female," or "Male."
5. Read the data privacy disclaimer and check the "I Agree to the Disclaimer" checkbox if you consent to provide your data for contact tracing purposes.
6. Click the "Submit" button to save the entered data to a file named "contact_tracing.txt" in the current directory.
7. The app will display a success message upon successfully saving the data. If any required fields are left empty, or the disclaimer checkbox is not selected, a warning message will be shown.
8. To search for specific entries, click "Search Entries" in the menu and open the search window. The search functionality is implemented using another class called Search_Entry, which provides search capabilities.

## Notes
- The app ensures that all required fields are filled in before saving the data to the file.
- If the disclaimer checkbox is not checked, the data will not be saved, and a warning message will be displayed.
- The "contact_tracing.txt" file stores the entered data in a comma-separated format for easy retrieval.
- The app uses Tkinter for the GUI, making it a lightweight and simple solution for contact tracing purposes.

## Class_Tkinter_Search_Entries.py
The "Class_Tkinter_Search_Entries.py" file contains a Python class named Search_Entry that provides a basic graphical user interface (GUI) for searching entries in a file and displaying the matching results.

### Usage
1. Make sure you have Python 3.x installed on your system.
2. Ensure that the Tkinter library is available. It is usually included in the standard Python distribution, so you likely won't need to install anything separately.
3. Place the "contact_tracing.txt" file in the same directory as the "Class_Tkinter_Search_Entries.py" file, or modify the file path in the search_entries method if the file is located elsewhere.
4. To use the class, import it into your Python script.

## Notes
- The search is case-insensitive. It will find matches regardless of the case of the search term and the entries in the file.
- If there are no matching entries found, a message will be printed in the console.
- If the search term is empty, a message will also be printed in the console, prompting the user to enter a search term.
- The search results are displayed in a new window with a simple layout.

## Outputs

# How To Use / Run
1. Install Python on your computer to run the code. You can download its latest version here: https://www.python.org/downloads/ 
2. Copy the code from the repository. 
3. Open an IDE and paste the code. 
4. Save the file with a .py extension. 
5. Run the code. 
