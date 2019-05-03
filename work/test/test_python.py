import numpy as np
import scipy.integrate as itg
import matplotlib.pyplot as plt
import pandas as pd

VMIN = -2.0
VMAX =  2.0

def func1(x):
    return x ** 2

def func2(x0, x1):
    return itg.quad(func1, x0, x1)[0]

x = pd.Series([i for i in np.arange(VMIN, VMAX, 0.01)])
y = x.map(func1)
y_sum = pd.Series([func2(VMIN, i) for i in x])


table = pd.DataFrame({'y':y, 'y_sum':y_sum})
table.index = x

print(table)

table.plot(title='Plot Example')
plt.show()
