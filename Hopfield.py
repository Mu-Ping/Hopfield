# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:53:56 2020
@author: Mu-Ping
"""

import tkinter as tk


def create_grid(c, c_list):  
    w = 240
    h = 240
    index=0
    # Create rectangles on whole window
    for x in range(5, w, 20):
        for y in range(5, h, 20):
            box = (x, y, x+20, y+20)
            c_list[index].append(c.create_rectangle(box, fill='white'))
        index+=1



window = tk.Tk()
window.geometry("1000x450")
window.resizable(False, False)
window.title("感知機訓練器")

plt1 = tk.Frame(window)
plt1.grid(row=0, column=0)

c1_list=[[] for _ in range(12)]
c1 = tk.Canvas(plt1, height=250, width=250)
c1.grid(row=0,column=0)

c2_list=[[] for _ in range(12)]
c2 = tk.Canvas(plt1, height=250, width=250)
c2.grid(row=0,column=1)

c3_list=[[] for _ in range(12)]
c3 = tk.Canvas(plt1, height=250, width=250)
c3.grid(row=0,column=2)

create_grid(c1, c1_list)
create_grid(c2, c2_list)
create_grid(c3, c3_list)

window.mainloop()