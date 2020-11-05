import tkinter as tk
import colors as c
from game_functionality import *


class MyApp:
    def __init__(self, root):
        self.root = root

        self.score_frame = tk.Frame(self.root)
        self.score_frame.place(relx=0.5, y=45, anchor="center")

        self.grid_frame = tk.Frame(self.root, bg=c.GRID_COLOR)
        self.grid_frame.grid(pady=(100, 0))

        self.menu_bar()
        self.display_score()
        self.display_board()

        # checks
        self.cells[0][0]['frame'].config(bg=c.CELL_COLORS[32])
        self.cells[0][0]['number'].config(bg=c.CELL_COLORS[32], text="32")

    def display_score(self):
        score_frame = tk.Frame(self.root)
        score_frame.place(relx=0.5, y=45, anchor="center")
        tk.Label(score_frame, text="Score", font=c.SCORE_FONT).grid(row=0)
        self.score_label = tk.Label(score_frame, text="0", font=c.SCORE_LABEL_FONT)
        self.score_label.grid(row=1)

    def display_board(self):
        self.cells = []
        for row in range(4):
            cells_row = []
            for col in range(4):
                cell_frame = tk.Frame(self.grid_frame, bg=c.EMPTY_CELL_COLOR, width=140, height=140)
                cell_frame.grid(row=row, column=col, padx=5, pady=5)

                cell_number = tk.Label(self.grid_frame, bg=c.EMPTY_CELL_COLOR, anchor="center")
                cell_number.grid(row=row, column=col)
                cell_data = {"frame": cell_frame, "number": cell_number}
                cells_row.append(cell_data)
            self.cells.append(cells_row)

    def menu_bar(self):
        menu_bar = tk.Menu(self.root)
        menu_bar.add_command(label="Restart", command=print("Restart"))
        menu_bar.add_command(label="Help", command=print("Help"))
        self.root.config(menu=menu_bar)

