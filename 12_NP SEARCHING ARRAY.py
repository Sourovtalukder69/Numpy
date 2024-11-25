# searching array - you can search an array for a certain value and return the indexes that get the match. by using where()
import numpy as np
sourov = np.array([1,2,3,4,5,4,4])
sourovnew = np.where(sourov == 4)
print(sourovnew)

# now we will find the indexes where the values are even:
import numpy as np
sourov = np.array([1,2,3,4,5,6,7,8])
sourov1 = np.where(sourov%2 == 0)
print(sourov1)

# now we will find the indexes where the values are odd:
import numpy as np
sourov = np.array([1,2,3,4,5,6,7,8])
sourov1 = np.where(sourov%2 == 1)
print(sourov1)

# Searchsorted() - perform binary search in array.
# we will now find the index where the value 7 should be insterted.
import numpy as np
sourov = np.array([6,7,8,9])
sourov1 = np.searchsorted(sourov, 7)
print(sourov1)

# now we will search fron right side
import numpy as np
sourov = np.array([6,7,8,9])
sourov1 = np.searchsorted(sourov, 7, side='right')
print(sourov1)

# how to search multiple values:
import numpy as np
sourov = np.array([1,3,5,7])
sourov1 = np.searchsorted(sourov, [2,4,6])
print(sourov1)

import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 8565, 5345, 3, 63, 4, 56, 32, 100])
# find all indices with value greater than 50 and replace
# np.where(condition, True, fasle)
b = np.where(a>50, 0, a)
print(b)

# find max item in array
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 8565, 5345, 3, 63, 4, 56, 32, 100])
b = np.argmax(a)
c = np.argmin(b)


# np.isin =  Search multiple items in one time
# we can see that one array having values are checked in a different numpy array having different elements with different sizes
import numpy as np
x = np.array([11, 53, 28, 50, 38, 37, 94,90, 92, 5, 30, 68, 9, 78, 2, 21])
item = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
search = np.isin(x, item)
print(search)
# [False False False  True False False False  True False False  True False      
#  False False False False]



# Unique() function use for search unique items
import numpy as np
e = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6])
u = np.unique(e)
print(u)
