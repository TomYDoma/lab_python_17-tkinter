import tkinter as tk
from math import*
from tkinter.ttk import Treeview

import numpy as np
from PIL import ImageTk, Image


window = tk.Tk()
window.title("Лабораторная работа №4 | Шуляк А.А.")
window.geometry("600x500")
window.resizable(width=False, height=False)
window["bg"] = "#FFCCCC"


def fun_clear_text():
    label_answer_1.config(text="")

def fun_decision():
    fun_clear_text()
    try:
        number = []
        a = float(entry_a.get())
        b = float(entry_b.get())
        n = float(entry_n.get())

        k = (b - a) / n
        m = 0
        for x in np.arange(b, a - 0.5, -k):
            m += 1
            if x < -3:
                y = 1
                ab = (m, x, y)
                number.append(ab)
            elif -3 <= x <= -1:
                y = -sqrt(pow(-2, 2) - pow(x + 1, 2))
                ab = (m, x, y)
                number.append(ab)
            elif -1 < x <= 2:
                y = -2
                ab = (m, x, y)
                number.append(ab)
            elif x > 2:
                y = x - 4
                ab = (m, x, y)
                number.append(ab)

        newWindow = tk.Toplevel(window)
        # определяем столбцы
        columns = ("n", "x", "y")

        tree = Treeview(newWindow, columns=columns, show="headings")
        tree.grid(column=1, row=2)

        # определяем заголовки
        tree.heading("n", text="N")
        tree.heading("x", text="X")
        tree.heading("y", text="Y")

        tree.column("#1", width=70)
        tree.column("#2", width=70)
        tree.column("#3", width=70)

        # добавляем данные
        for i in number:
            tree.insert(parent='', index='end', values=i)

    except:
        label_answer_1["text"] = "Ввод некоректен"


frame_widjets = tk.Frame(window)
frame_widjets["bg"] = "#FFCCCC"

label_one = tk.Label(frame_widjets, text="Вывод таблицы значений функции y=f(x), заданной графиком:", bg="#FFCCCC", font=("Arial", 10))
label_one.grid(column=0, row=0)

image_one = Image.open("image/lab2/LAB_2.png")
pil_image = image_one.resize((300, 150))
frame_widjets.image_one = ImageTk.PhotoImage(pil_image)
image_Label_one = tk.Label(frame_widjets, image=frame_widjets.image_one, bg="#FFCCCC")
image_Label_one.grid(column=0, row=1)



label_a = tk.Label(frame_widjets, text="Введите a:", bg="#FFCCCC", font=("Arial", 15))
label_a.grid(column=0, row=2)

entry_a = tk.Entry(frame_widjets, font=("Arial", 10))
entry_a.grid(column=0, row=3)

label_b = tk.Label(frame_widjets, text="Введите b:", bg="#FFCCCC", font=("Arial", 15))
label_b.grid(column=0, row=4)

entry_b = tk.Entry(frame_widjets, font=("Arial", 10))
entry_b.grid(column=0, row=5)

label_n = tk.Label(frame_widjets, text="Введите N:", bg="#FFCCCC", font=("Arial", 15))
label_n.grid(column=0, row=6)

entry_n = tk.Entry(frame_widjets, font=("Arial", 10))
entry_n.grid(column=0, row=7)

btn_launch = tk.Button(frame_widjets, text="Запуск", command=fun_decision, bg="#FF3399", font=("Arial", 20))
btn_launch.grid(column=0, row=8, pady=10)

label_answer_1 = tk.Label(frame_widjets, bg="#FFCCCC", font=("Arial", 15))
label_answer_1.grid(column=0, row=9)


frame_widjets.pack()


window.mainloop()

