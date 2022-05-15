from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
import time
from pygame import mixer


# Tutaj robi dźwięki :P


def destroyer(lista):
    for elem in lista:
        elem.destroy()
    return lista


class Page:
    def __init__(self):
        self.lista = []


class MENU(Page):
    def __init__(self, root, lista, sound=None):
        super(MENU, self).__init__()
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
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(0, weight=10)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=10)

    def create(self):
        self.configure()
        interface = []

        label = Label(self.root, text='BEAVER DAM', font=('Comic_Sans', 25))
        interface.append(label)

        # Przyciski

        przycisk_start = Button(self.root, text='Graj', height=3, width=20, font=('Comic_Sans', 14),
                                command=lambda: [beep(), self.START()])
        interface.append(przycisk_start)

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

        label.grid(columnspan=5, row=0)
        przycisk_start.grid(columnspan=5, rows=1)
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
        print(self.sound)

        self.inter = []
        MENU(self.root, self.inter, self.sound)
        self.root.mainloop()


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
                                                  self.clear_text([interface[2], interface[4],
                                                                   interface[6], interface[8]])])
        interface.append(przycisk_submit)

        przycisk_back = Button(self.root, text='Poprzednia strona', height=3, width=20, font=('Comic_Sans', 14),
                               command=lambda: [beep(), self.back(self.inter)])
        interface.append(przycisk_back)

        labeltip = Label(self.root,
                         text='Nie musisz wprowadzać poziomu - twoja fiszka zostanie wprowadzona do katalogu roboczego\n Możesz ją edytować później.',
                         font=('Comic_Sans', 16))
        interface.append(labeltip)

        l = Label(self.root, height=3, width=50, bg="black", fg="#000")
        interface.append(l)

        self.inter = interface

        l.grid(column=1, row=6)
        label2.grid(column=1, row=0)
        lvl.grid(column=1, row=1)
        wejscielvl.grid(column=1, row=2)
        labelANG.grid(column=0, row=3)
        wejscieANG.grid(column=0, row=4)
        labelPOL.grid(column=1, row=3)
        wejsciePOL.grid(column=1, row=4)
        labelKAT.grid(column=2, row=3)
        wejscieKAT.grid(column=2, row=4)
        przycisk_submit.grid(column=1, row=5)
        przycisk_back.grid(column=1, row=7)

    def back(self, lista):
        destroyer(lista)
        MENU(self.root, lista, self.sound)

    def show_message_good(self):
        label = Label(self.root, text="Fiszka została dodana", height=3, width=50,
                      background="lime",
                      foreground="black")
        label.grid(column=1, row=6)
        label.after(2000, label.destroy)

    def show_message_negative(self):
        label = Label(self.root, text="Nie uzupełniono jednej z rubryk! Spróbuj jeszcze raz", height=3, width=50,
                      background="red",
                      foreground="black")
        label.grid(column=1, row=6)
        label.after(2000, label.destroy)

    def show_message_isHere(self, a, p):
        if a and p:
            return messagebox.askyesno('Wykryto identyczne słówko!', 'Czy aby na pewno chcesz dodać fiszkę?')
        elif a:
            return messagebox.askyesno('Wykryto powtórzenie w słówku angielskim!',
                                       'Czy aby na pewno chcesz dodać fiszkę?')
        elif p:
            return messagebox.askyesno('Wykryto powtórzenie w słówku polskim!',
                                       'Czy aby na pewno chcesz dodać fiszkę?')

    def show_message_info(self):
        label = Label(self.root, text="Fiszka nie została dodana",
                      background="cyan",
                      foreground="black", height=3, width=50)
        label.grid(column=1, row=6)
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
                        print(lista)
                        if pol == lista[1]:

                            p = True
                        else:
                            p = False

                        if a or p:
                            print(a)
                            ans = self.show_message_isHere(a, p)
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
                            ans = self.show_message_isHere(a, p)
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

    def clear_text(self, entries):
        for entry in entries:
            entry.delete(0, 'end')


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

    def up_sound(self):
        a = self.sound.get_volume() + 0.1
        self.sound.set_volume(a)

    def down_sound(self):
        a = self.sound.get_volume() - 0.1
        self.sound.set_volume(a)

    def change_music(self):
        a = self.sound.get_volume()
        self.sound.stop()
        self.sound = mixer.Sound("Sounds/" + random.choice(os.listdir("Sounds")))
        self.sound.set_volume(a)
        self.sound.play(-1)

    def create(self):
        interface = []
        label2 = Label(self.root, text='Strona opcji', font=('Comic_Sans', 25))
        interface.append(label2)

        przycisk_next3 = Button(self.root, text='Up', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.up_sound()])
        interface.append(przycisk_next3)

        przycisk_next4 = Button(self.root, text='Down', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.down_sound()])
        interface.append(przycisk_next4)

        przycisk_next4 = Button(self.root, text='Zmiana', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.change_music()])
        interface.append(przycisk_next4)

        przycisk_next2 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_next2)

        for elem in interface:
            elem.pack()

        self.inter = interface


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
        MENU(self.root, lista)

    def configure(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)
        self.root.rowconfigure(0, weight=10)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=10)

    def show_message_isHere(self, a, p):
        if a and p:
            return messagebox.askyesno('Wykryto identyczne słówko!', 'Czy aby na pewno chcesz dodać fiszkę?')
        elif a:
            return messagebox.askyesno('Wykryto powtórzenie w słówku angielskim!',
                                       'Czy aby na pewno chcesz dodać fiszkę?')
        elif p:
            return messagebox.askyesno('Wykryto powtórzenie w słówku polskim!',
                                       'Czy aby na pewno chcesz dodać fiszkę?')

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

    def edit(self):
        win = Tk()

        def create_window():
            new_window = Toplevel(win)

        win.after(3000, create_window)
        entryText = StringVar()
        entry = Entry(win, textvariable=entryText)
        entryText.set("Hello World")
        entry.pack()
        win.mainloop()

    def show_message_positive(self):
        label = Label(self.root, text="Poprawnie usunięto fiszkę",
                      background="lime",
                      foreground="black", height=3, width=50)
        label.grid(column=1, row=6)
        label.after(2000, label.destroy)

    def show_message_info(self):
        label = Label(self.root, text="Nie usunięto fiszki",
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

        l.grid(column=1, row=2)
        self.inter.append(l)

        przycisk_remove = Button(self.root, text='Usuń', command=lambda: [beep(), self.are_you_sure(l, lista),BAZA_PAGE(self.root,self.inter,self.sound)])
        przycisk_remove.grid(row=4, column=0)
        self.inter.append(przycisk_remove)

        przycisk_edit = Button(self.root, text='Edytuj', command=lambda: [beep(), self.edit()])
        przycisk_edit.grid(row=4, column=2)
        self.inter.append(przycisk_edit)

    def create(self):
        interface = []

        label = Label(self.root, text='Baza danych', font=('Comic_Sans', 25))
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

        przycisk = Button(self.root, text='Aktualizuj bazę',
                          command=lambda: [self.checked(varA1, varA2, varB1, varB2, varC1, varC2, varO)])
        przycisk.grid(row=3, columnspan=5)
        interface.append(przycisk)

        przycisk_back = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                               command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_back)
        przycisk_back.grid(row=5, columnspan=5)

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

        # Rzędy
        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=2)

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
        label.grid(column=0, columnspan=4, row=3)
        label.after(1500, label.quit)

    def configure(self):
        # Kolumny
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        # Rzędy
        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)

    def create(self):
        self.configure()
        interface = []

        label2 = Label(self.root, text='Czy na pewno chcesz opuścić grę?', font=('Comic_Sans', 25))
        interface.append(label2)

        przycisk_back = Button(self.root, text='Nie', font=('Comic_Sans', 25),
                               command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_back)
        przycisk_quit = Button(self.root, text='Tak', font=('Comic_Sans', 25), command=lambda: [beep(), self.Quit()])
        interface.append(przycisk_quit)

        label2.grid(columnspan=4, row=0)
        przycisk_back.grid(column=1, columnspan=2, row=1)
        przycisk_quit.grid(column=0, columnspan=2, row=1)


class POSTEPY_PAGE(Page):
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

    def create(self):
        interface = []

        label2 = Label(self.root, text='Druga strona', font=('Comic_Sans', 25))
        interface.append(label2)

        przycisk_next2 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_next2)

        for elem in interface:
            elem.pack()

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

    def onPress(self, i, table):
        table[i] = not table[i]

    # def keyboard(self, window):
    #     pass
    #     # def clicked(txt):
    #     #     print(txt)
    #     #
    #     # A = Button(window, text="A", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #               command=lambda: clicked("A"))
    #     # A.grid(column=1, row=1)
    #     #
    #     # btn2 = Button(window, text="R", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #               command=lambda: clicked("R"))
    #     # btn2.grid(column=2, row=1)
    #     # btn3 = Button(window, text="B", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #               command=lambda: clicked("B"))
    #     # btn3.grid(column=3, row=1)
    #     # btn4 = Button(window, text="Z", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #               command=lambda: clicked("Z"))
    #     # btn4.grid(column=4, row=1)
    #     # btn5 = Button(window, text="T", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #               command=lambda: clicked("T"))
    #     # btn5.grid(column=5, row=1)
    #     # btn6 = Button(window, text="I", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #               command=lambda: clicked("I"))
    #     # btn6.grid(column=6, row=1)
    #     # btn7 = Button(window, text="C", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #               command=lambda: clicked("C"))
    #     # btn7.grid(column=7, row=1)
    #     # btn8 = Button(window, text="X", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #               command=lambda: clicked("X"))
    #     # btn8.grid(column=8, row=1)
    #     #
    #     # btn9 = Button(window, text="O", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #               command=lambda: clicked("O"))
    #     # btn9.grid(column=2, row=2)
    #     # btn10 = Button(window, text="Y", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #                command=lambda: clicked("Y"))
    #     # btn10.grid(column=3, row=2)
    #     # btn11 = Button(window, text="P", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #                command=lambda: clicked("P"))
    #     # btn11.grid(column=4, row=2)
    #     # btn12 = Button(window, text="N", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #                command=lambda: clicked("N"))
    #     # btn12.grid(column=5, row=2)
    #     # btn13 = Button(window, text="D", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #                command=lambda: clicked("D"))
    #     # btn13.grid(column=6, row=2)
    #     # btn14 = Button(window, text="W", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #                command=lambda: clicked("W"))
    #     # btn14.grid(column=7, row=2)
    #     #
    #     # btn15 = Button(window, text="V", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #                command=lambda: clicked("V"))
    #     # btn15.grid(column=3, row=3)
    #     # btn16 = Button(window, text="S", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #                command=lambda: clicked("S"))
    #     # btn16.grid(column=4, row=3)
    #     # btn17 = Button(window, text="L", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #                command=lambda: clicked("L"))
    #     # btn17.grid(column=5, row=3)
    #     # btn18 = Button(window, text="U", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #                command=lambda: clicked("U"))
    #     # btn18.grid(column=6, row=3)
    #     #
    #     # btn19 = Button(window, text="M", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #                command=lambda: clicked("M"))
    #     # btn19.grid(column=4, row=4)
    #     # btn20 = Button(window, text="E", bg="skyBlue", fg="Black", width=3, height=1, font=('Helvetica', '20'),
    #     #                command=lambda: clicked("E"))
    #     # btn20.grid(column=5, row=4)

    def configure(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)
        self.root.rowconfigure(0, weight=10)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=10)

    def checked(self, a1, a2, b1, b2, c1, c2, o,inter):
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
            LEARN_PAGE(self.root, lista, self.sound)
        elif self.tryb == 'CHALLENGE':
            CHALLENGE_PAGE(self.root, lista, self.sound)

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
                          command=lambda: [self.checked(varA1, varA2, varB1, varB2, varC1, varC2, varO,interface)])
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


class LEARN_PAGE(Page):

    def __init__(self, root, lista, sound):
        super().__init__()
        self.inter = []
        self.root = root
        self.sound = sound
        destroyer(lista)
        self.create()

    def configure(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)
        self.root.rowconfigure(0, weight=10)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=10)

    def back(self, lista):
        destroyer(lista)
        CHOICE_PAGE(self.root, lista, 'LEARN', self.sound)

    def create(self):
        interface = []
        label2 = Label(self.root, text='Strona nauki', font=('Comic_Sans', 25))
        interface.append(label2)
        label2.grid(row=1, columnspan=5)

        przycisk_next2 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_next2)

        przycisk_next2.grid(row=2, columnspan=5)

        self.inter = interface


class CHALLENGE_PAGE(Page):

    def __init__(self, root, lista, sound):
        super().__init__()
        self.inter = []
        self.root = root
        self.sound = sound
        destroyer(lista)
        self.create()

    def back(self, lista):
        destroyer(lista)
        CHOICE_PAGE(self.root, lista, 'CHALLENGE', self.sound)

    def create(self):
        interface = []
        label2 = Label(self.root, text='Strona wyzwania', font=('Comic_Sans', 25))
        interface.append(label2)
        label2.grid(row=1, columnspan=5)

        przycisk_next2 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_next2)

        przycisk_next2.grid(row=2, columnspan=5)

        self.inter = interface


class TIME_PAGE(Page):
    def __init__(self, root, lista, sound):
        super().__init__()
        self.inter = []
        self.root = root
        self.sound = sound
        destroyer(lista)
        self.create()

    def back(self, lista):
        destroyer(lista)
        CHALLENGE_PAGE(self.root, lista, self.sound)

    def create(self):
        interface = []
        label2 = Label(self.root, text='Strona wyzwanie-czas', font=('Comic_Sans', 25))
        interface.append(label2)

        przycisk_next2 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_next2)

        for elem in interface:
            elem.pack()

        self.inter = interface


class LIFE_PAGE(Page):
    def __init__(self, root, lista, sound):
        super().__init__()
        self.inter = []
        self.root = root
        self.sound = sound
        destroyer(lista)
        self.create()

    def back(self, lista):
        destroyer(lista)
        CHALLENGE_PAGE(self.root, lista, self.sound)

    def create(self):
        interface = []
        label2 = Label(self.root, text='Strona z życiami', font=('Comic_Sans', 25))
        interface.append(label2)

        przycisk_next2 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_next2)

        for elem in interface:
            elem.pack()

        self.inter = interface


def beep():
    mixer.init()
    s = mixer.Sound("App_interactions/Klik.wav")
    s.play()


if __name__ == '__main__':
    App()
