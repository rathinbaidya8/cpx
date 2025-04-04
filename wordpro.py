import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("CPX GALAXY")
root.geometry("800x600")

# Text Area
text_area = tk.Text(root, wrap='word', font=('Arial', 12))
text_area.pack(expand=1, fill='both')

# File Open Function
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

# File Save Function
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text_area.get(1.0, tk.END))

# Menu Bar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()
