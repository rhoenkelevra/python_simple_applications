# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 13:44:11 2021

@author: user24
"""

import tkinter as tk
import tkinter.filedialog as fd

root = tk.Tk()
root.withdraw()

file = fd.askopenfilename(
    title="ファイルを選んでください。",
    filetypes=[("TEXT", ".txt"), ("TEXT", ".py"), ("HTML", ".html")]
)

if file:
    with open(file, "r", encoding="utf_8") as fileobj:
        text = fileobj.read()
        print(text)


