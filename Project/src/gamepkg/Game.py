from py_compile import main
import tkinter as tk
from tkinter import messagebox
import random

# ==========================
# ตั้งค่าเกม
# ==========================
ROWS = 4
COLS = 4
TIME_LIMIT = 60
def rungame():
    root = tk.Tk()
    game = NumberMatchGame(root)
    root.mainloop()
class NumberMatchGame:

    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Number Matching Game")
        self.root.geometry("520x620")
        self.root.resizable(False, False)

        self.time_left = TIME_LIMIT

        self.first_btn = None
        self.second_btn = None
        self.first_num = None

        self.lock = False
        self.score = 0

        self.create_ui()
        self.new_game()

    # ==========================
    # สร้าง UI
    # ==========================
    def create_ui(self):

        top = tk.Frame(self.root)
        top.pack(pady=10)

        self.time_label = tk.Label(
            top,
            text="เวลา : 60",
            font=("Arial", 16, "bold"),
            fg="red"
        )
        self.time_label.grid(row=0, column=0, padx=20)

        self.score_label = tk.Label(
            top,
            text="คู่ที่จับได้ : 0 / 8",
            font=("Arial", 16, "bold")
        )
        self.score_label.grid(row=0, column=1, padx=20)

        self.restart_btn = tk.Button(
            self.root,
            text="🔄 รีเกม",
            font=("Arial", 14, "bold"),
            command=self.new_game
        )
        self.restart_btn.pack(pady=5)

        self.frame = tk.Frame(self.root)
        self.frame.pack()

    # ==========================
    # เริ่มเกมใหม่
    # ==========================
    def new_game(self):

        if hasattr(self, "timer"):
            self.root.after_cancel(self.timer)

        self.time_left = TIME_LIMIT
        self.score = 0

        self.first_btn = None
        self.second_btn = None
        self.first_num = None

        self.lock = False

        self.time_label.config(text=f"เวลา : {self.time_left}")
        self.score_label.config(text="คู่ที่จับได้ : 0 / 8")

        for widget in self.frame.winfo_children():
            widget.destroy()

        numbers = list(range(1, 9)) * 2
        random.shuffle(numbers)

        self.buttons = []

        index = 0

        for r in range(ROWS):
            for c in range(COLS):

                btn = tk.Button(
                    self.frame,
                    text="?",
                    font=("Arial", 22, "bold"),
                    width=5,
                    height=2,
                    bg="SystemButtonFace",
                    fg="black"
                )

                btn.number = numbers[index]
                btn.revealed = False

                btn.config(command=lambda b=btn: self.click(b))

                btn.grid(row=r, column=c, padx=5, pady=5)

                self.buttons.append(btn)

                index += 1

        self.countdown()

    # ==========================
    # คลิกการ์ด
    # ==========================
    def click(self, btn):

        if self.lock:
            return

        if btn.revealed:
            return

        btn.config(text=str(btn.number))
        btn.revealed = True

        if self.first_btn is None:
            self.first_btn = btn
            self.first_num = btn.number
            return

        self.second_btn = btn
        self.lock = True

        # ===== จับคู่ถูก =====
        if self.first_num == btn.number:

            self.first_btn.config(bg="lime green", fg="white")
            self.second_btn.config(bg="lime green", fg="white")

            self.score += 1

            self.score_label.config(
                text=f"คู่ที่จับได้ : {self.score} / 8"
            )

            self.first_btn = None
            self.second_btn = None
            self.first_num = None
            self.lock = False

            if self.score == 8:
                messagebox.showinfo("🎉 ชนะ", "ยินดีด้วย คุณจับคู่ครบแล้ว!")

                self.root.after(500, self.new_game)

        # ===== จับคู่ผิด =====
        else:

            self.first_btn.config(bg="red", fg="white")
            self.second_btn.config(bg="red", fg="white")

            self.root.after(700, self.hide_cards)

    # ==========================
    # ซ่อนการ์ดเมื่อจับคู่ผิด
    # ==========================
    def hide_cards(self):

        self.first_btn.config(
            text="?",
            bg="SystemButtonFace",
            fg="black"
        )

        self.second_btn.config(
            text="?",
            bg="SystemButtonFace",
            fg="black"
        )

        self.first_btn.revealed = False
        self.second_btn.revealed = False

        self.first_btn = None
        self.second_btn = None
        self.first_num = None

        self.lock = False

    # ==========================
    # ตัวจับเวลา
    # ==========================
    def countdown(self):

        self.time_label.config(
            text=f"เวลา : {self.time_left}"
        )

        if self.time_left <= 0:

            messagebox.showinfo(
                "⏰ หมดเวลา",
                "หมดเวลา! เกมจะเริ่มใหม่"
            )

            self.new_game()
            return

        self.time_left -= 1

        self.timer = self.root.after(
            1000,
            self.countdown
        )

# ==========================
# เริ่มโปรแกรม
# ==========================
root = tk.Tk()

game = NumberMatchGame(root)

root.mainloop()


if __name__ == "__main__":
    main()
    print(__name__)