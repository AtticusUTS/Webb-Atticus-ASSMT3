# Import necessary modules
import tkinter as tk  # Import Tkinter for creating the graphical user interface
import random  # Import random for generating random colour values


# Function to generate a random colour
def generate_colour():
    # Generate random values for red, green, and blue components
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # Convert RGB values to hexadecimal colour code
    colour = f'#{r:02x}{g:02x}{b:02x}'
    return colour


# Function to generate and display the colour palette
def generate_palette():
    # Get the number of colours to generate from the selection field
    num_colours = int(select_field.get())
    # Clear any existing colour labels from the colour frame
    for widget in colour_frame.winfo_children():
        widget.destroy()
    # Generate and display the specified number of colours
    for i in range(num_colours):
        colour = generate_colour()
        # Create a label to display the colour
        colour_label = tk.Label(colour_frame, bg=colour, width=10, height=5)
        colour_label.grid(row=i, column=0, padx=5, pady=5)
        # Create a label to display the hexadecimal colour code
        hex_label = tk.Label(colour_frame, text=colour, width=10)
        hex_label.grid(row=i, column=1, padx=5, pady=5)


# Create the main window
root = tk.Tk()
root.title("Colour Palette Generator")
root.geometry("300x655")  # Set the window size
root.configure(background="ghost white")  # Set the background colour

# Create a dropdown menu to select the number of colours
select_field = tk.StringVar(value="1")
select = tk.OptionMenu(root, select_field, "1", "2", "3", "4", "5")
select.pack(side="top", pady=10)
select.configure(background="ghost white")

# Create a button to generate the colour palette
generate_button = tk.Button(root, text="Generate", command=generate_palette)
generate_button.pack(side="top")
generate_button.configure(background="ghost white")

# Create a frame to hold the colour labels
colour_frame = tk.Frame(root)
colour_frame.pack(pady=10)
colour_frame.configure(background="white")

# Start the Tkinter event loop
root.mainloop()
