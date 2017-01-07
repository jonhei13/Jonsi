
def process_ls(s):
    res = list(s.split("\n"))
    NewList = []
    Result = []
    da = ''
    for i in range(len(res)):
        NewList.append(res[i].split(" "))
    for x in range(len(NewList)):
        NewList[x] = list(filter(None,NewList[x]))
    Want = sorted(NewList, key=lambda x:int(x[4]), reverse = True)
    Banned = []
    for i in Want:
        if i[0][:1] == 'd':
            Banned.append(i)
    for i in Banned:
        Want = [val for val in Want if val != i]
    for i in Want:
        if len(i) > 9:
            x = 8
            while x < len(i):
                da += i[x] + ' '
                x += 1
                i[8] = da
                if x == len(i):
                    da = da[:-1]
                    i[8] = da
        Result.append(i[8])
        da = ''
    return Result