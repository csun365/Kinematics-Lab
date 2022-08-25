import scipy
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def func(x, a, b):
    return a * (1 - np.exp(-b * x))

popt, pcov = curve_fit(func, X, Y)
print(popt)
