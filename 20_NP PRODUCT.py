# products: use prod() function.
# here we will find the product of the element of the below array:
import numpy as np
sourov = np.array([1,2,3,4]) # 1*2*3*4 = 24
sourovnew = np.prod(sourov)
print(sourovnew)

# here we will find the product of elemets in 2 different array:
import numpy as np
sourov1 = np.array([1,2,3,4])
sourov2 = np.array([5,6,7,8])
sourovnew = np.prod([sourov1, sourov2]) # 1*2*3*4*5*6*7*8 = 40320
print(sourovnew)

# product over an axis
import numpy as np
sourov1 = np.array([1,2,3,4])
sourov2 = np.array([5,6,7,8])
sourovnew = np.prod([sourov1, sourov2], axis=1) 
print(sourovnew)

# cummulative product:
# example  the partial product of [1,2,3,4] is [1,1*2,1*2*3,1*2*3*4] = [1,2,6,24] represented by cumprod().
import numpy as np
sourov = np.array([5,6,7,8])
sourovnew = np.cumprod(sourov)
print(sourovnew)