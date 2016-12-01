from itertools import *

def rank_hand(s):
    C = '2 2 2 2 3 3 3 3 4 4 4 4 5 5 5 5 6 6 6 6 7 7 7 7 8 8 8 8 9 9 9 9 T T T T J J J J Q Q Q Q K K K K A A A A'
    Ca = C.split(" ")
    S = 'H S D C'
    D = ['2C','2D','2H','2S','3C','3D','3H','3S','4C','4D','4H','4S','5C','5D','5H','5S','6C','6D','6H','6S','7C','7D','7H','7S','8C','8D','8H','8S','9C','9D','9H','9S','TC','TD','TH','TS','JC','JD','JH','JS','QC','QD','QH','QS','KC','KD','KH','KS','AC','AD','AH','AS']
    newS = sorted(s)


    def Two_Pair(newS):
        new = []
        for x in newS:
            new.append(x[0])
        Ma = list(set(permutations(new, 4)))
        Mas = list(set(permutations(Ca, 4)))
        loc3 = [(x,y) for x in Mas for y in Ma if x == y]
        for x in Ma:
            for i in loc3:
                if x == i[0]:
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


    Li = Two_Pair(newS)
    return Li


print(rank_hand([ '8D', '2H', '4C', '2S', 'QH' ]))