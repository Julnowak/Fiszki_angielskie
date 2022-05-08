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

    def WYBOR(self):
        WYBOR_PAGE(self.root, self.inter)

    def DODAJ(self):
        DODAJ_PAGE(self.root, self.inter)

    def BAZA(self):
        WYBOR_PAGE(self.root, self.inter)

    def POSTEPY(self):
        POSTEPY_PAGE(self.root, self.inter)

    def OPCJE(self):
        OPCJE_PAGE(self.root, self.inter)

    def EXIT(self):
        EXIT_PAGE(self.root, self.inter)

    def create(self):
        interface = []

        label = Label(self.root, text='NAZWA', font=('Comic_Sans', 25))
        interface.append(label)
        # Przyciski
        przycisk_start = Button(self.root, text='Graj', width=8, command=lambda: [beep(), self.WYBOR()])
        interface.append(przycisk_start)

        przycisk_dodaj = Button(self.root, text='Dodaj fiszkę', command=lambda: [beep(), self.DODAJ()])
        interface.append(przycisk_dodaj)

        przycisk_usun = Button(self.root, text='Baza fiszek', command=lambda: [beep(), self.BAZA()])
        interface.append(przycisk_usun)

        przycisk_postepy = Button(self.root, text='Postępy', command=lambda: [beep(), self.POSTEPY()])
        interface.append(przycisk_postepy)

        przycisk_opcji = Button(self.root, text='Opcje', command=lambda: [beep(), self.OPCJE()])
        interface.append(przycisk_opcji)

        przycisk_exit = Button(self.root, text='Wyjście', command=lambda: [beep(), self.EXIT()])
        interface.append(przycisk_exit)

        for elem in interface:
            elem.pack()

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

    def create(self):
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

        przycisk_submit = Button(self.root, text='Dodaj', font=('Comic_Sans', 25), command=lambda: [beep(), self.submit
        (interface[2], interface[4], interface[6], interface[8]), self.clear_text([interface[2], interface[4],
                                                                                  interface[6], interface[8]])])
        interface.append(przycisk_submit)

        przycisk_next2 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.back(self.inter)])
        interface.append(przycisk_next2)

        labeltip = Label(self.root, text='Nie musisz wprowadzać poziomu - twoja fiszka zostanie wprowadzona do katalogu roboczego\n Możesz ją edytować później.', font=('Comic_Sans', 16))
        interface.append(labeltip)

        for elem in interface:
            elem.pack()

        self.inter = interface

    def back(self, lista):
        self.destroyer(lista)
        MENU(self.root, lista)

    def show_message_good(self):
        label = Label(self.root, text="Fiszka została dodana",
                         background="lime",
                         foreground="black")
        label.pack()
        label.after(2000, label.destroy)

    def show_message_neutral(self):
        label = Label(self.root, text="Fiszka została dodana do katalogu 'Inne'\nUpewnij się, że dobrze wpisałeś poziom.",
                         background="yellow",
                         foreground="black")
        label.pack()
        label.after(2500, label.destroy)

    def show_message_negative(self):
        label = Label(self.root, text="Nie uzupełniono jednej z rubryk! Spróbuj jeszcze raz",
                         background="red",
                         foreground="black")
        label.pack()
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
        label.pack()
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

    def create(self):
        pass
        # label = Label(root, text='Baza danych', font=('Comic_Sans', 25))
        # label.pack()
        #
        # things = [{"dictionaryItem": "value"}, {"anotherDict": "itsValue"}, 10, "foo", ["bar", "baz"]]
        # # f = Frame(root).pack()
        # l = Listbox(root)
        #
        # l.pack()
        # num = 0
        # for i in list_of_words:
        #     l.insert(num, i)
        #     num += 1
        #
        # scrollbar = Scrollbar(root, orient='vertical', command=l.yview)
        # l.config(yscrollcommand=scrollbar.set)
        #
        # def delete(listbox):
        #     global things
        #     # Delete from Listbox
        #     selection = l.curselection()
        #     l.delete(selection[0])
        #     # Delete from list that provided it
        #     value = eval(l.get(selection[0]))
        #     ind = things.index(value)
        #     del (things[ind])
        #     print(things)
        #
        # b = Button(root, text="Usuń", command=lambda: delete(l))
        # b.pack()
        #
        # przycisk_back = Button(root, text='Poprzednia strona', font=('Comic_Sans', 25),
        #                        command=lambda: [beep(), back()])
        # przycisk_back.pack(side=BOTTOM)


class WYBOR_PAGE(Page):
    def __init__(self, root, lista):
        super().__init__()
        self.inter = []
        self.root = root
        self.destroyer(lista)
        self.create()


    def back(self, lista):
        self.destroyer(lista)
        MENU(self.root, lista)

    def start_lean(self):
        pass

    def start_challenge(self):
        pass

    def create(self):
        interface = []
        label2 = Label(self.root, text='Druga strona', font=('Comic_Sans', 25))
        interface.append(label2)


        przycisk_next2 = Button(self.root, text='Poprzednia strona', font=('Comic_Sans', 25),
                                command=lambda: [beep(), self.back(interface)])
        interface.append(przycisk_next2)

        przycisk_learn = Button(self.root, text='Tryb nauki', font=('Comic_Sans', 25), command=lambda: [beep(), self.start_lean()])
        interface.append(przycisk_learn)

        przycisk_challenge = Button(self.root, text='Tryb wyzwania', font=('Comic_Sans', 25), command=lambda: [beep()])
        interface.append(przycisk_challenge)

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
        # MILEGO DNIA jeszcze
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

def beep():
    mixer.init()
    s = mixer.Sound("Sounds/Klik.wav")
    s.play()


if __name__ == '__main__':
    App()
