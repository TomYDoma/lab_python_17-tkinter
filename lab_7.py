import tkinter as tk
from math import*
from tkinter.ttk import Treeview

import numpy as np
from PIL import ImageTk, Image


window = tk.Tk()
window.title("Лабораторная работа №7 | Шуляк А.А.")
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
        N = float(entry_N.get())
        e = float(entry_e.get())

        k = (b - a) / N
        m = 0
        for x in np.arange(b, a - 0.5, -k):
            count = 0
            t = 0
            for n in range(0, 25):
                t = pow(x-1, n+1) / ((n+1) * pow(x, n+1))
                count += t
                if fabs(t) < e:
                    break
            m += 1

            ab = (m, x, count)
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

label_one = tk.Label(frame_widjets, text="Вывод таблицы значений функции y=f(x), которая  \n вычисляется как конечная сумма ряда Тейлора:", bg="#FFCCCC", font=("Arial", 10))
label_one.grid(column=0, row=0)


image_one = Image.open("image/lab6/LAB_6.png")
pil_image = image_one.resize((400, 60))
frame_widjets.image_one = ImageTk.PhotoImage(pil_image)
image_Label_one = tk.Label(frame_widjets, image=frame_widjets.image_one, bg="#FFCCCC")
image_Label_one.grid(column=0, row=1)


label_e = tk.Label(frame_widjets, text="Введите ε:", bg="#FFCCCC", font=("Arial", 15))
label_e.grid(column=0, row=2)
entry_e = tk.Entry(frame_widjets, font=("Arial", 10))
entry_e.grid(column=0, row=3)

label_a = tk.Label(frame_widjets, text="Введите a:", bg="#FFCCCC", font=("Arial", 15))
label_a.grid(column=0, row=4)
entry_a = tk.Entry(frame_widjets, font=("Arial", 10))
entry_a.grid(column=0, row=5)

label_b = tk.Label(frame_widjets, text="Введите b:", bg="#FFCCCC", font=("Arial", 15))
label_b.grid(column=0, row=6)
entry_b = tk.Entry(frame_widjets, font=("Arial", 10))
entry_b.grid(column=0, row=7)

label_N = tk.Label(frame_widjets, text="Введите N:", bg="#FFCCCC", font=("Arial", 15))
label_N.grid(column=0, row=8)
entry_N = tk.Entry(frame_widjets, font=("Arial", 10))
entry_N.grid(column=0, row=9)

btn_launch = tk.Button(frame_widjets, text="Запуск", command=fun_decision, bg="#FF3399", font=("Arial", 20))
btn_launch.grid(column=0, row=10, pady=10)

label_answer_1 = tk.Label(frame_widjets, bg="#FFCCCC", font=("Arial", 15))
label_answer_1.grid(column=0, row=11)


frame_widjets.pack()


window.mainloop()

