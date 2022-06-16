import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
#2 - > 5
print(arr[1:5])
#4 - > 6
print(arr[3:-1])
#3   5   7
print(arr[2:8:2])