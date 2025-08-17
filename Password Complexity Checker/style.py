import tkinter.ttk as ttk

def apply_styles(root):
    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure("TLabel", foreground="#333", background="#e1f0ff", font=("Segoe UI", 12))
    style.configure("TButton", background="#007acc", foreground="white", font=("Segoe UI", 12, "bold"))
    style.map("TButton",
              background=[('active', '#005f99')],
              foreground=[('disabled', '#cccccc')])

    root.configure(background="#e1f0ff")
