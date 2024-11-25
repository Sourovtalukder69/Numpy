# sort() - the numpy ndarray object has a function which is called sort(), and this will sort a specified array.
import numpy as np
sharad = np.array([3,2,0,1])
print(np.sort(sharad)) # this method is like the copy()

# sort the array alphabetically
import numpy as np
sharad = np.array(['banana', 'cherry', 'apple'])
print(np.sort(sharad))

# sort the boolean array:
import numpy as np
sharad = np.array([True, False, True])
print(np.sort(sharad))

# sorting the 2-D array
import numpy as np
sharad = np.array([[3,2,4], [5,0,1]])
print(np.sort(sharad))


# Numpy tricks

import numpy as np
a = np.random.randint(1, 100, 15)
# Ascending order sorting
s1 = np.sort(a)
print(s1)

# decending order sorting
s11 = np.sort(a)[::-1]
print(s11)

b = np.random.randint(1, 100, 24).reshape(6, 4)
# row wise sort
s2 = np.sort(b)  
print(s2)

# column wise sort
s3 = np.sort(b, axis=0)
print(s3)



# np.flip()  : this function reverses the order of array elements along the specified axis. preserving the shape of the array
import numpy as np
x = np.array([11, 53, 28, 50, 38, 37, 94,90, 92, 5, 30, 68, 9, 78, 2, 21])
y = np.flip(x)  # 2D -  axis=0(for column); axis=1(for row)
print(y)

