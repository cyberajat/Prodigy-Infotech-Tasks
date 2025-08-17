import tkinter as tk
from tkinter import ttk, messagebox
import os
from style import apply_styles  # Import styling module

# Caesar Cipher logic
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == "Encrypt":
                shifted = (ord(char) - base + shift) % 26 + base
            else:  # Decrypt
                shifted = (ord(char) - base - shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

# Process button callback
def process():
    mode = mode_var.get()
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return

    if not text:
        messagebox.showwarning("Empty Input", "Please enter a message.")
        return

    output = caesar_cipher(text, shift, mode)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output)
    output_text.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher Encoder/Decoder")
root.geometry("600x500")
root.resizable(False, False)

# Set app icon
icon_path = os.path.join("assets", "ico.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

apply_styles(root)  # Apply custom styles

# Title Label
title = ttk.Label(root, text="Caesar Cipher Tool", font=("Segoe UI", 16, "bold"))
title.pack(pady=10)

# Mode and Shift Frame
mode_var = tk.StringVar(value="Encrypt")
mode_frame = ttk.Frame(root)
mode_frame.pack(pady=5)

ttk.Label(mode_frame, text="Mode:").grid(row=0, column=0, padx=5)
mode_menu = ttk.Combobox(mode_frame, textvariable=mode_var, values=["Encrypt", "Decrypt"], state="readonly", width=12)
mode_menu.grid(row=0, column=1)

ttk.Label(mode_frame, text="Shift:").grid(row=0, column=2, padx=10)
shift_entry = ttk.Entry(mode_frame, width=6)
shift_entry.grid(row=0, column=3)

# Message Input
ttk.Label(root, text="Enter your message:").pack(pady=5)
input_text = tk.Text(root, height=6, width=60, font=("Consolas", 12))
input_text.pack()

# Process Button
ttk.Button(root, text="Process", command=process).pack(pady=15)

# Output Display
ttk.Label(root, text="Output:").pack()
output_text = tk.Text(root, height=6, width=60, font=("Consolas", 12), bg="#eeeeee", state=tk.DISABLED)
output_text.pack()

root.mainloop()
