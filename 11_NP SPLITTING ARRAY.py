# spliting arrays in numpy- it is reverse to joining, breaking the array.
# array_split()

# split the array in 3 parts:
import numpy as np
sourov = np.array([1,2,3,4,5,6])
sourovnew = np.array_split(sourov, 3)
print(sourovnew)

# now we will split this array in 4 parts
import numpy as np
sourov = np.array([1,2,3,4,5,6])
sourovnew = np.array_split(sourov, 4)
print(sourovnew)

# split into array with index

import numpy as np
sourov = np.array([1,2,3,4,5,6])
sourovnew = np.array_split(sourov, 3)
print(sourovnew[0])
print(sourovnew[1])
print(sourovnew[2])


# splitting the 2-D array
import numpy as np
sourov = np.array([[1,2], [3,4], [5,6], [7,8], [9,10], [11,12]])
sourovnew = np.array_split(sourov, 3)
print(sourovnew)

# split the 2-D array into three 2-D arrays
import numpy as np
sourov = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
sourovnew = np.array_split(sourov, 3)
print(sourovnew)

# spliting the 2-D into three 2-Dalong with rows
import numpy as np
sourov = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
sourovnew = np.array_split(sourov, 3, axis=1)
print(sourovnew)

#alternate solution is using the hsplit(), opposite hstack()
import numpy as np
sourov = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
sourovnew = np.hsplit(sourov, 3)
print(sourovnew)