from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
import time
from pygame import mixer
# Tutaj robi dźwięki :P
import winsound


# winsound.Beep(1200, 200)


class Page:
    def __init__(self):
        self.lista = []

    def destroyer(self, lista):
        for elem in lista:
            elem.destroy()
        return lista


class MENU(Page):
    def __init__(self, root, lista):
        super(MENU, self).__init__()
        self.root = root
        self.inter = lista
        self.create()

    def START(self):
        START_PAGE(self.root, self.inter)

    def DODAJ(self):
        DODAJ_PAGE(self.root, self.inter)

    def BAZA(self):
        BAZA_PAGE(self.root, self.inter)

    def POSTEPY(self):
        POSTEPY_PAGE(self.root, self.inter)

    def OPCJE(self):
        OPCJE_PAGE(self.root, self.inter)

    def EXIT(self):
        EXIT_PAGE(self.root, self.inter)

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
        przycisk_start = Button(self.root, text='Graj', height=3, width=20,font=('Comic_Sans', 14), command=lambda: [beep(), self.START()])
        interface.append(przycisk_start)

        przycisk_dodaj = Button(self.root, text='Dodaj fiszkę', height=3, width=20,font=('Comic_Sans', 14), command=lambda: [beep(), self.DODAJ()])
        interface.append(przycisk_dodaj)

        przycisk_usun = Button(self.root, text='Baza fiszek', height=3, width=20,font=('Comic_Sans', 14), command=lambda: [beep(), self.BAZA()])
        interface.append(przycisk_usun)

        przycisk_postepy = Button(self.root, text='Postępy', height=3, width=20,font=('Comic_Sans', 14), command=lambda: [beep(), self.POSTEPY()])
        interface.append(przycisk_postepy)

        przycisk_opcji = Button(self.root, text='Opcje', height=3, width=20,font=('Comic_Sans', 14), command=lambda: [beep(), self.OPCJE()])
        interface.append(przycisk_opcji)

        przycisk_exit = Button(self.root, text='Wyjście', height=3, width=20,font=('Comic_Sans', 14), command=lambda: [beep(), self.EXIT()])
        interface.append(przycisk_exit)

        image = Image.open('bober.png')
        display = ImageTk.PhotoImage(image)

        label4 = Label(self.root, image=display)
        interface.append(label4)

        label.grid(column=1, row=0)
        przycisk_start.grid(column=1, row=1)
        przycisk_dodaj.grid(column=1, row=2)
        przycisk_usun.grid(column=1, row=3)
        przycisk_postepy.grid(column=1, row=4)
        przycisk_opcji.grid(column=1, row=5)
        przycisk_exit.grid(column=1, row=6)

        self.inter = interface


class App(Page):
    def __init__(self):
        super().__init__()

        # Tworzy okno
        self.root = Tk()
        self.root.title('Fiszki angielsko-polskie')

        self.width = 1000  # width for the Tk root
        self.height = 800  # height for the Tk root

        # get screen width and height
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (self.width / 2)
        y = (hs / 2) - (self.height / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))

        self.track_pages = dict()

        mixer.init()
        self.sound = mixer.Sound("Sounds/muzyka.wav")
        self.sound.set_volume(0.1)
        self.sound.play(-1)

        self.inter = []
        MENU(self.root, self.inter)
        self.root.mainloop()


class DODAJ_PAGE(Page):
    baza = {'A1': 'Baza/A1_words.txt',
            'A2': 'Baza/A2_words.txt',
            'B1': 'Baza/B1_words.txt',
            'B2': 'Baza/B2_words.txt',
            'C1': 'Baza/C1_words.txt',
            'C2': 'Baza/C2_words.txt'}

    def __init__(self, root, lista):
        super().__init__()
        self.inter = []
        self.root = root
        self.destroyer(lista)
        self.create()

    def configure(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
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
        lvl = Label(self.root, text='Poziom', font=('Comic_Sans', 16))
        interface.append(lvl)

        wejscielvl = Entry(self.root, width=40)
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

        przycisk_submit = Button(self.root, text='Dodaj', height=3, width=20,font=('Comic_Sans', 14), command=lambda: [beep(), self.submit
        (interface[2], interface[4], interface[6], interface[8]), self.clear_text([interface[2], interface[4],
                                                                                  interface[6], interface[8]])])
        interface.append(przycisk_submit)

        przycisk_back = Button(self.root, text='Poprzednia strona', height=3, width=20,font=('Comic_Sans', 14),
                                command=lambda: [beep(), self.back(self.inter)])
        interface.append(przycisk_back)

        labeltip = Label(self.root, text='Nie musisz wprowadzać poziomu - twoja fiszka zostanie wprowadzona do katalogu roboczego\n Możesz ją edytować później.', font=('Comic_Sans', 16))
        interface.append(labeltip)

        self.inter = interface
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
        self.destroyer(lista)
        MENU(self.root, lista)

    def show_message_good(self):
        label = Label(self.root, text="Fiszka została dodana", height=3, width=20,
                         background="lime",
                         foreground="black")
        label.grid(column=1, row=6)
        label.after(2000, label.destroy)

    def show_message_neutral(self):
        label = Label(self.root, text="Fiszka została dodana do katalogu 'Inne'\nUpewnij się, że dobrze wpisałeś poziom.",
                         background="yellow",
                         foreground="black")
        label.grid(column=1, row=6)
        label.after(2500, label.destroy)

    def show_message_negative(self):
        label = Label(self.root, text="Nie uzupełniono jednej z rubryk! Spróbuj jeszcze raz", height=3, width=50,
                         background="red",
                         foreground="black")
        label.grid(column=1, row=6)
        label.after(2000, label.destroy)

    def show_message_isHere(self,a,p):
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
                         foreground="black")
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
                with open(self.baza[lvl], 'a+', encoding='UTF-8') as f:

                    f.write(f"{ang} - {pol} - {kat}\n")
                self.show_message_good()
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
                            ans = self.show_message_isHere(a,p)
                            break
                if ans:
                    with open('Baza/Others.txt', 'a+', encoding='UTF-8') as f:
                        f.write(f"{ang} - {pol} - {kat}\n")
                    self.show_message_neutral()
                else:
                    self.show_message_info()
            f.close()
        else:
            self.show_message_negative()

    def clear_text(self, entries):
        for entry in entries:
            entry.delete(0, 'end')


class OPCJE_PAGE(Page):
    def __init__(self, root, lista):
        super().__init__()
        self.inter = []
        self.root = root
        self.destroyer(lista)
        self.create()

    def back(self, lista):
        self.destroyer(lista)
        MENU(self.root, lista)

    def create(self):
        interface = []
        label2 = Label(self.root, text='Strona opcji', font=('Comic_Sans', 25))
        interface.append(label2)

        przycisk_next2 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_next2)

        for elem in interface:
            elem.pack()

        self.inter = interface

class BAZA_PAGE(Page):
    def __init__(self, root, lista):
        super().__init__()
        self.inter = []
        self.root = root
        self.destroyer(lista)
        self.create()

    def back(self, lista):
        self.destroyer(lista)
        MENU(self.root, lista)


    def get(self,click):
        userline = click.get('active')
        print(userline)

    def create(self):
        interface = []
        label = Label(self.root, text='Baza danych', font=('Comic_Sans', 25))
        interface.append(label)

        scroll = Scrollbar(self.root)
        scroll.pack(side='right', fill='y')

        leftside = Listbox(self.root, yscrollcommand=scroll.set)
        for line in range(10):
            leftside.insert('end', "Scale " + str(line))

        leftside.pack()

        selectbutton = Button(self.root, text="Select", command=lambda: [self.get(leftside)])
        selectbutton.pack()

        przycisk_back = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                               command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_back)

        for elem in interface:
            elem.pack()

        self.inter = interface


class START_PAGE(Page):
    def __init__(self, root, lista):
        super().__init__()
        self.inter = []
        self.root = root
        self.destroyer(lista)
        self.create()

    def back(self, lista):
        self.destroyer(lista)
        MENU(self.root, lista)

    def start_learn(self,lista):
        LEARN_PAGE(self.root, lista)

    def start_challenge(self,lista):
        LEARN_PAGE(self.root, lista)

    def create(self):
        interface = []
        label2 = Label(self.root, text='Druga strona', font=('Comic_Sans', 25))
        interface.append(label2)

        przycisk_learn = Button(self.root, text='Tryb nauki', font=('Comic_Sans', 25), command=lambda: [beep(), self.start_learn(interface)])
        interface.append(przycisk_learn)

        przycisk_challenge = Button(self.root, text='Tryb wyzwania', font=('Comic_Sans', 25), command=lambda: [beep(), self.start_challenge(interface)])
        interface.append(przycisk_challenge)

        przycisk_next2 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_next2)

        for elem in interface:
            elem.pack()

        self.inter = interface


class EXIT_PAGE(Page):
    def __init__(self, root, lista):
        super().__init__()
        self.inter = []
        self.root = root
        self.destroyer(lista)
        self.create()

    def back(self, lista):
        self.destroyer(lista)
        MENU(self.root, lista)

    def Quit(self):
        label = Label(self.root, text='Miłego dnia!', font=('Comic_Sans', 25))
        label.pack()
        label.after(1500, label.quit)

    def create(self):
        interface = []

        label2 = Label(self.root, text='Czy na pewno chcesz opuścić grę?', font=('Comic_Sans', 25))
        interface.append(label2)

        przycisk_back = Button(self.root, text='Nie', width=15, height=5, font=('Comic_Sans', 25),
                               command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_back)
        przycisk_quit = Button(self.root, text='Tak', font=('Comic_Sans', 25), command=lambda: [beep(), self.Quit()])
        interface.append(przycisk_quit)

        for elem in interface:
            elem.pack()

        self.inter = interface


class POSTEPY_PAGE(Page):
    def __init__(self, root, lista):
        super().__init__()
        self.inter = []
        self.root = root
        self.destroyer(lista)
        self.create()

    def back(self, lista):
        self.destroyer(lista)
        MENU(self.root, lista)

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


class LEARN_PAGE(Page):
    baza = {'A1': 'Baza/A1_words.txt',
            'A2': 'Baza/A2_words.txt',
            'B1': 'Baza/B1_words.txt',
            'B2': 'Baza/B2_words.txt',
            'C1': 'Baza/C1_words.txt',
            'C2': 'Baza/C2_words.txt'}

    def __init__(self, root, lista):
        super().__init__()
        self.inter = []
        self.root = root
        self.destroyer(lista)
        self.create()

    def back(self, lista):
        self.destroyer(lista)
        START_PAGE(self.root, lista)

    def onPress(self,i,table):
        table[i] = not table[i]

    def create(self):
        interface = []
        label2 = Label(self.root, text='Strona uczenia', font=('Comic_Sans', 25))
        interface.append(label2)

        przycisk_next2 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_next2)

        is_checked = []


        for elem in interface:
            elem.pack()

        # Nieco zmienić i będzie działać
        # for i in range(7):
        #     chk = Checkbutton(self.root, text=str(i), command=(lambda i=i: self.onPress(i, is_checked)))
        #     interface.append(chk)
        #     is_checked.append(0)
        #     print(is_checked)

        self.inter = interface


class CHALLENGE_PAGE(Page):
    baza = {'A1': 'Baza/A1_words.txt',
            'A2': 'Baza/A2_words.txt',
            'B1': 'Baza/B1_words.txt',
            'B2': 'Baza/B2_words.txt',
            'C1': 'Baza/C1_words.txt',
            'C2': 'Baza/C2_words.txt'}

    def __init__(self, root, lista):
        super().__init__()
        self.inter = []
        self.root = root
        self.destroyer(lista)
        self.create()

    def back(self, lista):
        self.destroyer(lista)
        START_PAGE(self.root, lista)

    def create(self):
        interface = []
        label2 = Label(self.root, text='Strona wyzwania', font=('Comic_Sans', 25))
        interface.append(label2)

        przycisk_next2 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_next2)

        for elem in interface:
            elem.pack()

        self.inter = interface


class TIME_PAGE(Page):
    def __init__(self, root, lista):
        super().__init__()
        self.inter = []
        self.root = root
        self.destroyer(lista)
        self.create()

    def back(self, lista):
        self.destroyer(lista)
        CHALLENGE_PAGE(self.root, lista)

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
    def __init__(self, root, lista):
        super().__init__()
        self.inter = []
        self.root = root
        self.destroyer(lista)
        self.create()

    def back(self, lista):
        self.destroyer(lista)
        CHALLENGE_PAGE(self.root, lista)

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
    s = mixer.Sound("Sounds/Klik.wav")
    s.play()


if __name__ == '__main__':
    App()
