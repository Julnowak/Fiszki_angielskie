from tkinter import *
from PIL import Image, ImageTk
import random
import os

simp_path = 'A1_words.txt'
abs_path = os.path.abspath(simp_path)

print(abs_path)

root = Tk()
root.title('Fiszki angielsko-polskie')

# Tworzy okno
root.geometry('550x550')
list_of_words = []

root.configure(bg="#ffffff")

canvas = Canvas(root, bg="#ffffff", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")

canvas.place(x=0, y=0)


## Pobieranie słówek
# Pobiera słówka z A1

with open(r'Baza\A1_words.txt', 'r', encoding='UTF-8') as lines:
    for line in lines:
        list_of_words.append(line.rstrip())


def click_action():
    print("Wow!")


list_of_words.pop(0)
print(list_of_words)


# Przyciski
przycisk_start = Button(root, text='Graj', width=8, command=click_action)
przycisk_start.pack()

# przycisk_opcji = Button(okno, text='Opcje', width=8, command=click_action)
# przycisk_opcji.pack()

root.mainloop()
