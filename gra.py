from enums import *
from plansza import Plansza

class Gra: ## Główna klasa, tutaj wszystko się dzieje
    def __init__(self, rozmiar: int, bonus: float):
        self.plansza = Plansza(rozmiar)
        self.bonus = bonus
        self.gra_trwa = True
    
    def graj(self, tura_czarny: bool = True):
        x = int(input("Podaj x: "))
        y = int(input("Podaj y: "))
        
        tak = input("Tak: ")
        
        if tak != "":
            self.plansza.sprawdz_punkt(x, y,[], tura_czarny)
        else:
            self.plansza.zmien_pole(x, y, Tile.BLACK if tura_czarny else Tile.WHITE)
            
            self.plansza.debug_printuj_plansze(self.plansza.plansza)
            
        self.graj(not tura_czarny)
    
    