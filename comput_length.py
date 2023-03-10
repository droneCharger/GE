
def comput_length(path, graph):
    i = 0
    length = 0
    while i < len(path)-1:
        length += graph[path[i], path[i+1]]
        i += 1
    return length