# arithemtic operators: +, -, / , *
# by using ufunc additional arguments like, where, dtype and out.
# here now we will use add()
import numpy as np
souorv1 = np.array([10,11,12,13,14,15])
souorv2 = np.array([20,21,22,23,24,25])
souorvnew = np.add(souorv1, souorv2)
print(souorvnew)

#  example of substracting the value
import numpy as np
souorv1 = np.array([10,11,12,13,14,15])
souorv2 = np.array([20,21,22,23,24,25])
souorvnew = np.subtract(souorv1, souorv2)
print(souorvnew)

# example of multipication
import numpy as np
souorv1 = np.array([10,11,12,13,14,15])
souorv2 = np.array([20,21,22,23,24,25])
souorvnew = np.multiply(souorv1, souorv2)
print(souorvnew)

# example of divide()
import numpy as np
souorv1 = np.array([10,11,12,13,14,15])
souorv2 = np.array([20,21,22,23,24,25])
souorvnew = np.divide(souorv1, souorv2)
print(souorvnew)

# power() function raises the value from the 1st array to the power of the values of the 2nd array and return the results in a new array.

import numpy as np
souorv1 = np.array([10,20,30,40,50,60])
souorv2 = np.array([3,5,6,8,2,33])
souorvnew = np.power(souorv1, souorv2)
print(souorvnew)

# reminder- mod() and reminder() fucntions return the reminder of the 1st array corrosponding to the 2nd array, and result in the new array.
import numpy as np
souorv1 = np.array([10,20,30,40,50,60])
souorv2 = np.array([3,7,9,8,2,33])
souorvnew = np.mod(souorv1, souorv2)
print(souorvnew)

# by using reminder()
import numpy as np
souorv1 = np.array([10,20,30,40,50,60])
souorv2 = np.array([3,7,9,8,2,33])
souorvnew = np.remainder(souorv1, souorv2)
print(souorvnew)

# quotient and mod(reminder)
# the divmod() function return both the quotient and mod.
import numpy as np
souorv1 = np.array([10,20,30,40,50,60])
souorv2 = np.array([3,7,9,8,2,33])
souorvnew = np.divmod(souorv1, souorv2)
print(souorvnew)

# absolute() and abs()- do the same operation but here we should use absolute() to avoid confusion with python inbuilt function math.abs().
import numpy as np
souorv = np.array([-1,-2,-3,-4,-5])
souorvnew = np.absolute(souorv)
print(souorvnew) 
