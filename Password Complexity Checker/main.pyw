import tkinter as tk
from tkinter import ttk, messagebox
import re
import os
from style import apply_styles

def check_password_strength(password):
    length = len(password)
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    score = 0
    feedback = []

    if length >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if has_upper:
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if has_lower:
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if has_digit:
        score += 1
    else:
        feedback.append("Add digits.")

    if has_special:
        score += 1
    else:
        feedback.append("Add special characters.")

    if score == 5:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    elif score >= 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback

def estimate_crack_time(password):
    guesses_per_second = 1e10  # 10 billion guesses per second

    charset_size = 0
    if re.search(r"[a-z]", password):
        charset_size += 26
    if re.search(r"[A-Z]", password):
        charset_size += 26
    if re.search(r"\d", password):
        charset_size += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset_size += 32  # Approximate count of special chars

    length = len(password)

    if charset_size == 0 or length == 0:
        return "N/A"

    total_combinations = charset_size ** length

    seconds = total_combinations / guesses_per_second

    intervals = (
        ('centuries', 60*60*24*365*100),
        ('years', 60*60*24*365),
        ('days', 60*60*24),
        ('hours', 60*60),
        ('minutes', 60),
        ('seconds', 1)
    )

    result = []
    for name, count in intervals:
        value = int(seconds // count)
        if value > 0:
            seconds -= value * count
            result.append(f"{value} {name}")
    return ', '.join(result) if result else "less than 1 second"

def on_check():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password to check.")
        return
    
    strength, feedback = check_password_strength(password)
    crack_time = estimate_crack_time(password)
    
    result_label.config(text=f"Password Strength: {strength}\nEstimated time to crack: {crack_time}")
    
    feedback_text.config(state=tk.NORMAL)
    feedback_text.delete("1.0", tk.END)
    if feedback:
        feedback_text.insert(tk.END, "Suggestions:\n- " + "\n- ".join(feedback))
    else:
        feedback_text.insert(tk.END, "Your password is strong! No suggestions.")
    feedback_text.config(state=tk.DISABLED)

def toggle_password_visibility():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_btn.config(text="Show")
    else:
        password_entry.config(show='')
        toggle_btn.config(text="Hide")

# GUI Setup
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("520x420")
root.resizable(False, False)

# Set app icon
icon_path = os.path.join("assets", "icon.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

apply_styles(root)  # Apply your style.py styles

# Title Label
title = ttk.Label(root, text="Password Complexity Checker", font=("Segoe UI", 18, "bold"))
title.pack(pady=15)

# Password input frame for entry + toggle button
pwd_frame = ttk.Frame(root)
pwd_frame.pack(pady=5)

ttk.Label(pwd_frame, text="Enter Password:", font=("Segoe UI", 12)).grid(row=0, column=0, sticky="w", columnspan=2)

password_entry = ttk.Entry(pwd_frame, width=38, show="*")
password_entry.grid(row=1, column=0, padx=(0,5))

toggle_btn = ttk.Button(pwd_frame, text="Show", width=6, command=toggle_password_visibility)
toggle_btn.grid(row=1, column=1)

# Check Button
check_btn = ttk.Button(root, text="Check Strength", command=on_check)
check_btn.pack(pady=15)

# Result Label
result_label = ttk.Label(root, text="", font=("Segoe UI", 14))
result_label.pack(pady=5)

# Feedback Textbox
feedback_text = tk.Text(root, height=8, width=60, state=tk.DISABLED, bg="#f0f0f0", font=("Segoe UI", 11))
feedback_text.pack(pady=5)

root.mainloop()
