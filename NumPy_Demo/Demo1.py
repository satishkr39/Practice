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
