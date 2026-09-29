from enums import *

class Plansza:
    def __init__(self, rozmiar: int):
        self.plansza = [[Tile.BORDER for _ in range(rozmiar + 2)] if i == 0 or i == rozmiar + 1 else [Tile.BORDER if k == 0 or k == rozmiar + 1 else Tile.EMPTY for k in range(rozmiar + 2)] for i in range(rozmiar + 2)]
        
        # Ta linijka u góry tworzy planszę w jednej linijce. (Mogłem to zrobić w bardziej rozbudowanej funckji ale python to python :P)
        # 55555555555
        # 50000000005    (5 to ramka, a 0 to pusty tile. jeśli rozmiar jest podany 9 to jest 11 rzędów i 11 kolumn ponieważ ramka z każdej strony liczy się jako pole)
        # 50000000005
        # 50000000005
        # 50000000005
        # 50000000005
        # 50000000005
        # 50000000005
        # 50000000005 
        # 50000000005
        # 55555555555
        
    def debug_printuj_plansze(self): ## Nie do używania !!!
        for rzad in self.plansza:
            for pole in rzad:
                print(pole.value, end="")
            print()
    
    def zmien_pole(self, x, y, pole: Tile):
        self.plansza[y][x] = pole
        