import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])

print(arr[0] + arr[1])

arr2 = np.array([[1,2,3], [4,5,6]])

print(arr2)

print(arr2[0][0] + arr2[1][1] + arr2[0][2])
#          1     +     5      +     3        = 9

print(arr2[0][0].all())

print(arr2[-1][-1])

print(arr2.shape[0])

print(arr2[1][-1])