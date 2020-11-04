import tkinter as tk
import colors as c
from logic import *


class MyApp:
    def __init__(self, root):
        self.root = root

        self.score_frame = tk.Frame(self.root)
        self.score_frame.place(relx=0.5, y=45, anchor="center")

        self.board_background_frame = tk.Frame(self.root, bg=c.GRID_COLOR)
        self.board_background_frame.grid(pady=(100, 0))

        self.menu_bar()
        self.display_score()
        self.display_board()

    def display_score(self):
        score_frame = tk.Frame(self.root)
        score_frame.place(relx=0.5, y=45, anchor="center")
        tk.Label(score_frame, text="Score", font=c.SCORE_FONT).grid(row=0)
        self.score_label = tk.Label(score_frame, text="0", font=c.SCORE_LABEL_FONT)
        self.score_label.grid(row=1)

    def display_board(self):
        for row in range(4):
            for col in range(4):
                cell_frame = tk.Frame(
                    self.board_background_frame,
                    bg=c.EMPTY_CELL_COLOR,
                    width=140,
                    height=140
                )
                cell_frame.grid(row=row, column=col, padx=5, pady=5)

                cell_number = tk.Label(cell_frame, text=f"{row}x{col}", anchor="center")
                cell_number.place(relwidth=1, relheight=1)


    def menu_bar(self):
        menu_bar = tk.Menu(self.root)
        menu_bar.add_command(label="Restart", command=print("Restart"))
        menu_bar.add_command(label="Help", command=print("Help"))
        self.root.config(menu=menu_bar)
