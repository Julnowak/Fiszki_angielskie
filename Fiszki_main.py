from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import random
import numpy as np

import os
import time
from math import ceil
from pygame import mixer


def destroyer(lista):
    for elem in lista:
        elem.destroy()
    return lista


class Page:
    def __init__(self):
        self.lista = []


class MENU(Page):
    def __init__(self, root, lista, sound):
        super().__init__()
        self.root = root
        self.inter = lista
        self.create()
        self.sound = sound

    def START(self):
        START_PAGE(self.root, self.inter, self.sound)

    def DODAJ(self):
        DODAJ_PAGE(self.root, self.inter, self.sound)

    def BAZA(self):
        BAZA_PAGE(self.root, self.inter, self.sound)

    def POSTEPY(self):
        POSTEPY_PAGE(self.root, self.inter, self.sound)

    def OPCJE(self):
        OPCJE_PAGE(self.root, self.inter, self.sound)

    def EXIT(self):
        EXIT_PAGE(self.root, self.inter, self.sound)

    def configure(self):
        # Kolumny
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)

        # Rzędy
        self.root.rowconfigure(0, weight=10)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=2)

    def create(self):
        self.configure()
        interface = []

        label = Label(self.root, text='BEAVER DAM', font=('Comic_Sans', 25))
        interface.append(label)

        # Przyciski

        przycisk_start = Button(self.root, text='Graj', height=3, width=20, font=('Comic_Sans', 14),
                                command=lambda: [beep(), self.START()])
        interface.append(przycisk_start)

        label.grid(columnspan=5, row=0)
        przycisk_start.grid(columnspan=5, rows=1)

        przycisk_dodaj = Button(self.root, text='Dodaj fiszkę', height=3, width=20, font=('Comic_Sans', 14),
                                command=lambda: [beep(), self.DODAJ()])
        interface.append(przycisk_dodaj)

        przycisk_usun = Button(self.root, text='Baza fiszek', height=3, width=20, font=('Comic_Sans', 14),
                               command=lambda: [beep(), self.BAZA()])
        interface.append(przycisk_usun)

        przycisk_postepy = Button(self.root, text='Postępy', height=3, width=20, font=('Comic_Sans', 14),
                                  command=lambda: [beep(), self.POSTEPY()])
        interface.append(przycisk_postepy)

        przycisk_opcji = Button(self.root, text='Opcje', height=3, width=20, font=('Comic_Sans', 14),
                                command=lambda: [beep(), self.OPCJE()])
        interface.append(przycisk_opcji)

        przycisk_exit = Button(self.root, text='Wyjście', height=3, width=20, font=('Comic_Sans', 14),
                               command=lambda: [beep(), self.EXIT()])
        interface.append(przycisk_exit)

        przycisk_dodaj.grid(columnspan=5, row=2)
        przycisk_usun.grid(columnspan=5, row=3)
        przycisk_postepy.grid(columnspan=5, row=4)
        przycisk_opcji.grid(columnspan=5, row=5)
        przycisk_exit.grid(columnspan=5, row=6)

        self.inter = interface


class App(Page):
    def __init__(self):
        super().__init__()

        # Tworzy okno
        self.root = Tk()
        self.root.title('Fiszki angielsko-polskie')
        img = PhotoImage(file="tło2.png")
        self.root.config(bg='black')
        label = Label(
            self.root,
            image=img
        )
        label.place(x=0, y=0)

        self.width = 1000  # width for the Tk root
        self.height = 800  # height for the Tk root

        # get screen width and height
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen

        x = (ws / 2) - (self.width / 2)
        y = (hs / 2) - (self.height / 2)

        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))

        self.track_pages = dict()

        mixer.init()
        s = random.choice(os.listdir("Sounds"))
        self.sound = mixer.Sound("Sounds/" + s)
        self.sound.set_volume(0.1)
        self.sound.play(-1)

        self.inter = []
        MENU(self.root, self.inter, self.sound)
        self.root.mainloop()


def show_message_isHere(a, p):
    if a and p:
        return messagebox.askyesno('Wykryto identyczne słówko!', 'Czy aby na pewno chcesz dodać fiszkę?')
    elif a:
        return messagebox.askyesno('Wykryto powtórzenie w słówku angielskim!',
                                   'Czy aby na pewno chcesz dodać fiszkę?')
    elif p:
        return messagebox.askyesno('Wykryto powtórzenie w słówku polskim!',
                                   'Czy aby na pewno chcesz dodać fiszkę?')


def clear_text(entries):
    for entry in entries:
        entry.delete(0, 'end')


class DODAJ_PAGE(Page):
    baza = {'A1': 'Baza/A1_words.txt',
            'A2': 'Baza/A2_words.txt',
            'B1': 'Baza/B1_words.txt',
            'B2': 'Baza/B2_words.txt',
            'C1': 'Baza/C1_words.txt',
            'C2': 'Baza/C2_words.txt'}

    def __init__(self, root, lista, sound):
        super().__init__()
        self.inter = []
        self.root = root
        self.sound = sound
        destroyer(lista)
        self.create()

    def configure(self):
        # Kolumny
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)

        # Rzędy
        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=2)

    def create(self):
        self.configure()
        interface = []

        label2 = Label(self.root, text='Dodaj fiszkę', font=('Comic_Sans', 25))
        interface.append(label2)

        # Przyciski
        lvl = Label(self.root, text='Poziom/Level', font=('Comic_Sans', 16))
        interface.append(lvl)

        wejscielvl = Combobox(self.root)
        wejscielvl['values'] = ('A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'Inne')
        wejscielvl.current(0)
        interface.append(wejscielvl)

        labelANG = Label(self.root, text='Angielski/English', font=('Comic_Sans', 16))
        interface.append(labelANG)

        wejscieANG = Entry(self.root, width=40)
        interface.append(wejscieANG)

        labelPOL = Label(self.root, text='Polski/Polish', font=('Comic_Sans', 16))
        interface.append(labelPOL)

        wejsciePOL = Entry(self.root, width=40)
        interface.append(wejsciePOL)

        labelKAT = Label(self.root, text='Kategoria/Category', font=('Comic_Sans', 16))
        interface.append(labelKAT)

        wejscieKAT = Entry(self.root, width=40)
        interface.append(wejscieKAT)

        przycisk_submit = Button(self.root, text='Dodaj', height=3, width=20, font=('Comic_Sans', 14),
                                 command=lambda: [beep(), self.submit
                                 (interface[2], interface[4], interface[6], interface[8]),
                                                  clear_text([interface[2], interface[4],
                                                                   interface[6], interface[8]])])
        interface.append(przycisk_submit)

        przycisk_back = Button(self.root, text='Poprzednia strona', height=3, width=20, font=('Comic_Sans', 14),
                               command=lambda: [beep(), self.back(self.inter)])
        interface.append(przycisk_back)

        l = Label(self.root, height=3, width=50, bg="black", fg="#000")
        interface.append(l)

        self.inter = interface

        l.grid(columnspan=5, row=6)
        label2.grid(columnspan=5, row=0)
        lvl.grid(columnspan=5, row=1)
        wejscielvl.grid(columnspan=5, row=2)
        labelANG.grid(column=0, row=3)
        wejscieANG.grid(column=0, row=4)
        labelPOL.grid(columnspan=5, row=3)
        wejsciePOL.grid(columnspan=5, row=4)
        labelKAT.grid(column=4, row=3)
        wejscieKAT.grid(column=4, row=4)
        przycisk_submit.grid(columnspan=5, row=5)
        przycisk_back.grid(columnspan=5, row=7)

    def back(self, lista):
        destroyer(lista)
        MENU(self.root, lista, self.sound)

    def show_message_good(self):
        label = Label(self.root, text="Fiszka została dodana", height=3, width=50,
                      background="lime",
                      foreground="black")
        label.grid(columnspan=5, row=6)
        label.after(2000, label.destroy)

    def show_message_negative(self):
        label = Label(self.root, text="Nie uzupełniono jednej z rubryk! Spróbuj jeszcze raz", height=3, width=50,
                      background="red",
                      foreground="black")
        label.grid(columnspan=5, row=6)
        label.after(2000, label.destroy)

    def show_message_info(self):
        label = Label(self.root, text="Fiszka nie została dodana",
                      background="cyan",
                      foreground="black", height=3, width=50)
        label.grid(columnspan=5, row=6)
        label.after(2000, label.destroy)

    def submit(self, lvl, ANG, POL, KAT):
        lvl = lvl.get()
        ang = ANG.get()
        pol = POL.get()
        kat = KAT.get()

        lvl = lvl.strip()

        if ang != '' and pol != '' and kat != '':
            if lvl in self.baza.keys():
                ans = True
                with open(self.baza[lvl], 'r+', encoding='UTF-8') as f:
                    next(f)
                    for line in f:
                        lista = line.split(' - ')

                        if ang == lista[0]:
                            a = True
                        else:
                            a = False
                        if pol == lista[1]:

                            p = True
                        else:
                            p = False

                        if a or p:
                            ans = show_message_isHere(a, p)
                            break
                        else:
                            ans = True
                            break
                if ans:
                    with open(self.baza[lvl], 'a+', encoding='UTF-8') as f:
                        f.write(f"{ang} - {pol} - {kat}\n")
                    self.show_message_good()
                else:
                    self.show_message_info()
            else:
                ans = True
                with open('Baza/Others.txt', 'r', encoding='UTF-8') as f:
                    for line in f:
                        lista = line.split(' - ')

                        if ang in lista[0]:
                            a = True
                        else:
                            a = False

                        if pol in lista[1]:
                            p = True
                        else:
                            p = False

                        if a or p:
                            ans = show_message_isHere(a, p)
                            break
                if ans:
                    with open('Baza/Others.txt', 'a+', encoding='UTF-8') as f:
                        f.write(f"{ang} - {pol} - {kat}\n")
                    self.show_message_good()
                else:
                    self.show_message_info()
            f.close()
        else:
            self.show_message_negative()


class OPCJE_PAGE(Page):
    def __init__(self, root, lista, sound):
        super().__init__()
        self.inter = []
        self.root = root
        self.sound = sound
        destroyer(lista)
        self.create()

    def back(self, lista):
        destroyer(lista)
        MENU(self.root, lista, self.sound)

    def change_volume(self, s):
        a = s.get()
        self.sound.set_volume(a / 100)

    def change_music(self, w):
        w = w.get()
        a = self.sound.get_volume()
        self.sound.stop()
        print(w)
        if w == 'LOSOWA':
            t = random.choice(os.listdir("Sounds"))
            self.sound = mixer.Sound("Sounds/" + t)
        else:
            self.sound = mixer.Sound("Sounds/" + w + '.wav')
        self.sound.set_volume(a)
        self.sound.play(-1)

    def change_time(self):
        pass

    def configure(self):
        # Kolumny
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)

        # Rzędy
        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=2)

    def create(self):
        self.configure()
        interface = []
        label2 = Label(self.root, text='OPCJE', font=('Comic_Sans', 25))
        interface.append(label2)
        label2.grid(columnspan=5)
        slider = Scale(self.root, from_=0, to=100, orient=HORIZONTAL)
        interface.append(slider)
        slider.grid(columnspan=5)
        slider.set(ceil(self.sound.get_volume() * 100))

        przycisk_next5 = Button(self.root, text='Ustaw', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.change_volume(slider)])
        interface.append(przycisk_next5)
        przycisk_next5.grid(columnspan=5)

        wejscie = Combobox(self.root)
        wejscie['values'] = [i.removesuffix('.wav') for i in os.listdir("Sounds")] + ['LOSOWA']
        wejscie.current(0)
        interface.append(wejscie)
        wejscie.grid(columnspan=5)

        przycisk_next4 = Button(self.root, text='Zmiana', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.change_music(wejscie)])
        interface.append(przycisk_next4)
        przycisk_next4.grid(columnspan=5)

        przycisk_next2 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_next2)
        przycisk_next2.grid(columnspan=5)

        self.inter = interface


def show_message_isHere(a, p):
    if a and p:
        return messagebox.askyesno('Wykryto identyczne słówko!', 'Czy aby na pewno chcesz dodać fiszkę?')
    elif a:
        return messagebox.askyesno('Wykryto powtórzenie w słówku angielskim!',
                                   'Czy aby na pewno chcesz dodać fiszkę?')
    elif p:
        return messagebox.askyesno('Wykryto powtórzenie w słówku polskim!',
                                   'Czy aby na pewno chcesz dodać fiszkę?')


class BAZA_PAGE(Page):
    def __init__(self, root, lista, sound):
        super().__init__()
        self.inter = []
        self.root = root
        self.sound = sound
        self.list_of_words = []
        destroyer(lista)
        self.create()

    def back(self, lista):
        destroyer(lista)
        MENU(self.root, lista, self.sound)

    def configure(self):
        # Kolumny
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)

        # Rzędy
        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=2)

    def are_you_sure(self, l, lista):
        h = l.get()
        new = h.split(' - ')
        try:
            ans = messagebox.askyesno('Usuwanie fiszki',
                                      f'Czy na pewno chcesz usunąć fiszkę "{new[0]} - {new[1]}" z kategorii "{new[2].rstrip()}" ?')
            if ans:
                for plik in lista:
                    with open(plik, 'r+', encoding='UTF-8') as f:
                        d = f.readlines()
                        f.seek(0)
                        for i in d:
                            if i != h:
                                f.write(i)
                        f.truncate()
                        f.close()
                self.show_message_positive()
            else:
                self.show_message_info()

        except:
            self.show_message_warning()

    def add(self, e, e1, e2, h, lista, roo):
        e = e.get()
        e1 = e1.get()
        e2 = e2.get()
        for plik in lista:
            with open(plik, 'r+', encoding='UTF-8') as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != h:
                        f.write(i)
                    else:
                        f.write(f'{e} - {e1} - {e2}\n')

                f.truncate()
                f.close()
        self.show_message_positive_edit(roo)

    def edit(self, l, lista):
        win = Tk()

        def create_window():
            new_window = Toplevel(win)

        ws = win.winfo_screenwidth()  # width of the screen
        hs = win.winfo_screenheight()  # height of the screen

        x = (ws / 2) - (400 / 2)
        y = (hs / 2) - (500 / 2)

        win.geometry('%dx%d+%d+%d' % (400, 500, x, y))

        h = l.get()
        new = h.split(' - ')

        lab = Label(win, text=f'Edytujesz swoją fiszkę "{new[0]} - {new[1]}" z kategorii "{new[2].rstrip()}"')
        lab.pack()

        lab1 = Label(win, text=f'Nowa nazwa angielska')
        lab1.pack()

        entryText = StringVar()
        entryText.set("Hello World")
        entry = Entry(win, textvariable=entryText)
        entry.pack()

        lab2 = Label(win, text=f'Nowa nazwa polska')
        lab2.pack()

        entryText2 = StringVar()
        entryText2.set("Hello World")
        entry2 = Entry(win, textvariable=entryText2)
        entry2.pack()

        lab3 = Label(win, text=f'Nowa kategoria')
        lab3.pack()

        entryText3 = StringVar()
        entryText3.set("Hello World")
        entry3 = Entry(win, textvariable=entryText3)
        entry3.pack()
        try:
            przycisk = Button(win, text='Aktualizuj',
                              command=lambda: [beep(), self.add(entry, entry2, entry3, h, lista, win),
                                               BAZA_PAGE(self.root, self.inter, self.sound)])
            przycisk.pack()
        except:
            pass

        l = Label(win, height=3, width=50, bg="black", fg="#000")
        l.pack()

        win.mainloop()

    def show_message_positive(self):
        label = Label(self.root, text="Poprawnie usunięto fiszkę",
                      background="lime",
                      foreground="black", height=3, width=50)
        label.grid(column=1, row=6)
        label.after(2000, label.destroy)

    def show_message_positive_edit(self, roo):
        label = Label(roo, text="Poprawnie edytowano fiszkę",
                      background="lime",
                      foreground="black", height=3, width=50)
        label.pack()
        label.after(2000, label.destroy)

    def show_message_info(self):
        label = Label(self.root, text="Nie usunięto fiszki",
                      background="cyan",
                      foreground="black", height=3, width=50)
        label.grid(column=1, row=6)
        label.after(2000, label.destroy)

    def show_message_info_edit(self):
        label = Label(self.root, text="Nie zmieniono fiszki",
                      background="cyan",
                      foreground="black", height=3, width=50)
        label.grid(column=1, row=6)
        label.after(2000, label.destroy)

    def show_message_warning(self):
        label = Label(self.root, text="Wybrana fiszka nie istnieje",
                      background="red",
                      foreground="black", height=3, width=50)
        label.grid(column=1, row=6)
        label.after(2000, label.destroy)

    def checked(self, a1, a2, b1, b2, c1, c2, o):
        lista = []

        a1 = a1.get()
        a2 = a2.get()
        b1 = b1.get()
        b2 = b2.get()
        c1 = c1.get()
        c2 = c2.get()
        o = o.get()

        if a1 == 1:
            lista.append('Baza/A1_words.txt')
        if a2 == 1:
            lista.append('Baza/A2_words.txt')
        if b1 == 1:
            lista.append('Baza/B1_words.txt')
        if b2 == 1:
            lista.append('Baza/B2_words.txt')
        if c1 == 1:
            lista.append('Baza/C1_words.txt')
        if c2 == 1:
            lista.append('Baza/C2_words.txt')
        if o == 1:
            lista.append('Baza/Others.txt')

        for plik in lista:
            with open(plik, 'r+', encoding='UTF-8') as f:
                try:
                    next(f)
                    for line in f:
                        self.list_of_words.append(line)
                    f.close()
                except:
                    f.close()

        l = Combobox(self.root, width=50)
        l['values'] = self.list_of_words
        try:
            l.current(0)
        except:
            l.current(None)

        l.grid(columnspan=5, row=4)
        self.inter.append(l)

        przycisk_remove = Button(self.root, text='Usuń', command=lambda: [beep(), self.are_you_sure(l, lista),
                                                                          BAZA_PAGE(self.root, self.inter, self.sound)])
        przycisk_remove.grid(row=5, column=0)
        self.inter.append(przycisk_remove)

        przycisk_edit = Button(self.root, text='Edytuj', command=lambda: [beep(), self.edit(l, lista)])
        przycisk_edit.grid(row=5, column=4)
        self.inter.append(przycisk_edit)

    def create(self):
        self.configure()
        interface = []

        label = Label(self.root, text='Baza danych', font=('Comic_Sans', 25))
        interface.append(label)
        label.grid(row=0, columnspan=5)

        label2 = Label(self.root, text='Wybierz zakres', font=('Comic_Sans', 25))
        label2.grid(row=1, columnspan=5)
        interface.append(label2)

        frame = Frame(self.root)
        frame.grid(row=2, columnspan=5)
        interface.append(frame)

        varA1 = IntVar()
        check1 = Checkbutton(frame, text="A1", variable=varA1)
        check1.grid(row=1, column=1, sticky=W)
        interface.append(check1)

        varA2 = IntVar()
        check2 = Checkbutton(frame, text="A2", variable=varA2)
        check2.grid(row=2, column=1, sticky=W)
        interface.append(check2)

        varB1 = IntVar()
        check3 = Checkbutton(frame, text="B1", variable=varB1)
        check3.grid(row=1, column=2, sticky=W)
        interface.append(check3)

        varB2 = IntVar()
        check4 = Checkbutton(frame, text="B2", variable=varB2)
        check4.grid(row=2, column=2, sticky=W)
        interface.append(check4)

        varC1 = IntVar()
        check5 = Checkbutton(frame, text="C1", variable=varC1)
        check5.grid(row=1, column=3, sticky=W)
        interface.append(check5)

        varC2 = IntVar()
        check6 = Checkbutton(frame, text="C2", variable=varC2)
        check6.grid(row=2, column=3, sticky=W)
        interface.append(check6)

        varO = IntVar()
        check7 = Checkbutton(frame, text="Others", variable=varO)
        check7.grid(row=3, column=2, sticky=W)
        interface.append(check7)

        przycisk = Button(self.root, text='Aktualizuj bazę',
                          command=lambda: [self.checked(varA1, varA2, varB1, varB2, varC1, varC2, varO)])
        przycisk.grid(row=5, columnspan=5)
        interface.append(przycisk)

        przycisk_back = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                               command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_back)
        przycisk_back.grid(row=6, columnspan=5)

        self.inter = interface


class START_PAGE(Page):
    def __init__(self, root, lista, sound):
        super().__init__()
        self.inter = []
        self.root = root
        self.sound = sound
        destroyer(lista)
        self.create()

    def back(self, lista):
        destroyer(lista)
        MENU(self.root, lista, self.sound)

    def start_learn(self, lista):
        tryb = 'LEARN'
        CHOICE_PAGE(self.root, lista, tryb, self.sound)

    def start_challenge(self, lista):
        tryb = 'CHALLENGE'
        CHOICE_PAGE(self.root, lista, tryb, self.sound)

    def configure(self):
        # Kolumny
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)

        # Rzędy
        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=2)

    def create(self):
        interface = []
        self.configure()
        label2 = Label(self.root, text='Druga strona', font=('Comic_Sans', 25))
        label2.grid(row=0, columnspan=5)
        interface.append(label2)

        przycisk_learn = Button(self.root, text='Tryb nauki', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.start_learn(interface)])
        przycisk_learn.grid(row=1, columnspan=5)
        interface.append(przycisk_learn)

        przycisk_challenge = Button(self.root, text='Tryb wyzwania', font=('Comic_Sans', 25),
                                    command=lambda: [beep(), self.start_challenge(interface)])
        przycisk_challenge.grid(row=2, columnspan=5)
        interface.append(przycisk_challenge)

        przycisk_next2 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.back(interface)])
        przycisk_next2.grid(row=7, columnspan=5)
        interface.append(przycisk_next2)

        for elem in interface:
            elem.grid()

        self.inter = interface


class EXIT_PAGE(Page):
    def __init__(self, root, lista, sound):
        super().__init__()
        self.inter = []
        self.root = root
        self.sound = sound
        destroyer(lista)
        self.create()

    def back(self, lista):
        destroyer(lista)
        MENU(self.root, lista, self.sound)

    def Quit(self):
        label = Label(self.root, text='Miłego dnia!', font=('Comic_Sans', 25))
        label.grid(columnspan=5, row=3)
        label.after(1500, label.quit)

    def configure(self):
        # Kolumny
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)

        # Rzędy
        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=2)

    def create(self):
        self.configure()
        interface = []

        label2 = Label(self.root, text='Czy na pewno chcesz opuścić grę?', font=('Comic_Sans', 25))
        interface.append(label2)

        przycisk_quit = Button(self.root, text='Tak', font=('Comic_Sans', 25), command=lambda: [beep(), self.Quit()])
        interface.append(przycisk_quit)

        przycisk_back = Button(self.root, text='Nie', font=('Comic_Sans', 25),
                               command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_back)

        label2.grid(columnspan=5, row=0)
        przycisk_back.grid(column=3, row=1)
        przycisk_quit.grid(column=1, row=1)


class POSTEPY_PAGE(Page):
    def __init__(self, root, lista, sound, count_pos=0, count_neg=0, count_max=0):
        super().__init__()
        self.inter = []
        self.root = root
        self.sound = sound
        self.count_pos = count_pos
        self.count_neg = count_neg
        self.count_max = count_max
        self.container = []
        destroyer(lista)
        self.create()

    def back(self, lista):
        destroyer(lista)
        MENU(self.root, lista, self.sound)

    def checked(self, a1, a2, b1, b2, c1, c2, o):
        listat = []

        a1 = a1.get()
        a2 = a2.get()
        b1 = b1.get()
        b2 = b2.get()
        c1 = c1.get()
        c2 = c2.get()
        o = o.get()

        if a1 == 1:
            listat.append('Baza/A1_words.txt')
        if a2 == 1:
            listat.append('Baza/A2_words.txt')
        if b1 == 1:
            listat.append('Baza/B1_words.txt')
        if b2 == 1:
            listat.append('Baza/B2_words.txt')
        if c1 == 1:
            listat.append('Baza/C1_words.txt')
        if c2 == 1:
            listat.append('Baza/C2_words.txt')
        if o == 1:
            listat.append('Baza/Others.txt')

        list_of_words = []
        for plik in listat:
            with open(plik, 'r+', encoding='UTF-8') as f:
                try:
                    next(f)
                    for line in f:
                        self.count_max += 1
                        list_of_words.append(line)
                    f.close()
                except:
                    f.close()

        with open('umiem.txt', 'r+', encoding='UTF-8') as f:
            try:
                for line in f:
                    if line in list_of_words:
                        self.count_pos += 1
                f.close()
            except:
                f.close()

        with open('nie_umiem.txt', 'r+', encoding='UTF-8') as f:
            try:
                for line in f:
                    if line in list_of_words:
                        self.count_neg += 1
                f.close()
            except:
                f.close()

        labelpos = Label(self.root, text=f'Umiesz: {self.count_pos} z {self.count_max} ', font=('Comic_Sans', 25))
        self.inter.append(labelpos)
        self.container.append(labelpos)
        labelpos.grid(column=4, row=4)

        labelneg = Label(self.root, text=f'Nie umiesz: {self.count_neg} z {self.count_max} ', font=('Comic_Sans', 25))
        self.inter.append(labelneg)
        labelneg.grid(column=4, row=5)
        self.container.append(labelneg)

        labelnz = Label(self.root,
                        text=f'Nieoznaczone: {self.count_max - self.count_neg - self.count_pos} z {self.count_max} ',
                        font=('Comic_Sans', 25))
        self.inter.append(labelnz)
        labelnz.grid(column=4, row=6)
        self.container.append(labelnz)

        figure2 = Figure(figsize=(5, 5), dpi=100)
        subplot2 = figure2.add_subplot(111)
        labels2 = f'Umiem: {round(self.count_pos / self.count_max * 100, 2)}%', f'Nie umiem: {round(self.count_neg / self.count_max * 100, 2)}%', \
                  f'Nieoznaczone: {round((self.count_max - self.count_neg - self.count_pos) / self.count_max * 100, 2)}%'
        pieSizes = [self.count_pos, self.count_neg, self.count_max]
        my_colors2 = ['lime', 'red', 'silver']
        explode2 = (0, 0.1, 0)
        subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, startangle=90)

        subplot2.legend(labels2, loc='lower left')
        pie2 = FigureCanvasTkAgg(figure2, self.root)
        pie2.get_tk_widget().grid(row=4, rowspan=3, column=2)
        self.container.append(pie2)

    def configure(self):
        # Kolumny
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)

        # Rzędy
        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=2)

    def zeren(self):
        self.count_pos = 0
        self.count_neg = 0
        self.count_max = 0

    def d(self):
        try:
            self.container[-1].get_tk_widget().destroy()
            for i in self.container:
                i.destroy()
        except:
            pass
        self.container = []

    def create(self):
        self.configure()
        interface = []

        label2 = Label(self.root, text='POSTĘPY', font=('Comic_Sans', 25))
        interface.append(label2)
        label2.grid(columnspan=5)

        frame = Frame(self.root)
        frame.grid(columnspan=5)
        interface.append(frame)

        varA1 = IntVar()
        check1 = Checkbutton(frame, text="A1", variable=varA1)
        check1.grid(row=1, column=1, sticky=W)
        interface.append(check1)

        varA2 = IntVar()
        check2 = Checkbutton(frame, text="A2", variable=varA2)
        check2.grid(row=2, column=1, sticky=W)
        interface.append(check2)

        varB1 = IntVar()
        check3 = Checkbutton(frame, text="B1", variable=varB1)
        check3.grid(row=1, column=2, sticky=W)
        interface.append(check3)

        varB2 = IntVar()
        check4 = Checkbutton(frame, text="B2", variable=varB2)
        check4.grid(row=2, column=2, sticky=W)
        interface.append(check4)

        varC1 = IntVar()
        check5 = Checkbutton(frame, text="C1", variable=varC1)
        check5.grid(row=1, column=3, sticky=W)
        interface.append(check5)

        varC2 = IntVar()
        check6 = Checkbutton(frame, text="C2", variable=varC2)
        check6.grid(row=2, column=3, sticky=W)
        interface.append(check6)

        varO = IntVar()
        check7 = Checkbutton(frame, text="Others", variable=varO)
        check7.grid(row=3, column=2, sticky=W)
        interface.append(check7)

        przycisk = Button(self.root, text='Aktualizuj',
                          command=lambda: [self.d(), self.zeren(),
                                           self.checked(varA1, varA2, varB1, varB2, varC1, varC2, varO)])

        przycisk.grid(row=3, columnspan=5)
        interface.append(przycisk)

        przycisk_next2 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.zeren(), self.d(), self.back(interface)])
        interface.append(przycisk_next2)
        przycisk_next2.grid(columnspan=5, row=7)

        self.inter = interface


class CHOICE_PAGE(Page):
    def __init__(self, root, lista, tryb, sound):
        super().__init__()
        self.inter = []
        self.root = root
        self.sound = sound
        self.list_of_words = []
        self.tryb = tryb
        destroyer(lista)
        self.create()

    def back(self, lista):
        destroyer(lista)
        START_PAGE(self.root, lista, self.sound)

    def configure(self):
        # Kolumny
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)

        # Rzędy
        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=2)

    def checked(self, a1, a2, b1, b2, c1, c2, o, inter):
        lista = []

        a1 = a1.get()
        a2 = a2.get()
        b1 = b1.get()
        b2 = b2.get()
        c1 = c1.get()
        c2 = c2.get()
        o = o.get()

        if a1 == 1:
            lista.append('Baza/A1_words.txt')
        if a2 == 1:
            lista.append('Baza/A2_words.txt')
        if b1 == 1:
            lista.append('Baza/B1_words.txt')
        if b2 == 1:
            lista.append('Baza/B2_words.txt')
        if c1 == 1:
            lista.append('Baza/C1_words.txt')
        if c2 == 1:
            lista.append('Baza/C2_words.txt')
        if o == 1:
            lista.append('Baza/Others.txt')

        for plik in lista:
            with open(plik, 'r+', encoding='UTF-8') as f:
                try:
                    next(f)
                    for line in f:
                        self.list_of_words.append(line)
                    f.close()
                except:
                    f.close()

        if not self.list_of_words:
            self.show_message_warning()
        else:
            self.play(inter)

    def show_message_warning(self):
        label = Label(self.root, text="Nie wybrano żadnych fiszek!",
                      background="red",
                      foreground="black", height=3, width=50)
        label.grid(columnspan=5, row=4)
        label.after(2000, label.destroy)

    def play(self, lista):
        destroyer(lista)
        if self.tryb == 'LEARN':
            LEARN_PAGE(self.root, lista, self.sound, self.list_of_words)
        elif self.tryb == 'CHALLENGE':
            CHALLENGE_PAGE(self.root, lista, self.sound, self.list_of_words)

    def create(self):
        interface = []
        self.configure()

        label = Label(self.root, text='Choice', font=('Comic_Sans', 25))
        interface.append(label)
        label.grid(row=0, columnspan=5)

        label2 = Label(self.root, text='Wybierz zakres', font=('Comic_Sans', 25))
        label2.grid(row=0, columnspan=5)
        interface.append(label2)

        frame = Frame(self.root)
        frame.grid(row=1, columnspan=5)
        interface.append(frame)

        varA1 = IntVar()
        check1 = Checkbutton(frame, text="A1", variable=varA1)
        check1.grid(row=1, column=1, sticky=W)
        interface.append(check1)

        varA2 = IntVar()
        check2 = Checkbutton(frame, text="A2", variable=varA2)
        check2.grid(row=2, column=1, sticky=W)
        interface.append(check2)

        varB1 = IntVar()
        check3 = Checkbutton(frame, text="B1", variable=varB1)
        check3.grid(row=1, column=2, sticky=W)
        interface.append(check3)

        varB2 = IntVar()
        check4 = Checkbutton(frame, text="B2", variable=varB2)
        check4.grid(row=2, column=2, sticky=W)
        interface.append(check4)

        varC1 = IntVar()
        check5 = Checkbutton(frame, text="C1", variable=varC1)
        check5.grid(row=1, column=3, sticky=W)
        interface.append(check5)

        varC2 = IntVar()
        check6 = Checkbutton(frame, text="C2", variable=varC2)
        check6.grid(row=2, column=3, sticky=W)
        interface.append(check6)

        varO = IntVar()
        check7 = Checkbutton(frame, text="Others", variable=varO)
        check7.grid(row=3, column=2, sticky=W)
        interface.append(check7)

        przycisk = Button(self.root, text='Rozpocznij',
                          command=lambda: [self.checked(varA1, varA2, varB1, varB2, varC1, varC2, varO, interface)])
        przycisk.grid(row=3, columnspan=5)
        interface.append(przycisk)

        label = Label(self.root, height=3, width=50)
        label.grid(columnspan=5, row=4)
        interface.append(label)

        przycisk_next2 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.back(interface)])
        przycisk_next2.grid(row=5, columnspan=5)
        interface.append(przycisk_next2)

        self.inter = interface


def save(en, file):
    word = en
    print(word)

    flaga = True
    with open(file, 'r+', encoding='UTF-8') as f:
        try:
            for line in f:
                if line == word:
                    flaga = False
                    f.close()
        except:
            f.close()
    if flaga:
        with open(file, 'a+', encoding='UTF-8') as f:
            f.write(word)
            f.close()

        if file == 'umiem.txt':
            with open('nie_umiem.txt', 'r+', encoding='UTF-8') as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != word:
                        f.write(i)
                f.truncate()
                f.close()
        else:
            with open('umiem.txt', 'r+', encoding='UTF-8') as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != word:
                        f.write(i)
                f.truncate()
                f.close()


class LEARN_PAGE(Page):

    def __init__(self, root, lista, sound, words, cpos=0, cneg=0):
        super().__init__()
        self.inter = []
        self.root = root
        self.list_of_words = words
        self.sound = sound
        destroyer(lista)
        self.counter_pos = cpos
        self.counter_neg = cneg
        self.counter_help = 0
        self.create()

    def configure(self):
        # Kolumny
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)

        # Rzędy
        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=2)

    def back(self, lista):
        destroyer(lista)
        CHOICE_PAGE(self.root, lista, 'LEARN', self.sound)

    def helper(self, word):
        if self.counter_help < len(word):
            self.counter_help += 1

        if word[self.counter_help - 1] != ' ':
            h = word[0:self.counter_help]
        else:
            h = word[0:self.counter_help + 1]
            self.counter_help += 1
        label = Label(self.root, text=f"Podpowiedź: {h}",
                      background="cyan",
                      foreground="black", height=3, width=50)
        label.grid(columnspan=5, row=5)

        label.after(2000, label.destroy)

    def ask(self):
        ans = messagebox.askyesno('UWAGA!',
                                  'Czy na pewno chcesz wyjść?\nTwoje postępy zostaną utracone!')
        if ans:
            self.back(self.inter)

    def create(self):
        self.configure()
        interface = []

        labelz = Label(self.root, text='TRYB NAUKI', font=('Comic_Sans', 25))
        interface.append(labelz)
        labelz.grid(row=0, columnspan=5)

        label = Label(self.root, text="Podpowiedź: ", height=3, width=50,
                      background="lime",
                      foreground="black")
        label.grid(columnspan=5, row=5)
        label.after(2000, label.destroy)

        def generate():
            slowo = random.choice(self.list_of_words)
            self.counter_help = 0
            return slowo

        wordos1 = generate()
        wordos = wordos1.split(' - ')

        label3 = Label(self.root, text=wordos[1], font=('Comic_Sans', 25))
        interface.append(label3)
        label3.grid(row=2, columnspan=5)

        entry = Entry(self.root)
        entry.grid(row=3, columnspan=5)
        interface.append(entry)

        def answear():
            ans = entry.get()
            if ans == wordos[0].rstrip():
                self.show_message_good()
                self.counter_pos += 1
            elif len(ans) >= 3 and wordos[0][0:3] == 'to ':
                if ans == wordos[0][3:]:
                    self.show_message_good()
                    self.counter_pos += 1
                else:
                    self.show_message_negative(wordos[0])
                    self.counter_neg += 1
            else:
                self.show_message_negative(wordos[0])
                self.counter_neg += 1
            self.counter_help = 0

        przycisk_next2 = Button(self.root, text='Nowe słowo', font=('Comic_Sans', 25),
                                command=lambda: [beep(),
                                                 LEARN_PAGE(self.root, self.inter, self.sound, self.list_of_words,
                                                            self.counter_pos, self.counter_neg)])
        przycisk_next2.grid(row=4, column=2)
        interface.append(przycisk_next2)

        przycisk_next4 = Button(self.root, text='Odpowiadam', font=('Comic_Sans', 25),
                                command=lambda: [beep(), answear()])
        przycisk_next4.grid(row=4, column=1)
        interface.append(przycisk_next4)

        label = Label(self.root, height=3, width=50)
        label.grid(columnspan=5, row=5)

        przycisk_next0 = Button(self.root, text='UMIEM!', font=('Comic_Sans', 25),
                                command=lambda: [beep(), save(wordos1, 'umiem.txt')])
        interface.append(przycisk_next0)
        przycisk_next0.grid(column=3, row=4)

        przycisk_next8 = Button(self.root, text='NIE UMIEM!', font=('umiem', 25),
                                command=lambda: [beep(), save(wordos1, 'nie_umiem.txt')])
        interface.append(przycisk_next8)
        przycisk_next8.grid(column=4, row=4)

        przycisk_next5 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.ask()])
        interface.append(przycisk_next5)
        przycisk_next5.grid(row=7, columnspan=5)

        przycisk_next6 = Button(self.root, text='Podsumowanie', font=('Comic_Sans', 25),
                                command=lambda: [beep(),
                                                 SUMMARY_PAGE(self.root, self.inter, self.sound, self.counter_neg,
                                                              self.counter_pos, 'LEARN')])

        interface.append(przycisk_next6)
        przycisk_next6.grid(row=6, column=1)

        przycisk_next9 = Button(self.root, text='Podpowiedź', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.helper(wordos[0])])

        interface.append(przycisk_next9)
        przycisk_next9.grid(row=6, column=4)

        interface.append(label)

        self.inter = interface

    def show_message_good(self):
        label = Label(self.root, text="Zgadłeś!", height=3, width=50,
                      background="lime",
                      foreground="black")
        label.grid(columnspan=5, row=5)
        label.after(2000, label.destroy)

    def show_message_negative(self, correct):
        label = Label(self.root, text=f"Nie zgadłeś! Poprawna odpowiedź to: {correct}", height=3, width=50,
                      background="red",
                      foreground="black")
        label.grid(columnspan=5, row=5)
        label.after(2000, label.destroy)


class CHALLENGE_PAGE(Page):

    def __init__(self, root, lista, sound, words):
        super().__init__()
        self.inter = []
        self.root = root
        self.sound = sound
        self.list_of_words = words
        destroyer(lista)
        self.create()

    def back(self, lista):
        destroyer(lista)
        CHOICE_PAGE(self.root, lista, 'CHALLENGE', self.sound)

    def create(self):
        interface = []
        label2 = Label(self.root, text='Wybierz tryb gry', font=('Comic_Sans', 25))
        interface.append(label2)
        label2.grid(row=1, columnspan=5)

        przycisk_next2 = Button(self.root, text='Na czas', font=('Comic_Sans', 25),
                                command=lambda: [beep(),
                                                 TIME_PAGE(self.root, self.inter, self.sound, self.list_of_words)])
        interface.append(przycisk_next2)

        przycisk_next2.grid(row=2, columnspan=5)

        przycisk_next3 = Button(self.root, text='Życia', font=('Comic_Sans', 25),
                                command=lambda: [beep(),
                                                 LIFE_PAGE(self.root, self.inter, self.sound, self.list_of_words)])
        interface.append(przycisk_next3)
        przycisk_next3.grid(row=3, columnspan=5)

        przycisk_next4 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_next4)
        przycisk_next4.grid(row=4, columnspan=5)

        self.inter = interface


class TIME_PAGE(Page):
    def __init__(self, root, lista, sound, words, cneg=0, cpos=0, time=120):
        super().__init__()
        self.inter = []
        self.root = root
        self.list_of_words = words
        self.counter_pos = cpos
        self.counter_neg = cneg
        self.sound = sound
        self.time = time
        destroyer(lista)
        self.create()

    def configure(self):
        # Kolumny
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)

        # Rzędy
        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=2)

    def countdown(self, count, label, label2):
        mins = count // 60
        sec = count - 60 * mins
        try:
            label['text'] = f'{mins} minut'
            label2['text'] = f'{sec} sekund'

            if count >= 0:
                self.time -= 1
                self.root.after(1000, self.countdown, count - 1, label, label2)
            else:
                destroyer(self.inter)
                SUMMARY_PAGE(self.root, self.inter, self.sound, self.counter_neg, self.counter_pos, 'CHALLENGE')
        except:
            pass

    def ask(self):
        ans = messagebox.askyesno('UWAGA!',
                                  'Czy na pewno chcesz wyjść?\nTwoje postępy zostaną utracone!')
        if ans:
            self.back(self.inter)

    def show_message_good(self):
        label = Label(self.root, text="Zgadłeś!", height=3, width=50,
                      background="lime",
                      foreground="black")
        label.grid(columnspan=5, row=5)
        label.after(2000, label.destroy)

    def show_message_negative(self):
        label = Label(self.root, text=f"Nie zgadłeś!", height=3, width=50,
                      background="red",
                      foreground="black")
        label.grid(columnspan=5, row=5)
        label.after(2000, label.destroy)

    def back(self, lista):
        destroyer(lista)
        CHALLENGE_PAGE(self.root, lista, self.sound, self.list_of_words)

    def answear(self, entry, wordos):
        ans = entry.get()
        if ans == wordos[0].rstrip():
            self.show_message_good()
            self.counter_pos += 1
        elif len(ans) >= 3 and wordos[0][0:3] == 'to ':
            if ans == wordos[0][3:]:
                self.show_message_good()
                self.counter_pos += 1
            else:
                self.show_message_negative()
                self.counter_neg += 1
        else:
            self.show_message_negative()
            self.counter_neg += 1
        self.counter_help = 0

        TIME_PAGE(self.root, self.inter, self.sound, self.list_of_words, self.counter_neg,
                  self.counter_pos, self.time)

    def create(self):
        interface = []
        label2 = Label(self.root, text='WYZWANIE CZASOWE', font=('Comic_Sans', 25))
        interface.append(label2)
        label2.grid(columnspan=5, row=0)

        laber = Label(self.root, text='Pozostały czas:')
        interface.append(laber)
        laber.grid(row=1, column=1)

        lab = Label(self.root)
        interface.append(lab)
        lab.grid(row=1, column=2)

        lab2 = Label(self.root)
        interface.append(lab2)
        lab2.grid(row=1, column=3)

        self.countdown(self.time, lab, lab2)

        def generate():
            slowo = random.choice(self.list_of_words)
            self.counter_help = 0
            return slowo

        wordos1 = generate()
        wordos = wordos1.split(' - ')

        label3 = Label(self.root, text=wordos[1], font=('Comic_Sans', 25))
        interface.append(label3)
        label3.grid(row=2, columnspan=5)

        entry = Entry(self.root)
        entry.grid(row=3, columnspan=5)
        interface.append(entry)

        przycisk_next4 = Button(self.root, text='Odpowiadam', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.answear(entry, wordos)])
        przycisk_next4.grid(row=4, columnspan=5)
        interface.append(przycisk_next4)

        przycisk_next5 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.ask()])
        interface.append(przycisk_next5)
        przycisk_next5.grid(row=7, columnspan=5)

        self.inter = interface


class LIFE_PAGE(Page):
    def __init__(self, root, lista, sound, words, cpos=0, cneg=0, life=3, av_help=3):
        super().__init__()
        self.inter = []
        self.root = root
        self.sound = sound
        self.counter_pos = cpos
        self.counter_neg = cneg
        self.list_of_words = words
        self.av_help = av_help
        self.counter_help = 0
        self.life = life
        destroyer(lista)
        self.create()

    def back(self, lista):
        destroyer(lista)
        CHALLENGE_PAGE(self.root, lista, self.sound, self.list_of_words)

    def configure(self):
        # Kolumny
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)

        # Rzędy
        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=2)

    def helper(self, word):
        if self.av_help != 0:
            self.av_help -= 1
            if self.counter_help < len(word):
                self.counter_help += 1

            if word[self.counter_help - 1] != ' ':
                h = word[0:self.counter_help]
            else:
                h = word[0:self.counter_help + 1]
                self.counter_help += 1
            label = Label(self.root, text=f"Podpowiedź: {h}\nPozostałe podpowiedzi: {self.av_help}",
                          background="cyan",
                          foreground="black", height=3, width=50)
            label.grid(columnspan=5, row=5)
            label.after(2000, label.destroy)
        else:
            label = Label(self.root, text=f"Wykorzystano już wszystkie podpowiedzi!",
                          background="cyan",
                          foreground="black", height=3, width=50)
            label.grid(columnspan=5, row=5)
            label.after(2000, label.destroy)

    def ask(self):
        ans = messagebox.askyesno('UWAGA!',
                                  'Czy na pewno chcesz wyjść?\nTwoje postępy zostaną utracone!')
        if ans:
            self.back(self.inter)

    def answear(self, entry, wordos):
        ans = entry.get()
        if ans == wordos[0].rstrip():
            self.counter_pos += 1
            self.show_message_good()
        elif len(ans) >= 3 and wordos[0][0:3] == 'to ':
            if ans == wordos[0][3:]:
                self.counter_pos += 1
                self.show_message_good()
            else:
                self.life -= 1
                self.counter_neg += 1
                self.show_message_negative()

        else:
            self.life -= 1
            self.counter_neg += 1
            self.show_message_negative()

        self.counter_help = 0
        if self.life == 0:
            time.sleep(1)
            SUMMARY_PAGE(self.root, self.inter, self.sound, self.counter_neg, self.counter_pos, 'CHALLENGE')
        else:
            LIFE_PAGE(self.root, self.inter, self.sound, self.list_of_words, self.counter_pos, self.counter_neg,
                      self.life, self.av_help)

    def create(self):
        self.configure()

        interface = []
        label2 = Label(self.root, text='WYZWANIE NA ŻYCIA', font=('Comic_Sans', 25))
        interface.append(label2)
        label2.grid(columnspan=5, row=0)

        def generate():
            slowo = random.choice(self.list_of_words)
            self.counter_help = 0
            return slowo

        wordos1 = generate()
        wordos = wordos1.split(' - ')

        label3 = Label(self.root, text=wordos[1], font=('Comic_Sans', 25))
        interface.append(label3)
        label3.grid(row=2, columnspan=5)

        entry = Entry(self.root)
        entry.grid(row=3, columnspan=5)
        interface.append(entry)

        przycisk_next4 = Button(self.root, text='Odpowiadam', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.answear(entry, wordos)])
        przycisk_next4.grid(row=4, column=1)
        interface.append(przycisk_next4)

        przycisk_next5 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.ask()])
        interface.append(przycisk_next5)
        przycisk_next5.grid(row=7, columnspan=5)

        przycisk_next9 = Button(self.root, text='Podpowiedź', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.helper(wordos[0])])

        interface.append(przycisk_next9)
        przycisk_next9.grid(row=4, column=3)

        self.inter = interface

    def show_message_good(self):
        label = Label(self.root, text="Zgadłeś!", height=3, width=50,
                      background="lime",
                      foreground="black")
        label.grid(columnspan=5, row=5)
        label.after(2000, label.destroy)

    def show_message_negative(self):
        label = Label(self.root, text=f"Nie zgadłeś! Pozostałe szansy: {self.life} ", height=3, width=50,
                      background="red",
                      foreground="black")
        label.grid(columnspan=5, row=5)
        label.after(2000, label.destroy)


class SUMMARY_PAGE(Page):

    def __init__(self, root, lista, sound, cneg, cpos, name):
        super().__init__()
        self.inter = []
        self.root = root
        self.name = name
        self.sound = sound
        self.counter_pos = cpos
        self.counter_neg = cneg
        destroyer(lista)
        self.create()

    def again(self, lista):
        destroyer(lista)

        if self.name == 'CHALLENGE':
            CHOICE_PAGE(self.root, lista, 'CHALLENGE', self.sound)
        else:
            CHOICE_PAGE(self.root, lista, 'LEARN', self.sound)

    def configure(self):
        # Kolumny
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)

        # Rzędy
        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=2)

    def create(self):
        interface = []
        label2 = Label(self.root, text='Podsumowanie', font=('Comic_Sans', 25))
        interface.append(label2)
        label2.grid(row=0, columnspan=5)

        przycisk_next2 = Button(self.root, text='Powrót do Menu', font=('Comic_Sans', 25),
                                command=lambda: [beep(), destroyer(self.inter), canvas.get_tk_widget().destroy(),
                                                 MENU(self.root, self.inter, self.sound)])
        interface.append(przycisk_next2)
        przycisk_next2.grid(row=4, column=3)

        przycisk_next3 = Button(self.root, text='Zagraj ponownie', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.again(interface), canvas.get_tk_widget().destroy()])
        interface.append(przycisk_next3)
        przycisk_next3.grid(row=4, column=1)

        label3 = Label(self.root, text=f'Pozytywnie odpowiedziano {self.counter_pos} razy', font=('Comic_Sans', 25))
        interface.append(label3)
        label3.grid(row=2, columnspan=5)

        label4 = Label(self.root, text=f'Negatywnie odpowiedziano {self.counter_neg} razy', font=('Comic_Sans', 25))
        interface.append(label4)
        label4.grid(row=3, columnspan=5)

        matplotlib.use("TkAgg")

        figure = Figure(figsize=(5, 5), dpi=100)

        data = (self.counter_pos, self.counter_neg)
        ax = figure.add_subplot(111)

        ind = np.arange(2)
        width = .8

        ax.bar(ind, data, width, color=['green', 'red'])
        ax.set_title('Wyniki')
        ax.set_xticks(range(2), ['Prawidłowe', 'Nieprawidłowe'])

        canvas = FigureCanvasTkAgg(figure, self.root)
        canvas.get_tk_widget().grid(row=1, columnspan=5)

        self.inter = interface


def beep():
    mixer.init()
    s = mixer.Sound("App_interactions/Klik.wav")
    s.play()


if __name__ == '__main__':
    App()
