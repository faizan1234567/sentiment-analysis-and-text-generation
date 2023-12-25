import numpy as np 
import os


# to minimize!

def regularization_term(true, prediction):
    order = list(range(1,4))
    order.append(0)
    
    deviation = (true*true[:,order]) - (prediction*prediction[:,order])
    deviation = abs(deviation)**2
    return 0.2 * deviation

true = np.array([1, 0, 1, 0, 1])
pred = np.array([0, 1, 1, 0, 1])
print(regularization_term(true, pred))