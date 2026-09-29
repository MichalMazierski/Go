from enums import *
import copy


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
        
        self.plansza = [
            [Tile.BORDER, Tile.BORDER, Tile.BORDER, Tile.BORDER, Tile.BORDER, Tile.BORDER, Tile.BORDER,Tile.BORDER,Tile.BORDER],
            [Tile.BORDER, Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.BORDER],
            [Tile.BORDER, Tile.BLACK,  Tile.BLACK,  Tile.BLACK,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.BORDER],
            [Tile.BORDER, Tile.BLACK, Tile.EMPTY,  Tile.EMPTY,  Tile.BLACK,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,   Tile.BORDER],
            [Tile.BORDER, Tile.BLACK, Tile.EMPTY,  Tile.EMPTY,  Tile.BLACK,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,   Tile.BORDER],
            [Tile.BORDER, Tile.BLACK, Tile.EMPTY,  Tile.EMPTY,  Tile.BLACK,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,   Tile.BORDER],
            [Tile.BORDER, Tile.BLACK, Tile.EMPTY,  Tile.EMPTY,  Tile.BLACK,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,   Tile.BORDER],
            [Tile.BORDER, Tile.BLACK,  Tile.BLACK,  Tile.BLACK,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.BORDER],
            [Tile.BORDER, Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.BORDER],
            [Tile.BORDER, Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.BORDER],
            [Tile.BORDER, Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.BORDER],
            [Tile.BORDER, Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.BORDER],
            [Tile.BORDER, Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.EMPTY,  Tile.BORDER],
            [Tile.BORDER, Tile.BORDER, Tile.BORDER, Tile.BORDER, Tile.BORDER, Tile.BORDER, Tile.BORDER,Tile.BORDER,Tile.BORDER]
        ]
        
        
        

    def debug_printuj_plansze(self, plansza): ## Nie do używania !!!
        
        slownik = {
                Tile.EMPTY.value: "\033[48;5;0m*\033[0m",
                Tile.BLACK.value: "\033[48;5;27m*\033[0m",
                Tile.WHITE.value: "\033[48;5;28m*\033[0m",
                Tile.BLACK_POINT.value: "\033[48;5;52m*\033[0m",
                Tile.WHITE_POINT.value: "\033[48;5;52m*\033[0m",
                Tile.BORDER.value: "\033[48;5;58m*\033[0m",
                Tile.TEMP_ONE.value: "\033[48;5;52m*\033[0m",
                Tile.TEMP_ZERO.value: "\033[48;5;55m*\033[0m",
                }
        
        
        for rzad in plansza:

            for pole in rzad:

                print(slownik[pole.value], end="")

            print()
    

    def zmien_pole(self, x, y, pole: Tile):

        self.plansza[y][x] = pole
        

    def sprawdz_punkt(self, x: int, y: int, czy_czarne: bool):

        w = self.__policz_punkt(self.plansza, x, y, czy_czarne)
        
        punkty = 0

        for rzad in w:
            for pole in rzad:
                if pole == Tile.TEMP_ONE:
                    punkty += 1
        
        print("Punkty: " + punkty)
        
        self.debug_printuj_plansze(w)
    

    def __check_for_ok_combo(self, temp_plansza: list[list[Tile]], x: int, y: int, czy_czarne: bool):
        ok_combo = 0
        
        accepted = [
        
                    Tile.BORDER,
        
                    Tile.BLACK_POINT if czy_czarne else Tile.WHITE_POINT,
        
                    Tile.BLACK if czy_czarne else Tile.WHITE
        
                    ]
                
        for offset_x, offset_y in ((-1, 0), (1, 0), (0, -1), (0, 1)):

            if temp_plansza[y + offset_y][x + offset_x] in accepted:

                ok_combo += 1
            
        return ok_combo

    def __policz_punkt(self, plansza: list[list[Tile]], x: int, y: int, czy_czarne: bool) -> list[list[Tile]]:
        
        tile = Tile.BLACK if czy_czarne else Tile.WHITE

        empty = [Tile.TEMP_ZERO, Tile.EMPTY]
        

        accepted = [

            Tile.BORDER,

            Tile.BLACK_POINT if czy_czarne else Tile.WHITE_POINT,

            Tile.BLACK if czy_czarne else Tile.WHITE

            ]
        

        unaccepted = [

            Tile.WHITE if czy_czarne else Tile.BLACK,

            Tile.WHITE_POINT if czy_czarne else Tile.WHITE_POINT

        ]
        

        temp_plansza = copy.deepcopy(plansza)
        
        self.debug_printuj_plansze(temp_plansza)
        
        #input()

        if self.__check_for_ok_combo(temp_plansza, x, y, czy_czarne) >= 2:
            temp_plansza[y][x] = Tile.TEMP_ONE

        else:

            temp_plansza[y][x] = Tile.TEMP_ZERO


        for offset_x, offset_y in ((-1, 0), (1, 0), (0, -1), (0, 1)):

            if temp_plansza[y + offset_y][x + offset_x] == Tile.EMPTY:

                temp_plansza = self.__policz_punkt(temp_plansza, y + offset_y, x + offset_x, czy_czarne)
        

        for offset_x, offset_y in ((-1, 0), (1, 0), (0, -1), (0, 1)):

            if temp_plansza[y + offset_y][x + offset_x] in empty or temp_plansza[y + offset_y][x + offset_x] in unaccepted:

                temp_plansza[y + offset_y][x + offset_x] = Tile.TEMP_ZERO
        
        if self.__check_for_ok_combo(temp_plansza, x, y, czy_czarne) >= 2:
            temp_plansza[y][x] = Tile.TEMP_ONE

        return temp_plansza