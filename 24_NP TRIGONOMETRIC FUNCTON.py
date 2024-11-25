# Trigonometric function: numpy provides the ufuncs line sin(), cos() and tan() that takes values in radians and produce the corresponding sin, cos and tan values.
# here now we will find the sin value of pi/2
import numpy as np
sourov = np.sin(np.pi/2)
print(sourov)

# we will now find the sin values of an array
import numpy as np
sourov = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
sourovnew = np.sin(sourov)
print(sourovnew)

# Convert Degree into radians: by default all of the trigonometric functions tales radians as parameter.
# note: radians values are pi/180* degree value.
# here we will convert all the array values to radians:
import numpy as np
sourov = np.array([90, 180, 270,360])
sourovnew = np.deg2rad(sourov)
print(sourovnew)

# here we will convert radians into degree.
import numpy as np
sourov = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
sourovnew = np.rad2deg(sourov)
print(sourovnew)

# here we can also find angles : arcsin(), arccos() and arctan() that takes values in radians and produce the corresponding sin, cos and tan values.

# we will now find the angle of 1.0
import numpy as np
sourov = np.arcsin(1.0)
print(sourov)

# angles of each values in an array:
import numpy as np
sourov = np.array([1, -1, 0.1])
sourovnew = np.arcsin(sourov)
print(sourovnew)

# here we can also find the hypotenous using the pythagoras theorem in numpy
# hypot() function that takes values in radians and produce the corresponding sin, cos and tan values.

# here we will find the hypot for 3 base and 4 perpendicular.
import numpy as np
base = 3
perp = 4
sourov = np.hypot(base, perp)
print(sourov)

