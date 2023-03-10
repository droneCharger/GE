def belong(stop,winner_set):
    flag = 0
    for ii in winner_set:
        if stop in ii:
            flag = 1
            return flag
    return flag