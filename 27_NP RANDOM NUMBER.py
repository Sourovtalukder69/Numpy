# Random meaning - something that cannot be predicted logically.
# Now we will generate a random number from 0 to 100
from numpy import random 
rndm = random.randint(100)
print(rndm) 

# You can also genetrate float() via rand() from 0 to 1
from numpy import random 
rndm = random.rand()
print(rndm) 

# You can also generate random Array.
# we will generate a 1-D array containing 5 random int from 0 to 100:
from numpy import random 
rndm = random.randint(100, size=(5))
print(rndm) 

# You can also generate random Array.
# we will generate a 2-D array with 3 rows, each row  containing 5 random int from 0 to 100:
from numpy import random 
rndm = random.randint(100, size=(3, 5))
print(rndm) 

# You can also generate random Array.
# we will generate a 1-D array containing 5 random float:
from numpy import random 
rndm = random.rand(5)
print(rndm) 

# You can also generate random Array.
# we will generate a 2-D array with 3 rows, each containing 5 random float:
from numpy import random 
rndm = random.rand(3, 5)
print(rndm) 

# you can also generate random numbers from an array
# choice()

from numpy import random 
rndm = random.choice([3,5,7,9,1,4,6])
print(rndm) 

# you can also generate random numbers from an 2-D array
# choice()

from numpy import random 
rndm = random.choice([3,5,7,9,1,4,6], size=(3, 5))
print(rndm) 


# random array
import numpy as np
x = np.linspace(1, 10, 20).reshape(5,4)
print(x)