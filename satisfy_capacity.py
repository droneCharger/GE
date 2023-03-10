import sbpm.compute_passengers
import sbpm.find_min_passenger

def satisfy_capacity(path_cap, capacity,passengers):

    number_passengers = sbpm.compute_passengers.compute_passengers(path_cap,passengers)
    if number_passengers <= capacity:
        return path_cap
    while number_passengers > capacity:
        min_pas_index = sbpm.find_min_passenger.find_min_passenger(path_cap,passengers)

        path_cap.pop(min_pas_index)
        number_passengers = sbpm.compute_passengers.compute_passengers(path_cap, passengers)
    return path_cap