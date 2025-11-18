import numpy as np

narr = np.array([[1., 0., 0.], [0., 1., 2.]])
narr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(narr.ndim) #prints out the number of dimensions (axes) of the np array -- 2
# print(narr.shape) # prints out the tuple of integers in each dimension of the np array [rows, columns, depth] -- (2, 3)
# print(narr.size) # prints out the total number of elements in the array; also the product of tuple returned by the shape
# print(narr.dtype) # prints out the data type of the elements of the numpy array

narr[0] = 30
mv = memoryview(narr2.data)
# print(mv[2]) # we can also access data through the buffer returned by ndarray.data

# print(type(narr)) # <class 'numpy.ndarray'>

# -----------------------------------------------------------------------------------------------------------------------

narr3 = np.array((1, 2, 4, 5, 6), 
                 dtype=int,
                 copy=True,
                 order='F',
                 subok=False,
                 ndmin=1,
                 like=None)
# print(narr3)

# narr4 = np.copy(narr3)
# print(narr4)

# -----------------------------------------------------------------------------------------------------------------------

narr5 = np.zeros((2, 3), dtype=int)
narr6 = np.ones((2, 3), dtype=int)
narr7 = np.empty((2, 3), dtype=float)
# print(narr5)
# print(narr6)
# print(narr7)

# -----------------------------------------------------------------------------------------------------------------------

narr8 = np.array([
    [3, 5, 6],
    [89,1, 24],
    [66, 21, 17]
])

narr9 = np.sort(narr8) # returns the sorted array; returns flattened sorted array if axis is set to None
narr10 = np.argsort(narr8) # returns an array of indices of the same shape as a that index data along the given axis in sorted order.
# print(narr10)

narr11 = np.concatenate((narr2, narr8)) #concatenates arrays of same shape; if axis=None, the arrays are flattened first and then concatenated
# print(narr11)


