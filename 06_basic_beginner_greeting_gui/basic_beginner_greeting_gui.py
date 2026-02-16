# GREETING GUI
import tkinter as tk
root = tk.Tk()
root.title("Mini Greeting App")
root.geometry("400x300")
label=tk.Label(
        root,
        text="Enter Your Name:",
        font=("JetBrains Mono", 16)
    )
label.pack(pady=20)
def reset():
    label.config(
        text="Enter Your Name:",
        fg="black"
    )
entry = tk.Entry(root, font=("JetBrains Mono", 12))
entry.pack(pady=10)
def greet():
    name = entry.get()
    if name.strip():
        label.config(text=f"Hello, {name}!", fg="green")
    else:
        label.config(text="Please enter a valid name.", fg="red")
    entry.delete(0, tk.END)
    root.after(2000,reset)
button = tk.Button(
    root,
    text="Greet Me",
    font=("JetBrains Mono", 12),
    command=greet
)
button.pack(pady=10)
root.mainloop()
