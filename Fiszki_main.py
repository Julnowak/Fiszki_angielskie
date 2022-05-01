from tkinter import *
import random

root = Tk()
root.title('Fiszki angielsko-polskie')

# Tworzy okno
root.geometry('550x550')
list_of_words = []

### TRZEBA pomyśleć nad ścieżką!
# Pobiera słówka z A1
with open('C:/Users/Julia/Documents/GitHub/Fiszki_angielskie/Baza/A1_words.txt', 'r', encoding='UTF-8') as lines:
    for line in lines:
        list_of_words.append(line.rstrip())

list_of_words.pop(0)
print(list_of_words)
root.mainloop()
