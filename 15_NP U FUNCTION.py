# ufunc - stands for universal function and they are acually numpy functions that operates on the ndarray objects.
# ufunc also takes additional arguments like, where, dtype and out.
# vectorization - converting the iterative statements into a vector based statement.

# example without ufunc, here we will use python in built zip().
x = [1,2,3,4]
y = [4,5,6,7]
z= []
for i, j in zip(x,y):
    z.append(i+j)
print(z)

# with ufunc, we will now use add() function
import numpy as np
x = [1,2,3,4]
y = [4,5,6,7]
z = np.add(x,y)
print(z)




# to create your own ufunc, you have to define a function, like you do in normal function in python, then you add it to the numpy function with frompyfunc() method.
# arguments of frompyfunc(): function, inputs, outputs

# Create your own ufunc for addition:
import numpy as np
def myadd(x,y):
    return x+y

myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1,2,3,4], [5,6,7,8]))

# checking if this function in ufunc or not:
import numpy as np
print(type(np.add))

# concatenate()
import numpy as np
print(type(np.concatenate))

# what if ufunc does not exist: (please comment it while running the codes) 
import numpy as np
print(type(np.sjafdfdf))

# use an if statement to check if the functionis  a ufunc or not.
import numpy as np
if type(np.add) == np.ufunc:
    print('yes, this function is ufunc')
else:
    print('this function is not aan ufunc')




# Sigmoid() function : in this function every results belongs (0 -1)
#                   1
# sigmoid S(x) = ---------
#                1 + e-x
import numpy as np

a = np.arange(10)
def sigmoid(array):
    return np.exp(array)/(1+ np.exp(array))

b = sigmoid(a)
print(b)



# mean square error  (los function) mean((actual - predicted)**2)
import numpy as np

actual = np.random.randint(1, 50, 25)
print(actual)
predicted = np.random.randint(1, 50, 25)
print(predicted)


def mse(actual, predicted):
    np.mean((actual - predicted)**2)

d = mse(actual, predicted)

# binary cross entropy  create now




