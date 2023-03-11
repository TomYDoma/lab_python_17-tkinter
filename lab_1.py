import tkinter as tk
from math import*

from PIL import ImageTk, Image


window = tk.Tk()
window.title("Лабораторная работа №1 | Шуляк А.А.")
window.geometry("600x500")
window.resizable(width=False, height=False)
window["bg"] = "#FFCCCC"


def clear_text():
    label_answer_z1.config(text="")
    label_answer_z2.config(text="")

def fun_decision():
    clear_text()
    try:
        m = float(entry_m.get())

        z1 = (sqrt(pow(3 * m + 2, 2) - 24 * m)) / (3 * sqrt(m) - 2/sqrt(m))
        z2 = - sqrt(m)
        label_answer_z1["text"] = "z1 = " + str(round(z1, 3))
        label_answer_z2["text"] = "z2 = " + str(round(z2, 3))


    except:
        label_answer_z1["text"] = "Ввод некоректен"


frame_widjets = tk.Frame(window)
frame_widjets["bg"] = "#FFCCCC"

label_one = tk.Label(frame_widjets, text="Вычисление значений z1 и z2 по формулам:", bg="#FFCCCC", font=("Arial", 10))
label_one.grid(column=1, row=0)

image_one = Image.open("image/lab1/LAB_1_z1.png")
pil_image = image_one.resize((200, 100))
frame_widjets.image_one = ImageTk.PhotoImage(pil_image)
image_Label_one = tk.Label(frame_widjets, image=frame_widjets.image_one, bg="#FFCCCC")
image_Label_one.grid(column=0, row=1)

image_two = Image.open("image/lab1/LAB_1_z2.png")
pil_image = image_two.resize((100, 40))
frame_widjets.image_two = ImageTk.PhotoImage(pil_image)
image_Label_two = tk.Label(frame_widjets, image=frame_widjets.image_two, bg="#FFCCCC")
image_Label_two.grid(column=2, row=1)


label_m = tk.Label(frame_widjets, text="Введите m:", bg="#FFCCCC", font=("Arial", 15))
label_m.grid(column=1, row=2)

entry_m = tk.Entry(frame_widjets, font=("Arial", 10))
entry_m.grid(column=1, row=3, pady=30)

btn_launch = tk.Button(frame_widjets, text="Запуск", command=fun_decision, bg="#FF3399", font=("Arial", 20))
btn_launch.grid(column=1, row=4)

label_answer_z1 = tk.Label(frame_widjets, bg="#FFCCCC", font=("Arial", 15))
label_answer_z1.grid(column=0, row=5)

label_answer_z2 = tk.Label(frame_widjets, bg="#FFCCCC", font=("Arial", 15))
label_answer_z2.grid(column=2, row=5)

frame_widjets.pack()


window.mainloop()

