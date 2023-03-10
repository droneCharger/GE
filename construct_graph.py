import numpy as np
import dis_d

def construct_graph(graph_lat, graph_long, number_data):
    col = 0
    row = 0
    graph = np.zeros((number_data, number_data))
    for lat, long in zip(graph_lat, graph_long):
        row = 0
        for lat1, long1 in zip(graph_lat, graph_long):
            dis = dis_d.dis_d(lat, lat1, long, long1)
            graph[col, row] = dis
            row += 1
            if row >= number_data:
                break
        col += 1
        if col >= number_data:
            break
    return  graph