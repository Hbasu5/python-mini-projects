#PASSWORD GENERATOR (GUI VERSION)
import tkinter as tk
import random
import string

def password_generator(length):
    characters=string.ascii_letters+string.digits
    password=""
    for _ in range(length):
        password+=random.choice(characters)
    return password

def password_generation_on_click(event=None):
    try:
        length = int(entry.get())
        if length <= 0:
            label1.config(text="Please enter a positive integer for the password length.", wraplength=400)
            return
        elif length > 128:
            label1.config(text="Please enter a smaller integer (max 128) for the password length.", wraplength=400)
            return
    except ValueError:
        label1.config(text="Invalid input. Please enter a valid integer for the password length.", wraplength=400)
        return

    obtained_password = password_generator(length)
    root.clipboard_clear()
    result.config(text=f"Generated password: {obtained_password}")
    root.clipboard_append(obtained_password)
    root.after(4000, reset)

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x450")
root.resizable(False, False)
root.config(bg="#CED2DA")

label = tk.Label(
    root,
    text="Enter the length of the password\n\nPassword is automatically copied to clipboard once generated. Wait 4 seconds before new generation.",
    wraplength=475,
    font=("JetBrains Mono", 12),
    bg="#CED2DA",
)
label.pack(pady=20)
entry = tk.Entry(
    root,
    font=("JetBrains Mono", 12),
    bg="#8199DC",
)
entry.pack(pady=10)
button = tk.Button(
    root,
    text="Generate Password or Hit Enter",
    font=("JetBrains Mono", 12),
    command=password_generation_on_click,
    bg="#4CAF50",
)
root.bind("<Return>", password_generation_on_click)
button.pack(pady=10)
label1 = tk.Label(
    root,
    text="Generated password will be displayed below",
    font=("JetBrains Mono", 10),
    bg="#CED2DA",
)
label1.pack(pady=10)
result = tk.Label(
    root,
    text="",
    wraplength=400,
    font=("JetBrains Mono", 12),
    bg="#CED2DA",
)
result.pack(pady=10)
def reset():
    entry.delete(0, tk.END)
    result.config(text="")
    label1.config(text="Enter the length of the password")
entry.focus()
root.mainloop()