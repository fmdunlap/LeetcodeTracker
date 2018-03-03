import os
import random
import json
import pprint
import milsUtils
import webbrowser
import MainWindow
import LeetData

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk
    from Tkinter import messagebox
import pathlib

def setupWindow(main):
    main.title(LeetData.WIN_TITLE)
    main.geometry("%ix%i" % (LeetData.WIN_WIDTH, LeetData.WIN_HEIGHT))
    main.resizable(0,0)
    main.pack_propagate(0)

LeetData.parseSaveFile()
root = tk.Tk()
setupWindow(root)
mw = MainWindow.mainWindow(root, tk, LeetData.jsonData)

root.protocol("WM_DELETE_WINDOW", MainWindow.mainWindow.on_closing)
root.mainloop()