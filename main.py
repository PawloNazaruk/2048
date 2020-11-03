import tkinter as tk
from view import MyApp


def main():
    root = tk.Tk()
    root.geometry("600x600")
    root.title("2048")
    myapp = MyApp(root)

    root.mainloop()


if __name__ == __name__:
    main()
