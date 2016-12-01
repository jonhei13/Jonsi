from itertools import *

def rank_hand(s):
    S = '23456789TJQKA'
    P = []
    for i in S:
        P.append((i,i))
    T = []
    for i in S:
        T.append((i,i,i))
    C = '2 2 2 2 3 3 3 3 4 4 4 4 5 5 5 5 6 6 6 6 7 7 7 7 8 8 8 8 9 9 9 9 T T T T J J J J Q Q Q Q K K K K A A A A'
    Ca = C.split(" ")
    S = 'H S D C'
    D = ['2C','2D','2H','2S','3C','3D','3H','3S','4C','4D','4H','4S','5C','5D','5H','5S','6C','6D','6H','6S','7C','7D','7H','7S','8C','8D','8H','8S','9C','9D','9H','9S','TC','TD','TH','TS','JC','JD','JH','JS','QC','QD','QH','QS','KC','KD','KH','KS','AC','AD','AH','AS']
    newS = sorted(s)


    def Straight(newS):
        new = []

    def Three(newS):
        new = []
        for x in newS:
            new.append(x[0])
        Mas = list(tuple(permutations(new, 3)))
        Mas = list(set(Mas))
        loc3 = [(x,y) for x in T for y in Mas if x == y]
        if len(loc3) == 1:
            return 3
        return 0

    def Two_Pair(newS):
        new = []
        for x in newS:
            new.append(x[0])
        Mas = list(tuple(permutations(new, 2)))
        Mas = list(set(Mas))
        loc3 = [(x,y) for x in P for y in Mas if x == y]
        if len(loc3) == 2:
            return 2
        return 0

    def One_Pair(newS):
        Ma = list(set(permutations(newS, 2)))
        Ma.sort()
        Mas = list(set(permutations(D, 2)))
        Mas.sort()
        loc3 = list(set(Ma) & set(Mas))
        for x in loc3:
            if x[0][0] == x[1][0]:
                return 1
        return 0


    Li = Three(newS)
    return Li


print(rank_hand([ '4D', 'QH', '4C', 'QS', 'QH' ]))