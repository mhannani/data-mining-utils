# Distance between binary images
import numpy as np
from distance.euclidean import euclidean
from distance.minkowski import minkowski
from distance.manhattan import manhattan


print('----------- TP1 --------------')
print('Calculating the distance between images')

A1 = np.array([[1, 4, 3, 4, 5], [1, 5, 3, 4, 5]])
A2 = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])

# print(euclidean(A1, A2))
# print(minkowski(A1, A2, 5))
print(manhattan(A1, A2))

# ==> Binary images
# Image data are stored as an m-by-n logical matrix
# in which values of 0 and 1(or nonzero values) are interpreted as black and white

# ==> Grayscale Images
# A grayscale image is a data matrix whose
# values represent intensities of one image pixel

# ==> Truecolor Images
# A truecolor image is an image in which each
# pixel has a color specified by three values.
