import tkinter as tk


class MyApp:
    def __init__(self, root):
        self.root = root
        self.main_window()

    def main_window(self):
        self.background = tk.Frame(self.root, bg="red")
        self.background.place(relwidth=1, relheight=1)
