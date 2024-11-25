# difference between numpy array copy and view.
# we will make a copy, change in original array, and display both.

import numpy as np
x = np.array([1,2,3,4,5])
y = x.copy()
y[0] = 5
print(x)
print(y)

# now we will make a view, change original, display both

import numpy as np
x = np.array([1,2,3,4])
y = x.view()
x[0] = 31
print(x)
print(y)
