import tkinter as tk
from math import*

from PIL import ImageTk, Image


window = tk.Tk()
window.title("Лабораторная работа №6 | Шуляк А.А.")
window.geometry("600x500")
window.resizable(width=False, height=False)
window["bg"] = "#FFCCCC"


def fun_clear_text():
    label_answer.config(text="")

def fun_decision():
    fun_clear_text()
    try:
        x = float(entry_x.get())
        e = float(entry_e.get())
        m = 0
        for n in range(0, 25):
            t = pow(x-1, n+1) / ((n+1) * pow(x, n+1))
            if fabs(t) < e:
                break
            else:
                m += t
        label_answer["text"] = "Сумма ряда равна: " + str(m)

    except:
        label_answer["text"] = "Ввод некоректен"

#Создание фрейма в основном окне
frame_widjets = tk.Frame(window)
frame_widjets["bg"] = "#FFCCCC"


label_one = tk.Label(frame_widjets, text="Вычисление суммы ряда Тейлора по формуле:", bg="#FFCCCC", font=("Arial", 10))
label_one.grid(column=1, row=0)

#Вывод изображения графика (т.к. tkinter не умеет в изобржения, нам нужна библиотека Pillow
#Читаем изображение из папки
image_one = Image.open("image/lab6/LAB_6.png")
#изменяем размер изображения
pil_image = image_one.resize((400, 60))
#Размещаем изображение в виджете Label
frame_widjets.image_one = ImageTk.PhotoImage(pil_image)
image_Label_one = tk.Label(frame_widjets, image=frame_widjets.image_one, bg="#FFCCCC")
image_Label_one.grid(column=1, row=1)


label_x = tk.Label(frame_widjets, text="Введите X:", bg="#FFCCCC", font=("Arial", 15))
label_x.grid(column=1, row=2)

entry_x = tk.Entry(frame_widjets, font=("Arial", 10))
entry_x.grid(column=1, row=3, pady=30)

label_e = tk.Label(frame_widjets, text="Введите ε:", bg="#FFCCCC", font=("Arial", 15))
label_e.grid(column=1, row=4)

entry_e = tk.Entry(frame_widjets, font=("Arial", 10))
entry_e.grid(column=1, row=5, pady=30)

btn_launch = tk.Button(frame_widjets, text="Запуск", command=fun_decision, bg="#FF3399", font=("Arial", 20))
btn_launch.grid(column=1, row=6)

label_answer = tk.Label(frame_widjets, bg="#FFCCCC", font=("Arial", 15))
label_answer.grid(column=1, row=7)

frame_widjets.pack()


window.mainloop()

