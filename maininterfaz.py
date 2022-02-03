
import tkinter as tk
from tkinter import *
from App import App
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('usuariosBD.sqlite')
    app = App()
    app.mainloop()