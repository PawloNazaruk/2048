import tkinter as tk
import colors as c
from game_functionality import *
from random import randint
from pprint import pprint


class MyApp:
    def __init__(self, root):
        self.root = root
        self.board_GUI = []
        n = 4
        self.board_base = [[0 for i in range(n)] for j in range(n)]

        self.menu_bar()
        self.make_score()
        self.make_board()


        self.update_board()

    def make_score(self):
        self.score_frame = tk.Frame(self.root)
        self.score_frame.place(relx=0.5, y=45, anchor="center")
        tk.Label(self.score_frame, text="Score", font=c.SCORE_FONT).grid(row=0)

        self.score_label = tk.Label(self.score_frame, text="0", font=c.SCORE_LABEL_FONT)
        self.score_label.grid(row=1)

    def make_board(self):
        self.grid_frame = tk.Frame(self.root, bg=c.GRID_COLOR)
        self.grid_frame.grid(pady=(100, 0))
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(self.grid_frame, bg=c.EMPTY_CELL_COLOR, width=140, height=140)
                cell_frame.grid(row=i, column=j, padx=5, pady=5)

                cell_number = tk.Label(self.grid_frame, bg=c.EMPTY_CELL_COLOR, anchor="center")
                cell_number.grid(row=i, column=j)

                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.board_GUI.append(row)

    def update_board(self):
        pprint(self.board_base)
        numbers = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
        for i, row in enumerate(self.board_base):
            for j in row:
                if j in numbers:
                    self.board_GUI[i][j]['frame'].config(bg=c.CELL_COLORS[j])
                    self.board_GUI[i][j]['number'].config(bg=c.CELL_COLORS[j], text=str(j), font=c.CELL_NUMBER_FONTS[j])
                else:
                    self.board_GUI[i][j]['frame'].config(bg=c.EMPTY_CELL_COLOR)
                    self.board_GUI[i][j]['number'].config(bg=c.EMPTY_CELL_COLOR, text="")

    def menu_bar(self):
        menu_bar = tk.Menu(self.root)
        menu_bar.add_command(label="Restart", command=print("Restart"))
        menu_bar.add_command(label="Help", command=print("Help"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.board_base})"
