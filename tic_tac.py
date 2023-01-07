# 1. Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

from tkinter import *
root = Tk()
root.title('Крестики-Нолики')
root.geometry('350x350')

games = Canvas(root, width=400, height=400)
games.place(x=30, y=30)

for i in range(0, 9):
    x = i // 3 * 100
    y = i % 3 * 100
    games.create_rectangle(x, y, x + 100, y + 100,
    width=3,
    outline='gray',
    fill='white',
    activefill='gray')

def add_x(column, row):
    x = 10 + 100 * column
    y = 10 + 100 * row
    games.create_line(x, y, x + 80, y + 80, width=8, fill='green')
    games.create_line(x, y + 80, x + 80, y, width=8, fill='green')

def add_o(column, row):
    x = 10 + 100 * column
    y = 10 + 100 * row
    games.create_oval(x, y, x + 80, y + 80, width=8, outline='red')

def click(event):
    column = event.x // 100
    row = event.y // 100
    add_x(column, row)
games.bind('<Button-1>', click)

def click1(event):
    column = event.x // 100
    row = event.y // 100
    add_o(column, row) 
games.bind('<Button-2>', click1)

root.mainloop()
