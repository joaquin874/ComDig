from scipy import special
import numpy as np
from scipy.stats import norm as nm

x = 0.002
media = 1
var2 = 0.5
var = np.sqrt(var2)

# P(Z>=X) = Q(x)

def qfunc(x):
    return 0.5 - 0.5*special.erf(x/np.sqrt(2))

prob = qfunc((x-media)/var)
prob1 = nm.sf((x-media)/var)
print(prob, prob1)
# print(qfunc(np.sqrt(2*2.54)))
# x = 1

#print(nm.sf(np.sqrt(2*2.54)))
# print(q)