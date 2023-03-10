
import numpy as np

def ini_paras(number_data):

    mu, sigma = 15, 5
    passengers = np.random.normal(mu, sigma, number_data)
    passengers = np.trunc(passengers)
    passengers = passengers.astype(int)
    deadlines = [0] * number_data
    for i in range(number_data):
        mu, sigma = 5, 1.67
        deadl = np.random.normal(mu, sigma, number_data)
        deadl = np.trunc(deadl)
        deadlines[i] = min(deadl)

    beta = [0] * number_data
    for i in range(len(passengers)):
        beta_temp = np.random.randint(3, 8, passengers[i])
        beta_sum = 0
        for j in range(passengers[i]):
            beta_sum = beta_sum + beta_temp[j]
        beta[i] = beta_sum.astype(int)

    return passengers, beta, deadlines