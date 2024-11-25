# finding LCM(Lowest Common Multiple)
# here we will find the LCM of the 2 numbers:

import numpy as np
x1 = 4
x2 = 6
xnew = np.lcm(x1, x2)
print(xnew)
# the answers of the above is 12 because the LCM of both numbers (4*3=12 and 6*2=12) 

# finding the LCM in array: to findout lcm in array have to use np.lcm.reduce()

import numpy as np
x = np.array([3,6,9])
xnew = np.lcm.reduce(x) # the reduce() method will use the ufunc, in this case the lcm() function on each elemtn and it will reduce the array by 1 dimension.
print(xnew)


# here we will find the LCM of all of an array where the array contains all integers from 1 to 10.
import numpy as np
x = np.arange(1,11)
xnew = np.lcm.reduce(x)
print(xnew)