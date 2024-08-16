import tkinter as tk
import random
from typing import List
from tkinter import messagebox
import time


class Minesweeper:
    master: tk.Tk
    rows: int
    cols: int
    mines: int
    board: List[List[int]]
    buttons: List[List[tk.Button | None]]
    game_over = True

    def __init__(self, master, rows=10, cols=10, mines=10):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines

        self.generate_field()
        self.generate_mines()
        self.generate_numbers()
        self.generate_buttons()

        self.control_frame = tk.Frame(master)
        self.control_frame.grid(row=rows, column=0, columnspan=cols)

        self.restart_button = tk.Button(self.control_frame, text="Restart", command=self.restart)
        self.restart_button.pack(side=tk.LEFT)

        self.start_time = time.time()
        self.timer = tk.Label(self.control_frame, text="Time: 0")
        self.timer.pack(side=tk.RIGHT)
        self.update_timer()

        self.game_over = False

    def generate_buttons(self):
        self.buttons = [[None for c in range(self.cols)] for r in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                button = tk.Button(self.master,
                                   text="",
                                   width=2,
                                   height=1,
                                   bg="lightgrey",
                                   command=lambda r=r, c=c: self.reveal(r, c))
                button.bind("<Button-3>", lambda event, r=r, c=c: self.flag(event, r, c))
                button.grid(row=r, column=c)
                self.buttons[r][c] = button

    def generate_field(self):
        self.board = [[0 for c in range(self.cols)] for r in range(self.rows)]

    def generate_mines(self):
        count = 0
        while count < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if self.board[r][c] == 0:
                self.board[r][c] = -1
                count += 1

    def generate_numbers(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == -1:
                    continue
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols:
                            if self.board[r + dr][c + dc] == -1:
                                self.board[r][c] += 1

    def reveal(self, r, c):
        if self.game_over:
            return

        if self.buttons[r][c]["text"] != "":
            return

        if self.board[r][c] == -1:
            self.reveal_mines()
            self.game_over = True
            messagebox.showinfo(title="Конец игры", message="Вы подорвались D:")
            return

        self.buttons[r][c].config(text=self.board[r][c], bg='SystemButtonFace')
        if self.board[r][c] == 0:
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols:
                        self.reveal(r + dr, c + dc)

        if self.check_win():
            self.game_over = True
            messagebox.showinfo(title="Победа", message="Вы победили :D")

    def flag(self, event, r, c):
        if self.game_over:
            return

        if self.buttons[r][c]["text"] == "":
            self.buttons[r][c].config(text="F", bg='yellow')
        elif self.buttons[r][c]["text"] == "F":
            self.buttons[r][c].config(text="", bg='lightgrey')

    def check_win(self):
        opened = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] != -1 and self.buttons[r][c]["text"] not in ["", "F"]:
                    opened += 1

        return opened == self.rows * self.cols - self.mines

    def reveal_mines(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == -1:
                    self.buttons[r][c].config(text="*", bg='red')

    def update_timer(self):
        if not self.game_over:
            self.timer.config(text=f"Time: {int(time.time() - self.start_time)}")
        self.master.after(1000, self.update_timer)

    def restart(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.buttons[r][c].config(text="", bg="lightgrey")

        self.game_over = False
        self.generate_field()
        self.generate_mines()
        self.generate_numbers()
        self.start_time = time.time()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Сапёр")
    ms = Minesweeper(root)
    root.mainloop()
