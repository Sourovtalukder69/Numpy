# Iterating Array - means going through the elements one by one or step by step. like For loop.

# Iterate the element of 1-D
import numpy as np
ITERATE = np.array([1,2,3])
for i in ITERATE:
    print(i)

# Iterate 2-D
import numpy as np
ITERATE = np.array([[1,2,3], [4,5,6]])
for i in ITERATE:
    print(i)

# Iterate on each scalar element of the 2-D
import numpy as np
ITERATE = np.array([[1,2,3], [4,5,6]])
for iter1 in ITERATE:
    for iter2 in iter1:
        print(iter2)

# Iterate 3-D
import numpy as np
ITERATE = np.array([[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]])
for iter1 in ITERATE:
    for iter2 in iter1:
        for iter3 in iter2:
            print(iter3)

# Iterating arrays using the nditer() function.
# Now we will Iterate on each scalar element.

import numpy as np
ITERATE = np.array([[[1,2], [3,4], [5,6], [7,8]]])
for i in np.nditer(ITERATE):
    print(i)

# Now we will Iterate with different step sizes.
import numpy as np
ITERATE = np.array([[1,2,3,4], [5,6,7,8]])
for i in np.nditer(ITERATE[:, ::2]):
    print(i)

# Another example
import numpy as np
ITERATe = np.array([[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]])
for i in np.nditer(ITERATe[:, :, ::3]):
    print(i)