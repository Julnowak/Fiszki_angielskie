from tkinter import *
from PIL import Image, ImageTk
import random
import os
from pygame import mixer

# Tutaj robi dźwięki :P
import winsound
# winsound.Beep(1200, 200)

def beep():
    mixer.init()
    s = mixer.Sound("Klik.wav")
    s.play()

root = Tk()
root.title('Fiszki angielsko-polskie')


mixer.init()
sound=mixer.Sound("muzyka.wav")
sound.set_volume(0.4)
sound.play(-1)

# Tworzy okno

w = 800 # width for the Tk root
h = 650 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# label = Label(root, text='To jest tytuł fiszek', font=('Comic_Sans', 25))
# label.pack()

list_of_words = []


## Pobieranie słówek
# Pobiera słówka z A1

with open('Baza/A1_words.txt', 'r', encoding='UTF-8') as lines:
    for line in lines:
        list_of_words.append(line.rstrip())


def start_game():
    print("Wow!")
    # Wybór trybu

#
# list_of_words.pop(0)
# print(list_of_words)


def MENU():
    def destroyer():
        label.destroy()
        przycisk_start.destroy()
        przycisk_opcji.destroy()
        przycisk_exit.destroy()
        przycisk_dodaj.destroy()
        przycisk_postepy.destroy()


    def DODAJ():
        destroyer()
        label2 = Label(root, text='Druga strona', font=('Comic_Sans', 25))
        label2.pack()

        def back():
            label2.destroy()
            przycisk_next2.destroy()
            wejscie.destroy()
            MENU()

        wejscie = Entry(root,width=40)
        wejscie.pack()
        przycisk_next2 = Button(root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), back()])
        przycisk_next2.pack(side=BOTTOM)

    def POSTEPY():
        destroyer()
        label2 = Label(root, text='Druga strona', font=('Comic_Sans', 25))
        label2.pack()

        def back():
            label2.destroy()
            przycisk_next2.destroy()
            MENU()

        przycisk_next2 = Button(root, text='Poprzednia strona', font=('Comic_Sans', 25), command=lambda: [beep(), back()])
        przycisk_next2.pack(side=BOTTOM)

    def WYBOR():
        destroyer()
        label2 = Label(root, text='Druga strona', font=('Comic_Sans', 25))
        label2.pack()

        def back():
            label2.destroy()
            przycisk_next2.destroy()
            przycisk_learn.destroy()
            przycisk_challenge.destroy()
            MENU()

        przycisk_next2 = Button(root, text='Poprzednia strona', font=('Comic_Sans', 25), command=lambda: [beep(), back()])
        przycisk_next2.pack(side=BOTTOM)

        przycisk_learn = Button(root, text='Tryb nauki', font=('Comic_Sans', 25), command=lambda: [beep()])
        przycisk_learn.pack()

        przycisk_challenge = Button(root, text='Tryb wyzwania', font=('Comic_Sans', 25), command=lambda: [beep()])
        przycisk_challenge.pack()

    def OPCJE():
        destroyer()
        label2 = Label(root, text='Strona opcji', font=('Comic_Sans', 25))
        label2.pack()

        def back():
            label2.destroy()
            przycisk_next2.destroy()
            MENU()

        przycisk_next2 = Button(root, text='Poprzednia strona', font=('Comic_Sans', 25), command=lambda: [beep(), back()])
        przycisk_next2.pack(side=BOTTOM)

    def EXIT():
        destroyer()
        label2 = Label(root, text='Czy na pewno chcesz opuścić grę?', font=('Comic_Sans', 25))
        label2.pack()

        def back():
            label2.destroy()
            przycisk_back.destroy()
            przycisk_quit.destroy()
            MENU()

        przycisk_back = Button(root, text='Nie', font=('Comic_Sans', 25), command=lambda: [beep(), back()])
        przycisk_back.pack()

        przycisk_quit = Button(root, text='Tak', font=('Comic_Sans', 25), command=lambda: [beep(), quit()])
        przycisk_quit.pack()

    label = Label(root, text='Pierwsza', font=('Comic_Sans', 25))
    label.pack()

    # Przyciski
    przycisk_start = Button(root, text='Graj', width=8, command=lambda: [beep(), WYBOR()])
    przycisk_start.pack()

    przycisk_dodaj = Button(root, text='Dodaj fiszkę', command=lambda: [beep(), DODAJ()])
    przycisk_dodaj.pack()

    przycisk_postepy = Button(root, text='Postępy', command=lambda: [beep(), POSTEPY()])
    przycisk_postepy.pack()

    przycisk_opcji = Button(root, text='Opcje', command=lambda: [beep(), OPCJE()])
    przycisk_opcji.pack()

    przycisk_exit = Button(root, text='Wyjście', command=lambda: [beep(), EXIT()])
    przycisk_exit.pack()

MENU()
root.mainloop()
