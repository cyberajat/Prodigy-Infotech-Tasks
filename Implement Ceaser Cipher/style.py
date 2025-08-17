# style.py

from tkinter import ttk

def apply_styles(root):
    style = ttk.Style(root)

    # General font settings
    style.configure("TLabel", font=("Segoe UI", 12), background="#f8f8f8", foreground="#333333")
    style.configure("TEntry", font=("Segoe UI", 12))
    style.configure("TButton", font=("Segoe UI", 12), padding=6)
    style.configure("TCombobox", font=("Segoe UI", 12))

    # Make button hover effect (if available)
    try:
        style.map("TButton",
                  foreground=[("pressed", "white"), ("active", "#0078D7")],
                  background=[("active", "#e6f0ff")])
    except:
        pass

    # Set default theme
    style.theme_use("default")

    # Set window background color
    root.configure(bg="#f8f8f8")
