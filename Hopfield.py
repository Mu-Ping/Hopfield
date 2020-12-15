# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:53:56 2020
@author: Mu-Ping
"""
import os
import tkinter as tk
from tkinter import ttk


def create_grid(c, col, row, file=None, color=True): #https://www.coder.work/article/4933449
    zeor_color= '#D0D0D0' if color else "white"
    one_color= '#9D9D9D'  if color else "black"

    c.delete('all')
    file = list(file)
    for y in range(row):
        for x in range(col):
            pixel = file.pop(0)
            if(pixel=="0"):
                c.create_rectangle((7*x+2, 7*y+2, 7*x+9, 7*y+9), fill = zeor_color) #pixel起始x=2 ；y=2
            elif(pixel=="1"):
                c.create_rectangle((7*x+2, 7*y+2, 7*x+9, 7*y+9), fill = one_color)
                
def focus(event):
    for i in range(109):
        if(event.widget.itemcget(i ,'fill')=='#9D9D9D'):  #取得舊有屬性
            event.widget.itemconfig(i, fill='black')
        elif(event.widget.itemcget(i ,'fill')=='#D0D0D0'):
            event.widget.itemconfig(i, fill='white')
def unfocus(event):
    for i in range(109):
        if(event.widget.itemcget(i ,'fill')=='black'):  #取得舊有屬性
            event.widget.itemconfig(i, fill='#9D9D9D')
        elif(event.widget.itemcget(i ,'fill')=='white'):
            event.widget.itemconfig(i, fill='#D0D0D0')    
def readdata():           
    basic=["Basic_Training.txt", "Basic_Testing.txt"]
    bonus=["Bonus_Training.txt", "Bonus_Testing.txt"]
    data_format = [(basic, 12, basic_word),(bonus, 10, bonus_word)]
    for data in data_format:
        for i in data[0]:
            with open(os.getcwd()+'/Hopfield_dataset/'+ i, 'r', encoding='UTF-8') as file:
                word=[]
                pixel=""
                row=0
                for j in file.readlines():
                    if(row==data[1]):
                        word.append(pixel)
                        pixel=""
                        row=0
                        continue
                    pixel+=j.replace(" ","0").replace("\n","")
                    row+=1
            data[2].append(word)
def choose_test(event):
    file=""
    for i in range(109):
       if(event.widget.itemcget(i ,'fill')=='black'):  #取得舊有屬性
           file+='1'
       elif(event.widget.itemcget(i ,'fill')=='white'):
           file+='0' 

    if(len(file)%9==0): #反推canvas大小。也可以透過更改Canvas原始碼將資訊存進物件
        row=12
        col=9
    else:
        row=10
        col=10

    create_grid(test_data, col, row, file, False)
          
def GUI():
    plt_basic_train = tk.Frame(window)
    plt_basic_train.grid(row=0, column=0)
    plt_basic_test = tk.Frame(window)
    plt_basic_test.grid(row=0, column=1)
    plt_basic = [plt_basic_train, plt_basic_test]
    tk.Label(plt_basic_train, font=("微軟正黑體", 12, "bold"), text="Basic_Training").grid(row=0, column=0, columnspan=3)
    tk.Label(plt_basic_test, font=("微軟正黑體", 12, "bold"), text="Basic_Testing").grid(row=0, column=0, columnspan=3)
    for i in range(2):
        for j in range(3):
            c = tk.Canvas(plt_basic[i], height=85, width=75)
            c.grid(row=1,column=j)
            create_grid(c, 9, 12, basic_word[i][j]) #Basic資料集為9x12
            c.bind("<Enter>", focus)
            c.bind("<Leave>", unfocus)
            c.bind("<Button-1>", choose_test)
#--------------------------------------------------
    plt_bonus_train = tk.Frame(window)
    plt_bonus_train.grid(row=1, column=0, padx=20)
    plt_bonus_test = tk.Frame(window)
    plt_bonus_test.grid(row=1, column=1)
    plt_bonus=[plt_bonus_train, plt_bonus_test]
    tk.Label(plt_bonus_train, font=("微軟正黑體", 12, "bold"), text="Bonus_Training").grid(row=0, column=0, columnspan=3)
    tk.Label(plt_bonus_test, font=("微軟正黑體", 12, "bold"), text="Bonus_Testing").grid(row=0, column=0, columnspan=3)
    for i in range(2):
        rowindex=0
        for j in range(15):
            if(j%3==0): rowindex+=1
            c = tk.Canvas(plt_bonus[i], height=75, width=75)
            c.grid(row=rowindex, column=j%3)
            create_grid(c, 10, 10, bonus_word[i][j]) #Bonus資料集為10x10
            c.bind("<Enter>", focus)
            c.bind("<Leave>", unfocus)
            c.bind("<Button-1>", choose_test)
#--------------------------------------------------
    action_bar = tk.Frame(window)
    action_bar.grid(row=0, column=2, rowspan=2, padx=25)
    tk.Label(action_bar, font=("微軟正黑體", 12, "bold"), text="選擇訓練資料集").grid(row=0, column=0)
    data_combobox = ttk.Combobox(action_bar, value=["Basic_Training","Bonus_Training"], state="readonly", width=15) #readonly為只可讀狀態
    data_combobox.grid(row=1, column=0, sticky=tk.W)
    data_combobox.current(0) #預設Combobox為index0
    btn = tk.Button(action_bar, text='開始訓練')
    btn.grid(row=2, sticky=tk.E+tk.W, pady=10)
    
    tk.Label(action_bar, font=("微軟正黑體", 12, "bold"), text="選擇測試資料").grid(row=3, column=0)
    global test_data
    test_data = tk.Canvas(action_bar, height=85, width=75)
    test_data.grid(row=4, column=0)

basic_word=[]
bonus_word=[]
test_data=None
window = tk.Tk()
window.geometry("720x550")
window.resizable(False, False)
window.title("Hopfield")
readdata()
GUI()
window.mainloop()
