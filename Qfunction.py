from scipy import special
import numpy as np

x = 0.002
media = 1
var2 = 0.5
var = np.sqrt(var2)

# P(Z>=X) = Q()

def qfunc(x):
    return 0.5 - 0.5*special.erf(x/np.sqrt(2))

prob = qfunc((x-media)/var)

print(prob)