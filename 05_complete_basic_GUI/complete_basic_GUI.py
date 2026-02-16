# BASIC GUI
import tkinter as tk
c = 0
root = tk.Tk()
root.title("My First GUI")
root.geometry("400x300")
label=tk.Label(
    root,
    text="Waiting for Action...",
    font=("JetBrains Mono", 16),
    fg="red"
)
label.pack(pady=20)
def say_hello():
    global c
    c+=1
    if c==1:
        label.config(text="Button Was Clicked!",fg="green")
    elif c==2:
        label.config(text="Clicked Again!",fg="blue")
    else:
        label.config(text="Stop Clicking,Bruhh ",fg="purple")
    print("Button Clicked!")
button = tk.Button(
    root,
    text="Press Me",
    font=("JetBrains Mono", 12),
    command=say_hello
)
button.pack(pady=10)
root.mainloop()