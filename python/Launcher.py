import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

# กำหนดไฟล์ Python
PROGRAMS = {
    "Program 1": r"D:\python\testcode\Data.py",
    "Program 2": r"D:\python\testcode\Comment.py",
    "Program 3": r"D:\python\testcode\Numbers.py",
    "Program 4": r"D:\python\testcode\Multiple.py",
    "Program 5": r"D:\python\testcode\Variable.py",
}

def launch_program(file_path):
    if not os.path.isfile(file_path):
        messagebox.showerror("Error", f"ไม่พบไฟล์\n{file_path}")
        return

    try:
        subprocess.Popen([sys.executable, file_path])
    except Exception as e:
        messagebox.showerror("Error", str(e))

# สร้างหน้าต่าง
root = tk.Tk()
root.title("Python Program Launcher")
root.geometry("350x380")
root.resizable(False, False)

tk.Label(
    root,
    text="Python Program Launcher",
    font=("Arial", 16, "bold")
).pack(pady=15)

# ปุ่มเปิดโปรแกรม
for name, path in PROGRAMS.items():
    tk.Button(
        root,
        text=name,
        width=25,
        height=2,
        command=lambda p=path: launch_program(p)
    ).pack(pady=5)

# ปุ่มออก
tk.Button(
    root,
    text="ออก (Exit)",
    width=25,
    height=2,
    bg="red",
    fg="white",
    command=root.destroy
).pack(pady=15)

root.mainloop()