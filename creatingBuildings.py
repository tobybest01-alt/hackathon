import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Building GUI")
window.geometry("800x600")
window.configure(bg="skyblue")

# Create a canvas
canvas = tk.Canvas(window, width=800, height=600, bg="skyblue")
canvas.pack()

# Sun
canvas.create_oval(650, 50, 730, 130, fill="yellow", outline="")

# Ground
canvas.create_rectangle(0, 500, 800, 600, fill="green", outline="")

# Building 1
canvas.create_rectangle(50, 250, 200, 500, fill="gray", outline="black", width=2)

# Windows for building 1
for x in range(70, 190, 40):
    for y in range(280, 480, 50):
        canvas.create_rectangle(x, y, x + 20, y + 30,
                                fill="lightblue", outline="black")

# Building 2
canvas.create_rectangle(250, 180, 400, 500, fill="brown", outline="black", width=2)

# Windows for building 2
for x in range(270, 390, 40):
    for y in range(210, 480, 50):
        canvas.create_rectangle(x, y, x + 20, y + 30,
                                fill="yellow", outline="black")

# Building 3 - skyscraper
canvas.create_rectangle(470, 100, 650, 500, fill="darkblue", outline="black", width=2)

# Windows for skyscraper
for x in range(490, 640, 40):
    for y in range(130, 480, 50):
        canvas.create_rectangle(x, y, x + 20, y + 30,
                                fill="lightblue", outline="black")

# Title
canvas.create_text(
    400, 30,
    text="My City",
    font=("Arial", 24, "bold"),
    fill="white"
)

# Start the GUI
window.mainloop()
