import tkinter as tk
from math import*
import random
from PIL import ImageTk, Image


window = tk.Tk()
window.title("Лабораторная работа №5 | Шуляк А.А.")
window.geometry("600x500")
window.resizable(width=False, height=False)
window["bg"] = "#FFCCCC"


def fun_clear_text():
    label_answer_1.config(text="")
    label_answer_2.config(text="")

def fun_decision():
    fun_clear_text()
    try:
        amount = int(entry_amount.get())
        r = int(entry_r.get())
        t = 0
        f = 0
        for i in range(amount):
            x = random.randrange(-r, r)
            y = random.randrange(-r, r)
            if (pow((-r)-x, 2) + y * y <= r * r and x <= 0 and y >= 0) \
                    or ((pow(r-x, 2) + y*y) <= r*r and x >= 0 and y <= 0):
                print("Попал", x, y)
                t += 1
            else:
                f += 1
                print("Промазал", x, y)

        label_answer_1["text"] = "Вы попали {} раз".format(t)
        label_answer_2["text"] = "Вы промазали {} раз".format(f)
    except:
        label_answer_1["text"] = "Некорректный ввод"
        label_answer_2["text"] = "Некорректный ввод"


frame_widjets = tk.Frame(window)
frame_widjets["bg"] = "#FFCCCC"

label_one = tk.Label(frame_widjets, text="Выстрелы по мишени", bg="#FFCCCC", font=("Arial", 10))
label_one.grid(column=0, row=0)

image_one = Image.open("image/lab3/LAB_3.png")
pil_image = image_one.resize((220, 200))
frame_widjets.image_one = ImageTk.PhotoImage(pil_image)
image_Label_one = tk.Label(frame_widjets, image=frame_widjets.image_one, bg="#FFCCCC")
image_Label_one.grid(column=0, row=1)



label_amount = tk.Label(frame_widjets, text="Введите количество выстрелов:", bg="#FFCCCC", font=("Arial", 15))
label_amount.grid(column=0, row=2)

entry_amount = tk.Entry(frame_widjets, font=("Arial", 10))
entry_amount.grid(column=0, row=3, pady=10)

label_r = tk.Label(frame_widjets, text="Введите R:", bg="#FFCCCC", font=("Arial", 15))
label_r.grid(column=0, row=4)

entry_r = tk.Entry(frame_widjets, font=("Arial", 10))
entry_r.grid(column=0, row=5, pady=10)

btn_launch = tk.Button(frame_widjets, text="Запуск", command=fun_decision, bg="#FF3399", font=("Arial", 20))
btn_launch.grid(column=0, row=6)

label_answer_1 = tk.Label(frame_widjets, bg="#FFCCCC", font=("Arial", 15))
label_answer_1.grid(column=0, row=7)

label_answer_2 = tk.Label(frame_widjets, bg="#FFCCCC", font=("Arial", 15))
label_answer_2.grid(column=0, row=8)

frame_widjets.pack()


window.mainloop()

