import ge_alg.find_max_e
import ge_alg.comput_length
import ge_alg.compute_passengers
import ge_alg.find_min_deadline
import ge_alg.satisfy_capacity
def ge(graph,s_00,s_dd,beta,passengers,
       capacity,deadlines,speed, t1_max,t2_max,gamma,phi,M1):
    flag = True
    path = []
    while flag:
        max_stop = ge_alg.find_max_e.find_max_e(graph,s_00,s_dd,beta,passengers,M1)
        if max_stop == 0:
            flag = False
            break
        path.append(max_stop)
        path_capacity = ge_alg.compute_passengers.compute_passengers(path, passengers)
        path_temp = [s_00] + path + [s_dd]
        path_length = ge_alg.comput_length.comput_length(path_temp,graph)
        path_min_deadline = ge_alg.find_min_deadline.find_min_deadline(path, deadlines)
        path_length_constraint = (path_min_deadline -path_capacity*(t2_max+t1_max))* speed
        if path_length > path_length_constraint or path_capacity > capacity:
            flag = False
            path.pop()
            break
        else:
            graph[max_stop, 0] = M1
    if len(path) > 0:
        ge_beta = 0
        for ii in path:
            ge_beta = ge_beta + beta[ii]
        ge_path = [s_00] + path + [s_dd]
        ge_path_length = ge_alg.comput_length.comput_length(ge_path,graph)
        ge_path_welfare = ge_beta - ge_path_length * gamma * phi
    else:
        ge_path_welfare, ge_path = 0, []
    return ge_path_welfare,ge_path