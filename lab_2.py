import tkinter as tk
from math import*

from PIL import ImageTk, Image


window = tk.Tk()
window.title("Лабораторная работа №2 | Шуляк А.А.")
window.geometry("600x500")
window.resizable(width=False, height=False)
window["bg"] = "#FFCCCC"


def fun_clear_text():
    label_answer_x.config(text="")

def fun_decision():
    fun_clear_text()
    try:
        x = float(entry_x.get())
        if x < -3:
            y = 1
            label_answer_x["text"] = str(y)
        elif -3 <= x <= -1:
            y = -sqrt(pow(-2, 2) - pow(x+1, 2))
            label_answer_x["text"] = str(round(y, 3))
        elif -1 < x <= 2:
            y = -2
            label_answer_x["text"] = str(y)
        elif x > 2:
            y = x - 4
            label_answer_x["text"] = str(y)

    except:
        label_answer_x["text"] = "Ввод некоректен"

#Создание фрейма в основном окне
frame_widjets = tk.Frame(window)
frame_widjets["bg"] = "#FFCCCC"


label_one = tk.Label(frame_widjets, text="Вычисление значений функции y=f(x), которая задана графиком:", bg="#FFCCCC", font=("Arial", 10))
label_one.grid(column=1, row=0)

#Вывод изображения графика (т.к. tkinter не умеет в изобржения, нам нужна библиотека Pillow
#Читаем изображение из папки
image_one = Image.open("image/lab2/LAB_2.png")
#изменяем размер изображения
pil_image = image_one.resize((400, 200))
#Размещаем изображение в виджете Label
frame_widjets.image_one = ImageTk.PhotoImage(pil_image)
image_Label_one = tk.Label(frame_widjets, image=frame_widjets.image_one, bg="#FFCCCC")
image_Label_one.grid(column=1, row=1)


label_x = tk.Label(frame_widjets, text="Введите X:", bg="#FFCCCC", font=("Arial", 15))
label_x.grid(column=1, row=2)

entry_x = tk.Entry(frame_widjets, font=("Arial", 10))
entry_x.grid(column=1, row=3, pady=30)

btn_launch = tk.Button(frame_widjets, text="Запуск", command=fun_decision, bg="#FF3399", font=("Arial", 20))
btn_launch.grid(column=1, row=4)

label_answer_x = tk.Label(frame_widjets, bg="#FFCCCC", font=("Arial", 15))
label_answer_x.grid(column=1, row=5)

frame_widjets.pack()


window.mainloop()

