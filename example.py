import tkinter as tk
from tkOOP import *  # Import everything from tkOOP

# * Example usage
if __name__ == "__main__":  # * Line used to start the GUI, everything inside the IF will be displayed

    # Create a window
    app_screen = ScreenWidget(title="MY SUPER APP", bg="lightblue")

    # Enable fullscreen if desired
    #app_screen.toggle_fullscreen()

    # Create and place a label
    my_label = LabelWidget(parent=app_screen, text="Enter your name:", bg="lightblue", x=50, y=50)

    # Create and place an input field
    my_input = InputWidget(parent=app_screen, bg="pink", x=50, y=100)

    # Create a button with a command
    def button_action():
        my_button.change_text("You clicked the button")

    my_button = ButtonWidget(parent=app_screen, text="Click Me", bg="green", command=button_action, x=50, y=150)
    my_button.set_height(4)
    my_button.set_width(30)

    # Load and place a PNG image (ensure "example.png" is in the same directory)
    my_image = ImageWidget(parent=app_screen, image_path="example.png", x=300, y=50)
    my_image.set_size(100, 100)  # Resize the image to 100x100 pixels

    # Create and place a checkbox
    my_checkbox = CheckboxWidget(parent=app_screen, text="Accept Terms", x=50, y=250)

    # Create and show a frame
    my_frame = FrameWidget(screen=app_screen, width=400, height=200, x=100, y=300)
    my_frame.show()

    # Change the position of the frame
    my_frame.set_position(100, 300)  # You can change the position as needed

    # Create and place a label in the new frame
    frame_label = LabelWidget(parent=my_frame, text="This is a frame", bg="red", x=150, y=50)

    # Create and place a button in the new frame
    frame_button = ButtonWidget(parent=my_frame, text="Frame Button", bg="yellow", x=-0, y=30)

    # Start the app
    app_screen.start()

    # Print Tkinter actions when the app is closed
    print_actions()
