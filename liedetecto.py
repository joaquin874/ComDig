import numpy as np
import scipy.integrate

alpha = 1
beta = 20
pLie = 0.7
pTruth = 0.3

np.random.seed(1234)

# Hypothesis source: TRUE (1) FALSE (0)

def filterObservation(observations, hypothesis):
    truths = []
    lies = []

    for i in range(len(observations)):
        if hypothesis[i]:
            truths.append(observations[i])
        else:
            lies.append(observations[i])

    return [lies, truths]

[lieObservations, truthObservations] = filterObservation(ob)