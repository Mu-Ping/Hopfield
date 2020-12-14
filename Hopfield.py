# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:53:56 2020
@author: Mu-Ping
"""

import tkinter as tk
from tkinter import ttk

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
window.geometry("950x600")
window.resizable(False, False)
window.title("Hopfield")


plt1 = tk.Frame(window)
plt1.grid(row=0, column=0)
action_bar = tk.Frame(plt1)
action_bar.grid(row=0, column=0, padx=15)
tk.Label(action_bar, font=("微軟正黑體", 15, "bold"), text="選擇訓練資料").grid(row=0, column=0, sticky=tk.W)
update_combobox = ttk.Combobox(action_bar, value=['Basic_Training.txt','Bonus_Training.txt'], state="readonly", width=15) #readonly為只可讀狀態
update_combobox.grid(row=1, column=0, sticky=tk.W, pady=10)
update_combobox.current(0) #預設Combobox為index0
c1_1_list=[[] for _ in range(12)]
c1_1 = tk.Canvas(plt1, height=250, width=250)
c1_1.grid(row=0,column=1)
c1_2_list=[[] for _ in range(12)]
c1_2 = tk.Canvas(plt1, height=250, width=250)
c1_2.grid(row=0,column=2)
c1_3_list=[[] for _ in range(12)]
c1_3 = tk.Canvas(plt1, height=250, width=250)
c1_3.grid(row=0,column=3)
create_grid(c1_1, c1_1_list)
create_grid(c1_2, c1_2_list)
create_grid(c1_3, c1_3_list)


plt2 = tk.Frame(window)
plt2.grid(row=1, column=0)
tk.Label(plt2, font=("微軟正黑體", 15, "bold"), text="對應測試資料").grid(row=0, column=0, sticky=tk.W, padx=15)
c2_1_list=[[] for _ in range(12)]
c2_1 = tk.Canvas(plt2, height=250, width=250)
c2_1.grid(row=0,column=1)
c2_2_list=[[] for _ in range(12)]
c2_2 = tk.Canvas(plt2, height=250, width=250)
c2_2.grid(row=0,column=2)
c2_3_list=[[] for _ in range(12)]
c2_3 = tk.Canvas(plt2, height=250, width=250)
c2_3.grid(row=0,column=3)
create_grid(c2_1, c2_1_list)
create_grid(c2_2, c2_2_list)
create_grid(c2_3, c2_3_list)

window.mainloop()