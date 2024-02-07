import tkinter as tk
from tkinter import messagebox

def перевірка_переможця():
    for i in range(3):
        if кнопки[i][0]['text'] == кнопки[i][1]['text'] == кнопки[i][2]['text'] != '':
            return кнопки[i][0]['text ']
        if кнопки[0][i]['text'] == кнопки[1][i]['text'] == кнопки[2][i]['text'] != '':
            return кнопки[0][i]['text']
    if кнопки[0][0]['text'] == кнопки[1][1]['text'] == кнопки[2][2]['text'] != '':
        return кнопки[0][0]['text']
    if кнопки[0][2]['text'] == кнопки[1][1]['text'] == кнопки[2][0]['text'] != '':
        return кнопки[0][2]['text ']
    return None

def клік(row, col):
    global гравець
    if кнопки[row][col]['text'] == '':
        кнопки[row][col]['text'] = гравець
        переможець = перевірка_переможця()
        if переможець:
            messagebox.showinfo("Вітання!", f"Гравець {переможець} переміг!")
            скинути_дошку()
        elif all(кнопки[i][j]['text'] != '' for i in range(3) for j in range(3)):
            messagebox.showinfo("Нічия!", "Нічия!")
            скинути_дошку()
        else:
            гравець = 'X' if гравець == 'O' else 'O'

def скинути_дошку():
    global гравець
    for i in range(3):
        for j in range(3):
            кнопки[i][j]['text'] = ''
    гравець = 'X'

# Створення вікна
root = tk.Tk()
root.title("Крестики-нолики")

# Ініціалізація кнопок
кнопки = [[None, None, None] for _ in range(3)]
for i in range(3):
    for j in range(3):
        кнопки[i][j] = tk.Button(root, text='', font=('Arial', 20), width=4, height=2,
                                 command=lambda row=i, col=j: клік(row, col))
        кнопки[i][j].grid(row=i, column=j)

гравець = 'x'

root.mainloop()
