import tkinter as tk
from tkinter import messagebox
from pprint import pprint

import colors as c
import gameplay_logic as gp


class MyApp:
    """ Tkinter GUI object.

    Attributes:
        root - root of the app
        board_base - Matrix with integers values for logic/math operations.
        board_GUI - Matrix which holds as an element dict with Label and Frame tkinter objects to create GUI.

        score - An integer count for current gained score.

    """
    def __init__(self, root):
        """Inits MyApp with """
        self.root = root
        n = 4
        self.board_base = [[0 for i in range(n)] for j in range(n)]
        self.board_GUI = []

        self.score = tk.IntVar()
        self.make_score()
        self.make_board()

        gp.start_game(self.board_base)
        self.update_GUI()
        self.bind_movement()


    def make_score(self):
        """Display Score part of the GUI.

        Attributes:
            score_frame - Tkinter Frame object, sets placement of the score on the app view.
            score_label - Tkinter Label object displays current score value.

        """
        self.score_frame = tk.Frame(self.root)
        self.score_frame.place(relx=0.5, y=45, anchor="center")
        tk.Label(self.score_frame, text="Score", font=c.SCORE_FONT).grid(row=0)
        self.score_label = tk.Label(self.score_frame, text=str(0), font=c.SCORE_LABEL_FONT)
        self.score_label.grid(row=1)

    def make_board(self):
        """Display empty board part of the GUI and creates board_GUI.

        Attributes:
            grid_frame - Tkinter Frame object, sets placement of the board on the app view.
            cell_frame - Tkinter Frame object, sets placement of the cell on the board view.
            cell_number - Tkinter Label object, styles and displays number of the cell.
        """
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

    def update_GUI(self):
        """Updates GUI by actual board_base and score values."""
        numbers = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
        for i, row in enumerate(self.board_base):
            for j, val in enumerate(row):
                if val in numbers:
                    self.board_GUI[i][j]['frame'].config(bg=c.CELL_COLORS[val])
                    self.board_GUI[i][j]['number'].config(bg=c.CELL_COLORS[val], text=str(val), font=c.CELL_NUMBER_FONTS[val])
                else:
                    self.board_GUI[i][j]['frame'].config(bg=c.EMPTY_CELL_COLOR)
                    self.board_GUI[i][j]['number'].config(bg=c.EMPTY_CELL_COLOR, text="")
        self.score_label.config(text=self.score.get())

    def bind_movement(self):
        """Bind WSAD and ARROWS buttons for movements of the board."""
        self.root.bind("<Up>", self.movement_button_clicked)
        self.root.bind("<Down>", self.movement_button_clicked)
        self.root.bind("<Left>", self.movement_button_clicked)
        self.root.bind("<Right>", self.movement_button_clicked)
        self.root.bind("<w>", self.movement_button_clicked)
        self.root.bind("<s>", self.movement_button_clicked)
        self.root.bind("<a>", self.movement_button_clicked)
        self.root.bind("<d>", self.movement_button_clicked)

    def movement_button_clicked(self, evt):
        """Pulls out keyboard button name and uses it as a direction to perform board movement.

        Arguments:
            evt - Tkinter event raised after clicking binned keyboard button.
            keyboard_button - An string name of the keyboard button.
        """
        keyboard_button = evt.keysym
        self.move_board_elements(keyboard_button)

    def move_board_elements(self, direction):
        """Starts movement math/logic of the matrix in the given direction when performed updates score and board_base.

        At start the function checks if move in any direction is possible if
        not then game over occurs. The function sets mechanic that only after
        moving elements new elements can be spawned.

        Arguments:
            direction - An string name of the board movement direction.
            new_board_base - Matrix with integers values with its elements moved to the given direction.
            gained_score - An integer count of the new points scored.
        """
        to = {
            "Left": gp.move_elements_left(self.board_base),
            "a": gp.move_elements_left(self.board_base),
            "Right": gp.move_elements_right(self.board_base),
            "d": gp.move_elements_right(self.board_base),

            "Up": gp.move_elements_up(self.board_base),
            "w": gp.move_elements_up(self.board_base),
            "Down": gp.move_elements_down(self.board_base),
            "s": gp.move_elements_down(self.board_base),
        }

        if gp.game_over(self.board_base) == "END":
            messagebox.showinfo("Game Over", f"Yous score: {self.score.get()}")

        if self.board_base == to[direction][0]:
            return

        new_board_base, gained_score = to[direction]
        self.board_base = new_board_base
        self.board_base = gp.add_element(self.board_base)
        self.score.set(self.score.get() + gained_score)
        self.update_GUI()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.board_base})"
