# PASSWORD CHECKER GUI
import tkinter as tk
root = tk.Tk()
root.title("Password Checker")
root.geometry("400x300")
label=tk.Label(
    root,
    text="Enter Your Password:",
    font=("JetBrains Mono", 16)
)
label.pack(pady=20)
entry = tk.Entry(root, font=("JetBrains Mono", 12), show="*")
entry.pack(pady=10)
show_var=tk.BooleanVar()
def toggle_password():
    if show_var.get():
        entry.config(show="")
    else:
        entry.config(show="*")
show_checkbox = tk.Checkbutton(
    root,
    text="Show Password",
    font=("JetBrains Mono", 10),
    variable=show_var,
    command=toggle_password
)
show_checkbox.pack(pady=5)
def check_password(event):
    password = entry.get()
    if password.strip()=="":
        reset()
        return
    elif len(password)>=8 and (any(char.isdigit() for char in password)) and (any(not char.isalnum() for char in password)):
        label1.config(text="Strength: ✅Strong", fg="green")
    elif len(password)>=6 and (any(char.isdigit() for char in password)) and (any(char.isalpha() for char in password)):
        label1.config(text="Strength: ⚠️Medium", fg="orange")
    else:
        label1.config(text="Strength: ❌Weak", fg="red")
    
label1=tk.Label(
    root,
    text="Start typing to check strength...",
    font=("JetBrains Mono", 14)
)
label1.pack(pady=10)
def reset():
    label1.config(
        text="Start typing to check strength...",
        fg="black"
    )
entry.bind("<KeyRelease>",check_password)
root.mainloop()