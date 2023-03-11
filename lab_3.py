import tkinter as tk
from math import*

from PIL import ImageTk, Image


window = tk.Tk()
window.title("Лабораторная работа №3 | Шуляк А.А.")
window.geometry("600x500")
window.resizable(width=False, height=False)
window["bg"] = "#FFCCCC"


def fun_clear_text():
    label_answer_1.config(text="")
    label_answer_2.config(text="")

def fun_decision():
    fun_clear_text()
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        r = float(entry_r.get())

        if (pow((-r)-x, 2) + y * y <= r * r and x <= 0 and y >= 0) \
                or ((pow(r-x, 2) + y*y) <= r*r and x >= 0 and y <= 0):
            label_answer_1["text"] = "Входит"
            label_answer_2["text"] = "Входит"
        else:
            label_answer_1["text"] = "Не входит"
            label_answer_2["text"] = "Не входит"

    except:
        label_answer_1["text"] = "Ввод некоректен"
        label_answer_2["text"] = "Ввод некоректен"


frame_widjets = tk.Frame(window)
frame_widjets["bg"] = "#FFCCCC"

label_one = tk.Label(frame_widjets, text="Принадлежит ли точка заданной области:", bg="#FFCCCC", font=("Arial", 10))
label_one.grid(column=1, row=0)

image_one = Image.open("image/lab3/LAB_3.png")
pil_image = image_one.resize((250, 200))
frame_widjets.image_one = ImageTk.PhotoImage(pil_image)
image_Label_one = tk.Label(frame_widjets, image=frame_widjets.image_one, bg="#FFCCCC")
image_Label_one.grid(column=1, row=1)



label_x = tk.Label(frame_widjets, text="Введите X:", bg="#FFCCCC", font=("Arial", 15))
label_x.grid(column=0, row=2)

entry_x = tk.Entry(frame_widjets, font=("Arial", 10))
entry_x.grid(column=0, row=3, pady=30)

label_y = tk.Label(frame_widjets, text="Введите Y:", bg="#FFCCCC", font=("Arial", 15))
label_y.grid(column=2, row=2)

entry_y = tk.Entry(frame_widjets, font=("Arial", 10))
entry_y.grid(column=2, row=3, pady=30)

label_r = tk.Label(frame_widjets, text="Введите R:", bg="#FFCCCC", font=("Arial", 15))
label_r.grid(column=1, row=2)

entry_r = tk.Entry(frame_widjets, font=("Arial", 10))
entry_r.grid(column=1, row=3, pady=30)

btn_launch = tk.Button(frame_widjets, text="Запуск", command=fun_decision, bg="#FF3399", font=("Arial", 20))
btn_launch.grid(column=1, row=4)

label_answer_1 = tk.Label(frame_widjets, bg="#FFCCCC", font=("Arial", 15))
label_answer_1.grid(column=0, row=5)

label_answer_2 = tk.Label(frame_widjets, bg="#FFCCCC", font=("Arial", 15))
label_answer_2.grid(column=2, row=5)

frame_widjets.pack()


window.mainloop()

