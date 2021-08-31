import numpy as np

my_list = [1,2,3]
# 1D aarray
print(np.array(my_list))

# 2D array from list of list
my_list_two = [[1,2,3],[4,5,6]]
np_two = np.array(my_list_two)
print(np_two)

# arange() to create array dynamically
print(np.arange(0,10))  # array starting from 0 to 9 default step of 1
print(np.arange(start=0, stop=10, step=2)) # from 0 to 10 step of 2

# Generating array of 0 using np.zeros()
print(np.zeros(3))  # generate 1d array of 0

print(np.zeros((5,5))) # generate 2D array of 0 having 5 rows nd 5 columns

# Generating array of 1 using np.ones()
print(np.ones(4))  # 1D array having 1s
print(np.ones(shape=[2,3]))  # 2D array of 1s hacing 2 rows and 3 columns

# 2 x 3 ndarray full of fives
# np.full(shape, constant value)
X = np.full((2,3), 5)
print("FULL MATRIIX : \n", X)

# Diagonal Matrix
# 4 x 4 diagonal matrix that contains the numbers 10,20,30, and 50 on its main diagonal
X = np.diag([10,20,30,50])
print("DIAGONAL MATRIX : \n", X)

# linspace: it returns an 1D array of numbers between start and stop
# with evenly separated stepsize

print(np.linspace(0, 5, 10))  # give total of 10 items in 1D array start from 5 end at 10

# Identity matrix : same number of rows and columns and diagonal value is 1 and rest
# all values are 0
print(np.eye(4))  # creating identity matrix of size 4(rows=4, column=4)

# creating matrix from random number
print(np.random.rand(5))  # 1D matrix having 5 numbers between 0 & 1
print(np.random.rand(4,4))  # 2D matrix 4x4 nubmer between 0 & 1

# randint()
print(np.random.randint(1,100))  # 1D matrix having a random value between 1 & 99
print(np.random.randint(1,50, 10)) # 1D having 10 values between 1 & 49

# reshape() : to change any dimensional matrix to any order
arr = np.arange(0,25,1)  # 1D array from 0 to 24
arr = arr.reshape(5,5)  # converting 1D array to 2D array of 5x5 size
print(arr)

# max() : get max value from array
print(arr.max())
#min() : get min value
print(arr.min())
# argmax() : returns index of maximum value
print(arr.argmax())
# argmin() : returns index of minimum value
print(arr.argmin())
# shape : get dimenison of matrix
print(arr.shape)
# datatype of array : datatype of array
print(arr.dtype)


Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
print('Y has dimensions:', Y.shape) # Y has dimensions: (4, 3)
print('Y has a total of', Y.size, 'elements') # Y has a total of 12 elements
print('Y is an object of type:', type(Y)) # Y is an object of type: class 'numpy.ndarray'
print('The elements in Y are of type:', Y.dtype) # The elements in Y are of type: int64

# Specify the dtype when creating the ndarray
x = np.array([1.5, 2.2, 3.7, 4.0, 5.9], dtype = np.int64)

# Save the array into a file
np.save('my_array', x)

# Load the saved array from current directory
y = np.load('my_array.npy')
# Arange
# rank 1 ndarray that has sequential integers from 0 to 9
# x = [0 1 2 3 4 5 6 7 8 9]
x = np.arange(10)

# rank 1 ndarray that has sequential integers from 4 to 9
# [start, stop)
# x = [4 5 6 7 8 9]
x = np.arange(4,10)

# rank 1 ndarray that has evenly spaced integers from 1 to 13 in steps of 3.
# np.arange(start,stop,step)
# x = [ 1 4 7 10 13]
x = np.arange(1,14,3)

# Delete
# np.delete(ndarray, elements, axis)
x = np.array([1, 2, 3, 4, 5])
print(x)
# delete the first and fifth element of x
x = np.delete(x, [0,4])
print(x)
Y = np.array([[1,2,3],[4,5,6],[7,8,9]])
# delete the first row of Y
w = np.delete(Y, 0, axis=0)
# delete the first and last column of Y
v = np.delete(Y, [0,2], axis=1)

# Append
# np.append(ndarray, elements, axis)
# append the integer 6 to x
x = np.append(x, 6)
# append the integer 7 and 8 to x
x = np.append(x, [7,8])
# append a new row containing 7,8,9 to y
v = np.append(Y, [[10,11,12]], axis=0)
# append a new column containing 9 and 10 to y
q = np.append(Y,[[13],[14],[15]], axis=1)

# Insert
# np.insert(ndarray, index, elements, axis)
# inserts the given list of elements to ndarray right before
# the given index along the specified axis
x = np.array([1, 2, 5, 6, 7])
Y = np.array([[1,2,3],[7,8,9]])
# insert the integer 3 and 4 between 2 and 5 in x.
x = np.insert(x,2,[3,4])
# insert a row between the first and last row of Y
w = np.insert(Y,1,[4,5,6],axis=0)
# insert a column full of 5s between the first and second column of Y
v = np.insert(Y,1,5, axis=1)

# Copy
# if we want to create a new ndarray that contains a copy of the
# values in the slice we need to use the np.copy()
# create a copy of the slice using the np.copy() function
Z = np.copy(X[1:4,2:5])
#  create a copy of the slice using the copy as a method
W = X[1:4,2:5].copy()

# Extract elements along the diagonal
d0 = np.diag(X)
# As default is k=0, which refers to the main diagonal.
# Values of k > 0 are used to select elements in diagonals above
# the main diagonal, and values of k < 0 are used to select elements
# in diagonals below the main diagonal.
print(X)
d1 = np.diag(X, k=1)
d2 = np.diag(X, k=-1)

print(d1, d2)

# Boolean Indexing
X = np.arange(25).reshape(5, 5)
print('The elements in X that are greater than 10:', X[X > 10])
print('The elements in X that less than or equal to 7:', X[X <= 7])
print('The elements in X that are between 10 and 17:', X[(X > 10) & (X < 17)])

# use Boolean indexing to assign the elements that
# are between 10 and 17 the value of -1
X[(X > 10) & (X < 17)] = -1

# Set Operations
x = np.array([1,2,3,4,5])
y = np.array([6,7,2,8,4])
print('The elements that are both in x and y:', np.intersect1d(x,y))
print('The elements that are in x that are not in y:', np.setdiff1d(x,y))
print('All the elements of x and y:',np.union1d(x,y))

# Sorting
# When used as a function, it doesn't change the original ndarray
s = np.sort(x)
# When used as a method, the original array will be sorted
x.sort()
# sort x but only keep the unique elements in x
s = np.sort(np.unique(x))
# sort the columns of X
s = np.sort(X, axis = 0)
# sort the rows of X
s = np.sort(X, axis = 1)


# NumPy allows element-wise operations on ndarrays as well as
# matrix operations. In order to do element-wise operations,
# NumPy sometimes uses something called Broadcasting.
# Broadcasting is the term used to describe how NumPy handles
# element-wise arithmetic operations with ndarrays of different shapes.
# For example, broadcasting is used implicitly when doing arithmetic
# operations between scalars and ndarrays.
x = np.array([1,2,3,4])
y = np.array([5.5,6.5,7.5,8.5])
np.add(x,y)
np.subtract(x,y)
np.multiply(x,y)
np.divide(x,y)

# in order to do these operations the shapes of the ndarrays
# being operated on, must have the same shape or be broadcastable
X = np.array([1,2,3,4]).reshape(2,2)
Y = np.array([5.5,6.5,7.5,8.5]).reshape(2,2)
np.add(X,Y)
np.subtract(X,Y)
np.multiply(X,Y)
np.divide(X,Y)

# Statistical Functions
print('Average of all elements in X:', X.mean())
print('Average of all elements in the columns of X:', X.mean(axis=0))
print('Average of all elements in the rows of X:', X.mean(axis=1))
print()
print('Sum of all elements in X:', X.sum())
print('Standard Deviation of all elements in X:', X.std())
print('Median of all elements in X:', np.median(X))
print('Maximum value of all elements in X:', X.max())
print('Minimum value of all elements in X:', X.min())