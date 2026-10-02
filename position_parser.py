from enums import *

#B[fi];W[fj];B[gi];W[gj];B[hi];W[hj];B[ii];W[ij];B[ji];W[jj];B[kh];W[kj];B[lh];W[lj];B[lg];W[mh];B[lf];W[mf];B[le];W[me];B[ld];W[md];B[kc];W[lc];B[jc];W[mc];B[ic];W[jb];B[hc];W[hb];B[gc];W[fb];B[fc];W[ed];B[fd];W[ee];B[fe];W[de];B[ff];W[ef];B[eg];W[dh];B[eh];W[hg];B[];W[])

def parse_position_from_sgf(rozmiar: int, sgf: str):
    pozycje = sgf.split(";")
    plansza = [[Tile.BORDER for _ in range(rozmiar + 2)] if i == 0 or i == rozmiar + 1 else [Tile.BORDER if k == 0 or k == rozmiar + 1 else Tile.EMPTY for k in range(rozmiar + 2)] for i in range(rozmiar + 2)]
    
    translator = dict()
    
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in range(rozmiar):
        translator[alfabet[i]] = i
        
    print(translator)
    
    for i in pozycje:
        tile = Tile.BLACK if i[0] == "B" else Tile.WHITE
        
        kolumna = translator[i[2]]
        rzad = translator[i[3]]
        
        plansza[rzad][kolumna] = tile
    
    return plansza