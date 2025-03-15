import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox

def wipe_file(file_path, passes=3):
    if not os.path.exists(file_path):
        messagebox.showerror("Error", "File not found!")
        return

    file_size = os.path.getsize(file_path)

    with open(file_path, "wb") as file:
        for i in range(passes):
            if i % 2 == 0:
                file.seek(0)
                file.write(os.urandom(file_size))  #random bytes
            else:
                file.seek(0)
                file.write(b"\x00" * file_size)  #zero-fill overwrite

    os.remove(file_path)
    messagebox.showinfo("Success", f"{file_path} securely wiped and deleted.")

def wipe_folder(folder_path, passes=3):
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "Folder not found!")
        return
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            wipe_file(file_path, passes)
    
    messagebox.showinfo("Success", f"All files in {folder_path} wiped and deleted.")

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        wipe_file(file_path)

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        wipe_folder(folder_path)

root = tk.Tk()
root.title("Secure Data Wiper")
root.geometry("400x200")

tk.Label(root, text="Secure Data Wiper", font=("Arial", 14, "bold")).pack(pady=10)
tk.Button(root, text="Wipe a File", command=select_file, fg="white", bg="red").pack(pady=5)
tk.Button(root, text="Wipe a Folder", command=select_folder, fg="white", bg="red").pack(pady=5)

root.mainloop()
