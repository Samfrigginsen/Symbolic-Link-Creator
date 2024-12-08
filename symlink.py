import os
import tkinter as tk
from tkinter import filedialog

# Define source_entry and target_entry globally
source_entry = None
target_entry = None

def create_symlink(source_path, target_path):
    try:
        os.symlink(source_path, target_path)
        print(f"Symbolic link created: {target_path}")
    except Exception as e:
        print(f"Error creating symbolic link: {e}")

def browse_source_path():
    source_path = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, source_path)

def browse_target_path():
    target_path = filedialog.asksaveasfilename(defaultextension=".link", filetypes=[("Symbolic Link files", "*.link")])
    target_entry.delete(0, tk.END)
    target_entry.insert(0, target_path)

def create_symlink_gui():
    global source_entry, target_entry  # Declare these as global variables

    root = tk.Tk()
    root.title("Symbolic Link Creator")

    source_label = tk.Label(root, text="Source Path:")
    source_label.grid(row=0, column=0, padx=10, pady=10)

    source_entry = tk.Entry(root, width=50)
    source_entry.grid(row=0, column=1, padx=10, pady=10)

    source_browse_button = tk.Button(root, text="Browse", command=browse_source_path)
    source_browse_button.grid(row=0, column=2, padx=10, pady=10)

    target_label = tk.Label(root, text="Target Path:")
    target_label.grid(row=1, column=0, padx=10, pady=10)

    target_entry = tk.Entry(root, width=50)
    target_entry.grid(row=1, column=1, padx=10, pady=10)

    target_browse_button = tk.Button(root, text="Browse", command=browse_target_path)
    target_browse_button.grid(row=1, column=2, padx=10, pady=10)

    create_button = tk.Button(root, text="Create Symbolic Link", command=lambda: create_symlink(source_entry.get(), target_entry.get()))
    create_button.grid(row=2, column=1, pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_symlink_gui()
