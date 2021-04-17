# Distance between binary images binary images/
import numpy as np
from distance.euclidean import euclidean
from distance.minkowski import minkowski
from distance.manhattan import manhattan
A1 = np.array([[1, 4, 3, 4, 5], [1, 5, 3, 4, 5]])
A2 = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])

# print(euclidean(A1, A2))
# print(minkowski(A1, A2, 5))
print(manhattan(A1, A2))
