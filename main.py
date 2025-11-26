import tkinter as tk

# Function to handle button click (numbers and operators)
def click(event):
    text = event.widget.cget("text")  # Get text of clicked button
    if text == "=":
        try:
            result = str(eval(entry.get()))  # Evaluate the expression
            entry_var.set(result)            # Display the result
        except Exception as e:
            entry_var.set("Error")           # Display error if invalid
    elif text == "C":
        entry_var.set("")                   # Clear the display
    else:
        entry_var.set(entry_var.get() + text)  # Add the clicked button text to display

# Create main window
root = tk.Tk()
root.title("GW CALCULATOR")
root.geometry("300x400")  # Set window size

# Entry widget to show input and result
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", bd=5, relief=tk.RIDGE, justify='right')
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

# Frame to hold the buttons
frame = tk.Frame(root)
frame.pack()

# List of buttons
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

# Create buttons dynamically
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        btn = tk.Button(frame, text=btn_text, font="Arial 18", width=5, height=2)
        btn.grid(row=i, column=j, padx=5, pady=5)
        btn.bind("<Button-1>", click)  # Bind left mouse click to click function

# Run the main loop
root.mainloop()
