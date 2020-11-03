import tkinter as tk
from logic import *


class MyApp:
    def __init__(self, root):
        self.root = root
        self.menu_bar()
        self.main_window()

    def menu_bar(self):
        menu_bar = tk.Menu(self.root)
        menu_bar.add_command(label="Restart", command=print("Restart"))
        menu_bar.add_command(label="Help", command=print("Help"))
        self.root.config(menu=menu_bar)

    def main_window(self):
        self.background = tk.Frame(self.root, bg="red")
        self.background.place(relwidth=1, relheight=1)
