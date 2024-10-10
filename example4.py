# Importing the custom libraries
from tkOOP import ScreenWidget, ButtonWidget, LabelWidget, FrameWidget, InputWidget
from dbOOP import Dataset

import time
import os

# Initialize the dataset for storing player scores
score_dataset = Dataset('scores.txt')

# Initialize the main screen
main_screen = ScreenWidget(title="Quiz Game", bg="lightblue")

# Create Main Menu Frame
main_menu_frame = FrameWidget(main_screen, width=600, height=400, bg="lightblue", x=0, y=0)

# Function to handle 'Start' button click
def start_game():
    main_menu_frame.hide()
    show_name_input()

# Function to handle 'Score' button click
def show_scores():
    main_menu_frame.hide()
    display_scores()

# Create 'Start' button in Main Menu Frame
start_button = ButtonWidget(parent=main_menu_frame, text="Start", bg="green", command=start_game, x=250, y=150)

# Create 'Score' button in Main Menu Frame
score_button = ButtonWidget(parent=main_menu_frame, text="Score", bg="orange", command=show_scores, x=250, y=220)

# Function to display the name input frame
def show_name_input():
    # Create a new frame for name input
    name_frame = FrameWidget(main_screen, width=600, height=400, bg="lightblue", x=0, y=0)
    
    # Label for name input
    name_label = LabelWidget(parent=name_frame, text="Enter Your Name:", bg="lightblue", x=200, y=150)
    
    # Input field for name
    name_input = InputWidget(parent=name_frame, bg="white", x=250, y=180)
    
    # Function to handle 'Save' button click
    def save_name():
        player_name = name_input.entry.get().strip()
        if player_name:
            name_frame.hide()
            show_question(player_name)
        else:
            name_label.label.config(text="Name cannot be empty. Please enter your name.")
    
    # 'Save' button
    save_button = ButtonWidget(parent=name_frame, text="Save", bg="blue", command=save_name, x=275, y=220)

# Function to display the quiz question frame
def show_question(player_name):
    # Create a new frame for the question
    question_frame = FrameWidget(main_screen, width=600, height=400, bg="lightyellow", x=0, y=0)
    
    # Question label
    question_label = LabelWidget(parent=question_frame, text="What is the capital of France?", bg="lightyellow", x=150, y=50)
    
    # Stopwatch label
    stopwatch_label = LabelWidget(parent=question_frame, text="Time: 0.00s", bg="lightyellow", x=250, y=10)
    
    # Start the stopwatch
    start_time = time.time()
    
    # Update the stopwatch every 100 ms
    def update_stopwatch():
        current_time = time.time()
        elapsed = current_time - start_time
        stopwatch_label.label.config(text=f"Time: {elapsed:.2f}s")
        question_frame.frame.after(100, update_stopwatch)
    
    update_stopwatch()
    
    # Function to check the answer
    def check_answer(selected_answer):
        end_time = time.time()
        elapsed_time = end_time - start_time
        if selected_answer == "Paris":
            score_dataset.add_data(f"{player_name},{elapsed_time:.2f}")
            question_label.label.config(text=f"Correct! Time taken: {elapsed_time:.2f} seconds")
            # Navigate back to main menu after 2 seconds
            question_frame.frame.after(2000, lambda: navigate_back(question_frame))
        else:
            question_label.label.config(text="Incorrect! Try again.")
    
    # Answer buttons
    answer1 = ButtonWidget(parent=question_frame, text="Berlin", bg="red", command=lambda: check_answer("Berlin"), x=200, y=100)
    answer2 = ButtonWidget(parent=question_frame, text="Madrid", bg="red", command=lambda: check_answer("Madrid"), x=200, y=150)
    answer3 = ButtonWidget(parent=question_frame, text="Paris", bg="red", command=lambda: check_answer("Paris"), x=200, y=200)
    answer4 = ButtonWidget(parent=question_frame, text="Rome", bg="red", command=lambda: check_answer("Rome"), x=200, y=250)

# Function to navigate back to the main menu
def navigate_back(current_frame):
    current_frame.hide()
    main_menu_frame.show()

# Function to display the scores
def display_scores():
    # Create a new frame for displaying scores
    score_frame = FrameWidget(main_screen, width=600, height=400, bg="lightgreen", x=0, y=0)
    
    # Label for scores
    score_label = LabelWidget(parent=score_frame, text="Player Scores", bg="lightgreen", x=250, y=20)
    
    # Retrieve data from the dataset
    data = score_dataset.get_data()
    scores = []
    for line in data:
        if ',' in line:
            name, time_taken = line.strip().split(',')
            try:
                scores.append((name, float(time_taken)))
            except ValueError:
                continue  # Skip lines with invalid format
    
    # Sort the scores by time taken (ascending)
    sorted_scores = sorted(scores, key=lambda x: x[1])
    
    # Display the sorted scores
    y_position = 60
    for idx, (name, time_taken) in enumerate(sorted_scores, start=1):
        score_text = f"{idx}. {name} - {time_taken:.2f} seconds"
        player_label = LabelWidget(parent=score_frame, text=score_text, bg="lightgreen", x=200, y=y_position)
        y_position += 30
    
    # Back button to return to main menu
    def back_to_main():
        score_frame.hide()
        main_menu_frame.show()
    
    back_button = ButtonWidget(parent=score_frame, text="Back", bg="grey", command=back_to_main, x=250, y=350)

# Display the main menu frame
main_menu_frame.show()

# Start the application
main_screen.start()
