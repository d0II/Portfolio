import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Display the pop-up message
messagebox.showinfo("Greeting", "Hello, World")

# Run the application
root.mainloop()
