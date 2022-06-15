import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(np.__version__)

print(type(arr))
#numpy.ndarray
arr = np.array((1, 2, 3, 4, 5))

print(arr)

print(type(arr))

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a)
print(b)
print(c)
print(d)
#print dimension of array
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print(arr.ndim)