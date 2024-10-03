# Importing necessary classes from the libraries
from tkOOP import ScreenWidget, ButtonWidget, LabelWidget
from dbOOP import Dataset

# Create a dataset instance for "answers.txt"
answers_dataset = Dataset("answers.txt")

# Add the correct answer to the dataset
answers_dataset.add_data("Ankara")

# Function to check the answer
def check_answer(selected_answer):
    if selected_answer == "Ankara":
        label_widget.label.config(text="Congratulations")  # Correct answer
    else:
        label_widget.label.config(text="Oopsie, wrong answer")  # Wrong answer

# Creating the GUI
screen = ScreenWidget("Capital City Quiz", "lightgreen")

# Label to display the question
label_widget = LabelWidget(screen, text="What is the capital city of Turkey?", x=50, y=50)
label_widget.set_width(25)

# Buttons for answer options
button_rome = ButtonWidget(screen, text="Rome", command=lambda: check_answer("Rome"), x=50, y=100)
button_ankara = ButtonWidget(screen, text="Ankara", command=lambda: check_answer("Ankara"), x=150, y=100)
button_istanbul = ButtonWidget(screen, text="Istanbul", command=lambda: check_answer("Istanbul"), x=250, y=100)
button_paris = ButtonWidget(screen, text="Paris", command=lambda: check_answer("Paris"), x=350, y=100)

# Start the main loop
screen.start()
