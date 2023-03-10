def compute_number(passengers):
    number = 0
    for i in range(len(passengers)):
        number = number + passengers[i]
    return number