from enums import *
import copy
import position_parser


class Plansza:

    def __init__(self, rozmiar: int, sgf: str = ""):

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
        
        if sgf != "":
            self.plansza = position_parser.parse_position_from_sgf(rozmiar, sgf)

    def debug_printuj_plansze(self, plansza): ## Nie do używania !!!
        
        slownik = {
                Tile.EMPTY.value: "\033[48;5;0m*\033[0m",
                Tile.BLACK.value: "\033[48;5;27m*\033[0m",
                Tile.WHITE.value: "\033[48;5;28m*\033[0m",
                Tile.BLACK_POINT.value: "\033[48;5;52m*\033[0m",
                Tile.WHITE_POINT.value: "\033[48;5;52m*\033[0m",
                Tile.BORDER.value: "\033[48;5;58m*\033[0m",
                Tile.TEMP_ONE.value: "\033[48;5;222m*\033[0m",
                Tile.TEMP_ZERO.value: "\033[48;5;55m*\033[0m",
                }
        print(
            "Legenda: "
            "\033[48;5;0mPusty\033[0m",
            "\033[48;5;27mCzarny\033[0m",    ### Zrobione na szybko ale potrzebne aby łatwiej odnajdywać się w planszy (:
            "\033[48;5;28mBiały\033[0m",
            "\033[48;5;52mCzarnyPunkt\033[0m",
            "\033[48;5;60mBiałyPunkt\033[0m",
            "\033[48;5;58mRamka\033[0m",
            "\033[48;5;222mTempJeden\033[0m",
            "\033[48;5;55mTempZero\033[0m"
        )
        for rzad in plansza:

            for pole in rzad:

                print(slownik[pole.value], end="")

            print()
    

    def zmien_pole(self, x, y, pole: Tile):

        self.plansza[y][x] = pole
        

    def sprawdz(self, czy_czarne: bool):
        
        odw = []
        
        w = copy.deepcopy(self.plansza)
        
        for rzad in range(len(self.plansza)):
            for kolumna in range(len(self.plansza[rzad])):
                if (rzad,kolumna) == (6,3):
                    pass
                if w[rzad][kolumna] == Tile.EMPTY:
                    w = self.polacz_plansze(w, self.__policz_punkt(w, odw, kolumna, rzad, czy_czarne), czy_czarne)
                    self.debug_printuj_plansze(w)
        
        self.plansza = copy.deepcopy(w)
        
        self.debug_printuj_plansze(self.plansza)

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
            Tile.WHITE_POINT if czy_czarne else Tile.BLACK_POINT,
            Tile.BORDER
        ]

        temp_plansza = copy.deepcopy(plansza)

        def sprawdz_rekursywny(x: int, y: int) -> None:
            
            if (x, y) in odwiedzone:
                return

            odwiedzone.append((x, y))

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
                # any(
                #     temp_plansza[y + offset_y][x + offset_x] in unaccepted
                #     for offset_x, offset_y in (
                #         (-1, 0),
                #         (1, 0),
                #         (0, -1),
                #         (0, 1)
                #     )
                # )
                # or
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

            if ok_combo >= 2 and temp_plansza[y][x] not in unaccepted:
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
                    sprawdz_rekursywny(nx, ny)
        
        def rozsiej_zero(x: int, y: int) -> None:
            if (x, y) in odwiedzone:
                return

            odwiedzone.append((x, y))
            
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
                    and temp_plansza[ny][nx] not in [Tile.BORDER, Tile.BLACK, Tile.WHITE, Tile.BLACK_POINT, Tile.WHITE_POINT]
                ):
                    rozsiej_zero(nx, ny)
        

        sprawdz_rekursywny(x, y)
        
        for odw in odwiedzone[::-1]:
            if temp_plansza[odw[1]][odw[0]] == Tile.TEMP_ZERO: 
                odwiedzone = []
                rozsiej_zero(*odw)
                break

        return temp_plansza

    def polacz_plansze(self, stara_plansza: list[list[Tile]], w: list[list[Tile]], czy_czarne: bool):
        nowa_plansza = [[Tile.EMPTY for j in range(len(self.plansza))] for i in range(len(self.plansza))]
                
        final_punkt = Tile.BLACK_POINT if czy_czarne else Tile.WHITE_POINT
        
        for i in range(len(nowa_plansza)):
            for j in range(len(nowa_plansza[i])):
                if w[i][j] == Tile.TEMP_ONE:
                    nowa_plansza[i][j] = final_punkt
                else:
                    nowa_plansza[i][j] = stara_plansza[i][j]
        
        return nowa_plansza
