# Getting some elements out of an existing array and creating a new array is called filtering.
# A boolean index list is a list ofboolean corresponding to indexes in the array. (True and False)
# create an array from the element on index 0 to 2:
import numpy as np
x = np.array([41,42,43,44])
x1 = [True, False, True, False]
finalx = x[x1]
print(finalx)

# now we will create a filter array
# that will return only values higher than 42.
import numpy as np
x = np.array([41,42,43,44])
emptyx = []
for element in x:
    if element > 42:
        emptyx.append(True)
    else:
        emptyx.append(False)
xnew = x[emptyx]
print(emptyx)
print(xnew)

# Create a filter array that will return only even elements from the original array.
import numpy as np
x = np.array([1,2,3,4,5,6,7])
xempty = []
for i in x:
    if i%2 == 0:
        xempty.append(True)
    else:
        xempty.append(False)
xnew = x[xempty]
print(xempty)
print(xnew)

# Yes, you can also create filter directly from array
# that will return only values higher than 42.
import numpy as np
x = np.array([41,42,43,44])
xempty = x > 42
xnew = x[xempty]
print(xempty)
print(xnew)

# Yes, you can also create filter directly from array
# Create a filter array that will return only even elements from the original array.
import numpy as np
x = np.array([1,2,3,4,5,6,7])
xempty = x % 2 == 0
xnew = x[xempty]
print(xempty)
print(xnew)




# for create missing value use np.nan
import numpy as np
a = np.array([1, 2, 3, 4, np.nan, 6])
print(a)
b = np.isnan(a)
print(b)
# [False False False False  True False]
print(a[~np.isnan(a)])
