# Distance between binary images binary images/
import numpy as np
from distance.euclidean import euclidean
A1 = np.array([[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]])
A2 = np.array([[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]])

print(euclidean(A1, A2))
