import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Main Window")

# Create a function to open the new window
def open_new_window():
    # Create the new window
    new_window = tk.Toplevel(window)
    new_window.title("New Window")

    # Create a label to display the input
    label = tk.Label(new_window, text="")
    label.pack()

    # Create a function to take the input and display it on the new window
    def show_input():
        # Get the input from the input field
        input_text = input_field.get()

        # Update the label with the input text
        label.config(text=input_text)

    # Create an input field for the user to enter text
    input_field = tk.Entry(new_window)
    input_field.pack()

    # Create a button to take the input and display it on the new window
    button = tk.Button(new_window, text="Show Input", command=show_input)
    button.pack()

# Create a button to open the new window
button = tk.Button(window, text="Open New Window", command=open_new_window)
button.pack()

# Run the main loop
window.mainloop()
