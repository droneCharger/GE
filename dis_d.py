from math import radians, cos, sin, asin, sqrt

def dis_d(LaA, LaB, LoA, LoB):
    LoA = radians(float(LoA))
    LoB = radians(float(LoB))
    LaA = radians(float(LaA))
    LaB = radians(float(LaB))
    D_la = LaB - LaA
    D_lo = LoB - LoA
    P= sin(D_la / 2) ** 2 + cos(LaA) * cos(LaB) * sin(D_lo / 2) ** 2
    Q = 2 * asin(sqrt(P))
    R_km = 6371
    return Q * R_km