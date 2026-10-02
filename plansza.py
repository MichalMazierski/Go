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
        
        self.plansza = [ ### DO USUNIĘCIA PÓŹNIEJ!!!!!! (tylko na potrzeby testU oWo )
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
        print(
            "Legenda: "
            "\033[48;5;0mPusty\033[0m",
            "\033[48;5;27mCzarny\033[0m",    ### Zrobione na szybko ale potrzebne aby łatwiej odnajdywać się w planszy (:
            "\033[48;5;28mBiały\033[0m",
            "\033[48;5;52mCzarnyPunkt\033[0m",
            "\033[48;5;52mBiałyPunkt\033[0m",
            "\033[48;5;58mRamka\033[0m",
            "\033[48;5;52mTempJeden\033[0m",
            "\033[48;5;55mTempZero\033[0m"
        )
        for rzad in plansza:

            for pole in rzad:

                print(slownik[pole.value], end="")

            print()
    

    def zmien_pole(self, x, y, pole: Tile):

        self.plansza[y][x] = pole
        

    def sprawdz_punkt(self, x: int, y: int, odw: list[tuple[int, int]], czy_czarne: bool):

        w = self.__policz_punkt(copy.deepcopy(self.plansza), odw, x, y, czy_czarne)
        
        punkty = 0
        
        print("Punkty: " + str(punkty))

        nowa_plansza = [[Tile.EMPTY for j in range(len(self.plansza))] for i in range(len(self.plansza))]
        
        final_punkt = Tile.BLACK_POINT if czy_czarne else Tile.WHITE_POINT
        
        for i in range(len(nowa_plansza)):
            for j in range(len(nowa_plansza[i])):
                if w[i][j] == Tile.TEMP_ONE:
                    nowa_plansza[i][j] = final_punkt
                    punkty += 1
                else:
                    nowa_plansza[i][j] = self.plansza[i][j]

        self.plansza = nowa_plansza

    def __policz_punkt(
        self,
        plansza: list[list[Tile]],
        odwiedzone: list[tuple[int, int]],
        x: int,
        y: int,
        czy_czarne: bool
    ) -> list[list[Tile]]:

        tile = Tile.BLACK if czy_czarne else Tile.WHITE

        empty = [
            Tile.TEMP_ZERO
        ]

        accepted = [
            Tile.BORDER,
            Tile.BLACK_POINT if czy_czarne else Tile.WHITE_POINT,
            tile,
            Tile.TEMP_ONE
        ]

        unaccepted = [
            Tile.WHITE if czy_czarne else Tile.BLACK,
            Tile.WHITE_POINT if czy_czarne else Tile.BLACK_POINT
        ]

        temp_plansza = copy.deepcopy(plansza)

        odwiedzone = set(odwiedzone)

        def sprawdz(x: int, y: int) -> None:
            
            if (x, y) in odwiedzone:
                return

            odwiedzone.add((x, y))

            ok_combo = 0

            for offset_x, offset_y in (
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ):
                nx = x + offset_x
                ny = y + offset_y

                if temp_plansza[ny][nx] in accepted:
                    ok_combo += 1

            if (
                any(
                    temp_plansza[y + offset_y][x + offset_x] in unaccepted
                    for offset_x, offset_y in (
                        (-1, 0),
                        (1, 0),
                        (0, -1),
                        (0, 1)
                    )
                )
                or
                sum(
                    temp_plansza[y + offset_y][x + offset_x] in empty
                    for offset_x, offset_y in (
                        (-1, 0),
                        (1, 0),
                        (0, -1),
                        (0, 1)
                    )
                ) >= 1
            ):
                ok_combo = 0

            if ok_combo >= 2:
                temp_plansza[y][x] = Tile.TEMP_ONE
            else:
                temp_plansza[y][x] = Tile.TEMP_ZERO
                
            for offset_x, offset_y in (
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ):
                nx = x + offset_x
                ny = y + offset_y

                if (
                    (nx, ny) not in odwiedzone
                    and temp_plansza[ny][nx] == Tile.EMPTY
                ):
                    sprawdz(nx, ny)
        

        sprawdz(x, y)

        return temp_plansza
