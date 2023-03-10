
def find_min_deadline(path, deadlines):
    min_deadline = 10000
    for i in path:
        if min_deadline > deadlines[i]:
            min_deadline = deadlines[i]
    return min_deadline