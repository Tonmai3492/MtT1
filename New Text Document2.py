import tkinter as tk

# ฟังก์ชันเมื่อกดปุ่ม
def click(value):
    current = entry.get()

    if value == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif value == "C":
        entry.delete(0, tk.END)

    else:
        entry.insert(tk.END, value)


# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("320x420")
root.resizable(False, False)

# ช่องแสดงผล
entry = tk.Entry(root, font=("Arial", 22), justify="right", bd=8)
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# ปุ่มต่าง ๆ
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")

    for btn in row:
        b = tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 18),
            command=lambda x=btn: click(x)
        )
        b.pack(side="left", expand=True, fill="both", padx=2, pady=2)

root.mainloop()