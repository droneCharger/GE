
def compute_passengers(path, passengers):
    number = 0
    for i in range(len(path)):
        number = number + passengers[path[i]]
    return number