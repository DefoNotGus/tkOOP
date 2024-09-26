**What is tkOOP?**

This is a Python library used for formulating tkinter code making following the instructions listed below:

- **ScreenWidget**:  
  - **Purpose**: Creates the main window for your app.
  - **Attributes**: 
    - `title`: Window title (e.g., "My App").
    - `bg`: Background color (e.g., "blue").
  - **Common Uses**: Starting point for any app; sets up the visual space where everything happens.
  - **Functions**: 
    - `set_width(width)`: Adjusts the window's width.
    - `set_height(height)`: Adjusts the window's height.
    - `toggle_fullscreen(enable)`: Turns fullscreen mode on or off.
    - `start()`: Launches the app so it can be used.

- **ButtonWidget**:  
  - **Purpose**: Adds a clickable button to perform an action.
  - **Attributes**: 
    - `text`: Button label (e.g., "Submit").
    - `bg`: Background color (e.g., "yellow").
    - `command`: Function to run when the button is clicked.
  - **Common Uses**: Perform actions like submitting a form or starting a process.
  - **Functions**: 
    - `set_width(width)`: Adjusts button width.
    - `set_height(height)`: Adjusts button height.
    - `change_text(new_text)`: Changes the button's label.
    - `change_command(new_command)`: Updates the action tied to the button.

- **InputWidget**:  
  - **Purpose**: Creates a text input field where users can type.
  - **Attributes**: 
    - `bg`: Background color (e.g., "white").
  - **Common Uses**: Collect user input like names or emails.
  - **Functions**: 
    - `set_width(width)`: Adjusts the width of the input box.

- **ImageWidget**:  
  - **Purpose**: Displays an image (e.g., a logo or photo).
  - **Attributes**: 
    - `image_path`: Path to the image file (e.g., "logo.png").
    - `width`, `height`: Size of the image.
  - **Common Uses**: Show visual elements like pictures or icons in your app.
  - **Functions**: 
    - `set_size(width, height)`: Adjusts the image size while keeping proportions.
    - `change_image_path(new_image_path)`: Changes the image file being displayed.

- **LabelWidget**:  
  - **Purpose**: Adds a label to show text in the app.
  - **Attributes**: 
    - `text`: Text to display (e.g., "Welcome!").
    - `bg`: Background color (e.g., "green").
  - **Common Uses**: Display instructions, titles, or static information.
  - **Functions**: 
    - `set_width(width)`: Adjusts label width.

- **CheckboxWidget**:  
  - **Purpose**: Creates a checkbox that users can check or uncheck.
  - **Attributes**: 
    - `text`: Label next to the checkbox (e.g., "I Agree").
  - **Common Uses**: Let users make binary choices (e.g., accept terms or select options).

- **FrameWidget**:  
  - **Purpose**: Creates a container to group other widgets.
  - **Attributes**: 
    - `width`, `height`: Size of the frame.
    - `bg`: Background color (e.g., "lightgray").
  - **Common Uses**: Organize layout by grouping multiple widgets together.
  - **Functions**: 
    - `set_width(width)`: Adjusts the frame’s width.
    - `set_height(height)`: Adjusts the frame’s height.
    - `set_position(x, y)`: Moves the frame to a specific position.
    - `show()`: Makes the frame visible.
    - `hide()`: Hides the frame from view.

- **Utility Function**:  
  - **print_actions()**: 
    - **Purpose**: Prints a list of all the Tkinter actions performed so far.
    - **Common Uses**: Track what you've built step by step, useful for debugging.
