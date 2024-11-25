# Append using 2d array
import numpy as np
b = np.random.randint(1, 100, 24).reshape(6, 4)
c = np.append(b, np.ones((b.shape[0], 1)), axis=1)
print(c)

# Joining the numpy array - here for this we will pass concatenate()
# concatenate perfect for 1-D array
import numpy as np
cnctnt = np.array([1,2,3])
cnctnt1 = np.array([4,5,6])
cnctnt2 = np.concatenate((cnctnt, cnctnt1))   # [1, 2, 3, 4, 5, 6]
print(cnctnt2)

# Joining of 2-D arrays along with rows(axis = 1). returs sequencly array
# similar to the hstack
import numpy as np
cnctnt = np.array([[1,2],[3,4]])
cnctnt1 = np.array([[5,6], [7,8]])
cnctnt2 = np.concatenate((cnctnt, cnctnt1), axis=1)  # [[1 2 5 6] 
print(cnctnt2)                                       #  [3 4 7 8]]

# concatenate row wise
import numpy as np
x= np.arange(6).reshape(2, 3)
y = np.arange(6, 12).reshape(2, 3)
z = np.concatenate((x, y), axis=0)


# concatenate along column
import numpy as np
x= np.arange(6).reshape(2, 3)
y = np.arange(6, 12).reshape(2, 3)
print(x)
print(y)
z = np.concatenate((x, y), axis=1)
print(z)


# Joining array using the stack function: 
import numpy as np
stk = np.array([1,2,3])
stk1 = np.array([4,5,6])
stk2 = np.stack((stk, stk1), axis=1)      # [[1 4]
#                                                  #  [2 5]
print(stk2)                                     #  [3 6]]

# Stacking along with rows: hstack()
import numpy as np
hstk = np.array([1,2,3])
hstk1 = np.array([4,5,6])
hstk2 = np.hstack((hstk, hstk1))          # [1 2 3 4 5 6]
print(hstk2)

# Stacking along with column
import numpy as np
vstk = np.array([1,2,3])
vstk1 = np.array([4,5,6])
vstk2 = np.vstack((vstk, vstk1))
print(vstk2)

# Stacking along with height(depth)
# import numpy as np
dstk = np.array([1,2,3])
dstk1 = np.array([4,5,6])
dstk2 = np.dstack((dstk, dstk1))
print(dstk2) 