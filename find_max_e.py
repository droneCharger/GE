def find_max_e(graph,s_00,s_dd,beta,passengers,M1):
    result = 0
    re_stop = 0
    for i in range(len(graph)):
        if graph[i,0] < M1 and i != s_00 and i != s_dd:
            if result < beta[i]/passengers[i]:
                result = beta[i]/passengers[i]
                re_stop = i
    return re_stop