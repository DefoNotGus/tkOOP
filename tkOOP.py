import tkinter as tk

# List to track Tkinter actions
yourTkCode = []

# *CLASSES
# Screen class to initialize the main window
class ScreenWidget:
    def __init__(self, title="App", bg="white"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("600x400")  # Default size
        self.root.configure(bg=bg)
        yourTkCode.append(f"tk.Tk()\nroot.title('{title}')\nroot.geometry('600x400')\nroot.configure(bg='{bg}')")

    def set_width(self, width):
        self.root.geometry(f"{width}x{self.root.winfo_height()}")
        yourTkCode.append(f"root.geometry('{width}x' + str(root.winfo_height()))")

    def set_height(self, height):
        self.root.geometry(f"{self.root.winfo_width()}x{height}")
        yourTkCode.append(f"root.geometry(str(root.winfo_width()) + 'x{height}')")

    def toggle_fullscreen(self, enable=True):
        self.root.attributes('-fullscreen', enable)
        yourTkCode.append(f"root.attributes('-fullscreen', {enable})")

    def start(self):
        yourTkCode.append("root.mainloop()")
        self.root.mainloop()

# Button class
class ButtonWidget:
    def __init__(self, parent, text="Button", bg="lightgray", command=None, x=0, y=0):
        self.button = tk.Button(parent.root if isinstance(parent, ScreenWidget) else parent.frame, text=text, bg=bg, width=15, height=2, command=command)
        self.button.place(x=x, y=y)  # Use place to position
        yourTkCode.append(f"tk.Button(text='{text}', bg='{bg}', width=15, height=2, command={command})\nbutton.place(x={x}, y={y})")

    def set_width(self, width):
        self.button.config(width=width)
        yourTkCode.append(f"button.config(width={width})")

    def set_height(self, height):
        self.button.config(height=height)
        yourTkCode.append(f"button.config(height={height})")

    def change_text(self, new_text):
        self.button.config(text=new_text)
        yourTkCode.append(f"button.config(text='{new_text}')")

    def change_command(self, new_command):
        self.button.config(command=new_command)
        yourTkCode.append(f"button.config(command={new_command})")

# Input class
class InputWidget:
    def __init__(self, parent, bg="white", x=0, y=0):
        self.entry = tk.Entry(parent.root if isinstance(parent, ScreenWidget) else parent.frame, bg=bg, width=25)
        self.entry.place(x=x, y=y)  # Use place to position
        yourTkCode.append(f"tk.Entry(bg='{bg}', width=25)\nentry.place(x={x}, y={y})")

    def set_width(self, width):
        self.entry.config(width=width)
        yourTkCode.append(f"entry.config(width={width})")

# Image class for PNG images with resizing functionality
class ImageWidget:
    def __init__(self, parent, image_path=None, width=None, height=None, x=0, y=0):
        self.image_path = image_path
        self.original_image = tk.PhotoImage(file=image_path) if image_path else None
        self.image = self.original_image

        if width and height:
            self.set_size(width, height)

        self.label = tk.Label(parent.root if isinstance(parent, ScreenWidget) else parent.frame, image=self.image)
        self.label.place(x=x, y=y)  # Use place to position
        yourTkCode.append(f"tk.PhotoImage(file='{image_path}')\ntk.Label(image=original_image)\nlabel.place(x={x}, y={y})")

    def set_size(self, width, height):
        if self.original_image:  # Only resize if there is an image
            # Maintain the aspect ratio
            aspect_ratio = self.original_image.width() / self.original_image.height()
            if width and height:
                if aspect_ratio > 1:  # Wider than tall
                    height = int(width / aspect_ratio)
                else:
                    width = int(height * aspect_ratio)

            # Apply resizing
            self.image = self.original_image.subsample(int(self.original_image.width() / width), int(self.original_image.height() / height))
            self.label.config(image=self.image)  # Update label with the new image size
            yourTkCode.append(f"original_image.subsample({self.original_image.width() // width}, {self.original_image.height() // height})\nlabel.config(image=image)")

    def change_image_path(self, new_image_path):
        self.image_path = new_image_path
        self.original_image = tk.PhotoImage(file=new_image_path)
        self.image = self.original_image
        self.label.config(image=self.image)
        yourTkCode.append(f"tk.PhotoImage(file='{new_image_path}')\nlabel.config(image=original_image)")

# Label class
class LabelWidget:
    def __init__(self, parent, text="Label", bg="white", x=0, y=0):
        self.label = tk.Label(parent.root if isinstance(parent, ScreenWidget) else parent.frame, text=text, bg=bg, width=20, height=1)
        self.label.place(x=x, y=y)  # Use place to position
        yourTkCode.append(f"tk.Label(text='{text}', bg='{bg}', width=20, height=1)\nlabel.place(x={x}, y={y})")

    def set_width(self, width):
        self.label.config(width=width)
        yourTkCode.append(f"label.config(width={width})")

# Checkbox class
class CheckboxWidget:
    def __init__(self, parent, text="Checkbox", x=0, y=0):
        self.var = tk.IntVar()
        self.checkbox = tk.Checkbutton(parent.root if isinstance(parent, ScreenWidget) else parent.frame, text=text, variable=self.var)
        self.checkbox.place(x=x, y=y)  # Use place to position
        yourTkCode.append(f"tk.Checkbutton(text='{text}', variable=var)\ncheckbox.place(x={x}, y={y})")

# Frame class
class FrameWidget:
    def __init__(self, screen, width=300, height=200, bg="white", x=0, y=0):
        self.frame = tk.Frame(screen.root, width=width, height=height, bg=bg)
        self.frame.place(x=x, y=y)  # Use place to position
        yourTkCode.append(f"tk.Frame(width={width}, height={height}, bg='{bg}')\nframe.place(x={x}, y={y})")

    def set_width(self, width):
        self.frame.config(width=width)
        yourTkCode.append(f"frame.config(width={width})")

    def set_height(self, height):
        self.frame.config(height=height)
        yourTkCode.append(f"frame.config(height={height})")

    def set_position(self, x, y):
        self.frame.place(x=x, y=y)  # Set the frame's position
        yourTkCode.append(f"frame.place(x={x}, y={y})")

    def show(self):
        self.frame.lift()  # Bring the frame to the front
        yourTkCode.append("frame.lift()")

    def hide(self):
        self.frame.place_forget()  # Hide the frame
        yourTkCode.append("frame.place_forget()")

def print_actions():
    """Function to print all Tkinter actions."""
    print("\n".join(yourTkCode))
