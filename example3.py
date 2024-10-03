# Importing necessary classes from the libraries
from tkOOP import ScreenWidget, InputWidget, ButtonWidget, LabelWidget
from dbOOP import Dataset

# Create a dataset instance for "data.txt"
dataset = Dataset("data.txt")

# Function to save the input text to the data file
def save_data():
    user_input = input_widget.entry.get()  # Get text from input
    if user_input:  # Check if input is not empty
        dataset.add_data(user_input)  # Save data
        input_widget.entry.delete(0, 'end')  # Clear the input field

# Function to read the entire contents of the data file
def read_data():
    data = dataset.get_data()  # Get data from the file
    label_widget.label.config(text=''.join(data))  # Update label with file contents

# Function to delete the specified data from the file
def del_data():
    user_input = input_widget.entry.get()  # Get text from input
    if user_input:  # Check if input is not empty
        dataset.remove_data(user_input)  # Remove specified data
        input_widget.entry.delete(0, 'end')  # Clear the input field after deletion

# Creating the GUI
screen = ScreenWidget("Simple Text File App", "lightblue")

# Input field
input_widget = InputWidget(screen, x=50, y=50)

# Save button
save_button = ButtonWidget(screen, text="Save", command=save_data, x=50, y=100)

# Read button
read_button = ButtonWidget(screen, text="Read", command=read_data, x=150, y=100)

# Delete button
delete_button = ButtonWidget(screen, text="Delete", command=del_data, x=250, y=100)

# Label to display file contents
label_widget = LabelWidget(screen, text="File contents will appear here", x=50, y=150)
label_widget.set_height(10)

# Start the main loop
screen.start()
