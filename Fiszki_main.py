from tkinter import *
import random

okno = Tk()
okno.title('Fiszki angielsko-polskie')

# Tworzy okno
okno.geometry('550x550')
list_of_words = []

### TRZEBA pomyśleć nad ścieżką!
# Pobiera słówka z A1
with open('C:/Users/Julia/Documents/GitHub/Fiszki_angielskie/Baza/A1_words.txt', 'r', encoding='UTF-8') as lines:
    for line in lines:
        list_of_words.append(line.rstrip())


def click_action():
    print("Wow!")

list_of_words.pop(0)
print(list_of_words)

# Przyciski
przycisk_start = Button(okno, text='Graj', width=8, command=click_action, image="Pla")
przycisk_start.pack()

przycisk_opcji = Button(okno, text='Opcje', width=8, command=click_action)
przycisk_opcji.pack()

okno.mainloop()
